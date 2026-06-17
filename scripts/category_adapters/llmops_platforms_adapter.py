"""
LLMOps Platforms Adapter — Template for smoke gate integration.

Each tool on the roster needs a concrete adapter that implements the LLMOpsAdapter
contract defined in smoke_gate.py. This module provides the factory function
get_adapter(tool_name) that returns the correct adapter instance.

To add a new adapter:
1. Create a class inheriting from LLMOpsAdapter (imported from smoke_gate)
2. Implement setup(), work(), teardown(), get_name(), get_sub_category()
3. Add it to the ADAPTERS dict below
4. Run: python smoke_gate.py --tool <name>

Example adapters (pseudocode) are provided for reference.
"""

import sys
import os

# Add parent directory to path so we can import the base adapter
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from smoke_gate import LLMOpsAdapter


class SimulatedDifyAdapter(LLMOpsAdapter):
    """Simulated adapter for Dify — reference implementation."""

    def get_name(self):
        return "Dify"

    def get_sub_category(self):
        return "workflow-builder"

    def setup(self, config):
        # In production: docker compose up -d
        # Wait for health check on localhost:3001
        self.setup_method = "docker compose"
        pass

    def work(self, workload):
        # In production: create workflow app via API, add nodes/edges, execute
        return {"workflow_id": "simulated", "status": "completed", "nodes": workload.get("nodes", 3)}

    def teardown(self):
        # In production: docker compose down, remove volumes
        pass


class SimulatedLangGraphAdapter(LLMOpsAdapter):
    """Simulated adapter for LangGraph — reference implementation."""

    def get_name(self):
        return "LangGraph"

    def get_sub_category(self):
        return "agent-framework"

    def setup(self, config):
        # In production: pip install langgraph
        self.setup_method = "pip install"
        pass

    def work(self, workload):
        # In production: define StateGraph, compile, invoke with inputs
        return {"graph_state": "simulated", "agents": workload.get("agents", 2)}

    def teardown(self):
        # In production: cleanup temp files, stop any running processes
        pass


class SimulatedLangfuseAdapter(LLMOpsAdapter):
    """Simulated adapter for Langfuse — reference implementation."""

    def get_name(self):
        return "Langfuse"

    def get_sub_category(self):
        return "observability"

    def setup(self, config):
        # In production: docker compose up -d or connect to cloud API
        self.setup_method = "docker compose or cloud API"
        pass

    def work(self, workload):
        # In production: ingest traces via SDK, query back via API
        return {"traces_ingested": workload.get("spans", 5), "status": "ok"}

    def teardown(self):
        # In production: docker compose down, delete test project
        pass


# Registry of all implemented adapters
ADAPTERS = {
    "dify": SimulatedDifyAdapter,
    "langgraph": SimulatedLangGraphAdapter,
    "langfuse": SimulatedLangfuseAdapter,
    # Add more adapters here as they are implemented
    # "braintrust": SimulatedBraintrustAdapter,
    # "crewai": SimulatedCrewAIAdapter,
    # "n8n": SimulatedN8nAdapter,
    # "flowise": SimulatedFlowiseAdapter,
    # "promptlayer": SimulatedPromptLayerAdapter,
    # "helicone": SimulatedHeliconeAdapter,
    # "comet-opik": SimulatedCometOpikAdapter,
}


def get_adapter(tool_name: str) -> LLMOpsAdapter:
    """
    Factory function: returns an adapter instance for the given tool name.
    Tool name is case-insensitive and spaces are normalized.
    """
    key = tool_name.lower().replace(" ", "-").replace(".", "").replace("&", "and")
    # Also try without hyphens
    key_alt = key.replace("-", "")

    if key in ADAPTERS:
        return ADAPTERS[key]()
    if key_alt in ADAPTERS:
        return ADAPTERS[key_alt]()

    # Try common aliases
    aliases = {
        "openai-agents-sdk": "openai-agents",
        "comet-opik": "opik",
        "semantic-kernel": "semantickernel",
    }
    if key in aliases and aliases[key] in ADAPTERS:
        return ADAPTERS[aliases[key]]()

    raise ValueError(f"No adapter implemented for tool '{tool_name}' (key: {key}). "
                     f"Add it to category_adapters/llmops_platforms_adapter.py")
