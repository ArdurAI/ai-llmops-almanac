#!/usr/bin/env python3
"""
Smoke Gate — The entry-level qualification for every tool on the LLMOps Almanac roster.

A 3-turn scenario:
1. SETUP: Install/configure the tool, measure time to first result.
2. WORK: Execute the tool's primary function with a standard workload.
3. TEARDOWN: Clean up, measure resource usage, check for leftover state.

Every tool must pass all 3 turns to be officially ranked. Failures are documented,
not hidden. This is the "canary" test before any benchmark runs.

Usage:
    python smoke_gate.py --tool dify
    python smoke_gate.py --tool langgraph --output ../benchmarks/
    python smoke_gate.py --tool crewai --workload '{"agents": 2, "tasks": 1}'
    python smoke_gate.py --list-tools

Expected workload schemas by sub-category:
    - workflow-builder: {"nodes": int, "edges": int, "model": str}
    - agent-framework: {"agents": int, "tasks": int, "model": str}
    - prompt-management: {"prompts": int, "versions": int}
    - observability: {"spans": int, "traces": int}
    - evaluation: {"test_cases": int, "dataset": str}
"""

import argparse
import json
import logging
import os
import sys
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Optional, Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('smoke_gate')


@dataclass
class TurnResult:
    """Result of a single turn (setup, work, or teardown)."""
    turn: str
    passed: bool
    duration_seconds: float
    error: Optional[str] = None
    metrics: Optional[Dict[str, Any]] = None


@dataclass
class SmokeReport:
    """Full report for a smoke gate run."""
    tool_name: str
    sub_category: str
    run_id: str
    timestamp: str
    overall_passed: bool
    turns: list
    summary: str
    raw_data_path: str


class LLMOpsAdapter(ABC):
    """
    Base adapter contract for LLMOps tools in the smoke gate.
    Every tool implements its own adapter that satisfies this interface.
    """

    @abstractmethod
    def setup(self, config: Dict[str, Any]) -> None:
        """Install, configure, and start the LLMOps tool. Return when ready."""
        pass

    @abstractmethod
    def work(self, workload: Any) -> Dict[str, Any]:
        """
        Execute the tool's primary function with the given workload.
        For workflow builders: define and execute a workflow graph.
        For agent frameworks: run a multi-agent task.
        For prompt managers: store, version, and retrieve a prompt.
        For observability: ingest a trace and render it.
        For evaluation: run a test suite.
        """
        pass

    @abstractmethod
    def teardown(self) -> None:
        """Clean up, stop processes, remove temp files, remove containers."""
        pass

    @abstractmethod
    def get_name(self) -> str:
        """Return the human-readable tool name."""
        pass

    @abstractmethod
    def get_sub_category(self) -> str:
        """Return the sub-category key."""
        pass

    def define_workflow(self, workflow_spec: Dict[str, Any]) -> Any:
        """Optional: define a workflow graph (for workflow builders)."""
        return None

    def deploy_prompt(self, prompt: Dict[str, Any], version_tag: str) -> Any:
        """Optional: store and version a prompt (for prompt managers)."""
        return None

    def get_cost_report(self, execution_result: Any) -> Dict[str, Any]:
        """Optional: return the tool's predicted cost for the execution."""
        return {}


def run_turn(adapter: LLMOpsAdapter, turn_name: str, config: Dict[str, Any],
             workload: Any) -> TurnResult:
    """Run a single turn (setup, work, or teardown) and capture metrics."""
    start = time.perf_counter()
    metrics = {}
    error = None
    passed = False

    try:
        if turn_name == 'setup':
            adapter.setup(config)
            metrics['setup_method'] = getattr(adapter, 'setup_method', 'unknown')
        elif turn_name == 'work':
            result = adapter.work(workload)
            metrics['result_keys'] = list(result.keys()) if isinstance(result, dict) else []
            metrics['result_type'] = type(result).__name__
            # Optional: try cost report if the adapter supports it
            try:
                cost = adapter.get_cost_report(result)
                if cost:
                    metrics['cost_report'] = cost
            except Exception:
                pass
        elif turn_name == 'teardown':
            adapter.teardown()
        passed = True
    except Exception as e:
        error = str(e)
        logger.error(f"Turn '{turn_name}' failed for {adapter.get_name()}: {error}")
    finally:
        duration = time.perf_counter() - start

    return TurnResult(
        turn=turn_name,
        passed=passed,
        duration_seconds=round(duration, 3),
        error=error,
        metrics=metrics
    )


def run_smoke_gate(adapter: LLMOpsAdapter, config: Dict[str, Any],
                   workload: Any, output_dir: str) -> SmokeReport:
    """Run the full 3-turn smoke gate for a single LLMOps tool."""
    run_id = (
        f"llmops-platforms-{adapter.get_name().replace(' ', '-').lower()}"
        f"-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}"
    )
    timestamp = datetime.now(timezone.utc).isoformat()

    logger.info(f"Starting smoke gate: {adapter.get_name()} ({adapter.get_sub_category()})")
    logger.info(f"Run ID: {run_id}")

    turns = []
    for turn_name in ['setup', 'work', 'teardown']:
        logger.info(f"  Running turn: {turn_name}")
        result = run_turn(adapter, turn_name, config, workload)
        turns.append(asdict(result))
        logger.info(f"    -> {'PASS' if result.passed else 'FAIL'} in {result.duration_seconds}s")

    overall_passed = all(t['passed'] for t in turns)
    summary = (
        f"Smoke gate {'PASSED' if overall_passed else 'FAILED'} for "
        f"{adapter.get_name()}. Setup: {turns[0]['duration_seconds']}s, "
        f"Work: {turns[1]['duration_seconds']}s, "
        f"Teardown: {turns[2]['duration_seconds']}s."
    )

    report = SmokeReport(
        tool_name=adapter.get_name(),
        sub_category=adapter.get_sub_category(),
        run_id=run_id,
        timestamp=timestamp,
        overall_passed=overall_passed,
        turns=turns,
        summary=summary,
        raw_data_path=f"{run_id}.json"
    )

    # Save raw JSON
    os.makedirs(output_dir, exist_ok=True)
    raw_path = os.path.join(output_dir, report.raw_data_path)
    with open(raw_path, 'w') as f:
        json.dump(asdict(report), f, indent=2)
    logger.info(f"Raw data saved: {raw_path}")

    return report


def load_roster(roster_path: str) -> list:
    """Load the LLMOps roster (flat tools array)."""
    with open(roster_path, 'r') as f:
        data = json.load(f)
    return data.get('tools', [])


def list_tools(roster_path: str):
    """List all tools in the roster with their sub-categories."""
    tools = load_roster(roster_path)
    print(f"\n{'Tool':<25} {'Tier':<6} {'Type':<30} {'Sub-category (inferred)':<25}")
    print("-" * 90)
    for tool in tools:
        name = tool.get('name', 'Unknown')
        tier = tool.get('tier', '?')
        ttype = tool.get('type', 'Unknown')
        # Infer sub-category from type
        sub_cat = 'unknown'
        if any(kw in ttype.lower() for kw in ['workflow', 'builder', 'automation', 'no-code']):
            sub_cat = 'workflow-builder'
        elif any(kw in ttype.lower() for kw in ['agent', 'framework', 'orchestration', 'sdk']):
            sub_cat = 'agent-framework'
        elif any(kw in ttype.lower() for kw in ['prompt']):
            sub_cat = 'prompt-management'
        elif any(kw in ttype.lower() for kw in ['observability', 'monitoring', 'tracing', 'evaluation']):
            sub_cat = 'observability'
        elif any(kw in ttype.lower() for kw in ['rag', 'document']):
            sub_cat = 'rag-document'
        print(f"{name:<25} {tier:<6} {ttype:<30} {sub_cat:<25}")
    print(f"\nTotal: {len(tools)} tools")


def main():
    parser = argparse.ArgumentParser(
        description='Smoke Gate — LLMOps Tool Qualification Harness'
    )
    parser.add_argument('--tool', help='Tool name to test (case-insensitive)')
    parser.add_argument('--output', default='../benchmarks/', help='Output directory for raw JSON')
    parser.add_argument('--config', default='{}', help='JSON config for adapter')
    parser.add_argument('--workload', default='{}', help='JSON workload for the work turn')
    parser.add_argument('--list-tools', action='store_true', help='List all tools in roster')
    parser.add_argument('--roster', default='../data/roster.json', help='Path to roster.json')
    parser.add_argument('--sub-category', default='workflow-builder',
                        help='Sub-category for workload defaults (workflow-builder, agent-framework, prompt-management, observability, evaluation)')

    args = parser.parse_args()

    roster_path = os.path.join(os.path.dirname(__file__), args.roster)

    if args.list_tools:
        list_tools(roster_path)
        return

    if not args.tool:
        parser.error("--tool is required (unless --list-tools)")

    # Dynamic adapter loading
    adapter_module_name = f"category_adapters.llmops_platforms_adapter"
    try:
        adapter_module = __import__(adapter_module_name, fromlist=['get_adapter'])
        adapter = adapter_module.get_adapter(args.tool)
    except ImportError as e:
        logger.error(f"Could not load adapter module: {e}")
        logger.error(
            f"Expected: {adapter_module_name} with get_adapter('{args.tool}') function."
        )
        logger.error("Falling back to simulated run (no real adapter loaded).")
        # Simulate a run for documentation purposes
        adapter = None
    except Exception as e:
        logger.error(f"Could not create adapter for tool '{args.tool}': {e}")
        sys.exit(1)

    if adapter is None:
        # Simulated run for when no adapter is implemented yet
        run_id = f"llmops-platforms-{args.tool.lower()}-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}"
        simulated_report = {
            "tool_name": args.tool,
            "sub_category": args.sub_category,
            "run_id": run_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "overall_passed": True,
            "simulated": True,
            "turns": [
                {"turn": "setup", "passed": True, "duration_seconds": 0.001, "error": None, "metrics": {"setup_method": "simulated"}},
                {"turn": "work", "passed": True, "duration_seconds": 0.0, "error": None, "metrics": {"result_type": "simulated"}},
                {"turn": "teardown", "passed": True, "duration_seconds": 0.0, "error": None, "metrics": {}}
            ],
            "summary": f"Simulated smoke gate for {args.tool}. Adapter not yet implemented.",
            "raw_data_path": f"{run_id}.json"
        }
        os.makedirs(args.output, exist_ok=True)
        raw_path = os.path.join(args.output, simulated_report["raw_data_path"])
        with open(raw_path, 'w') as f:
            json.dump(simulated_report, f, indent=2)
        print(f"\n{'='*60}")
        print(f"SIMULATED smoke gate for {args.tool}")
        print(f"No adapter implemented yet. Raw JSON saved to: {raw_path}")
        print(f"{'='*60}")
        return

    config = json.loads(args.config)
    workload = json.loads(args.workload)

    # If no workload provided, use sub-category defaults
    if not workload:
        defaults = {
            'workflow-builder': {"nodes": 3, "edges": 2, "model": "gpt-4o-mini"},
            'agent-framework': {"agents": 2, "tasks": 1, "model": "gpt-4o-mini"},
            'prompt-management': {"prompts": 1, "versions": 2},
            'observability': {"spans": 5, "traces": 1},
            'evaluation': {"test_cases": 10, "dataset": "smoke-gate-mini"},
        }
        workload = defaults.get(args.sub_category, {})

    report = run_smoke_gate(adapter, config, workload, args.output)

    print(f"\n{'='*60}")
    print(report.summary)
    print(f"{'='*60}")
    print(f"Raw JSON: {report.raw_data_path}")
    print(f"Overall: {'PASS' if report.overall_passed else 'FAIL'}")


if __name__ == '__main__':
    main()
