#!/usr/bin/env python3
"""
Refresh Metadata — Update GitHub metadata for every tool on the LLMOps Almanac roster.

Usage:
    python refresh_metadata.py          # Refresh all tools
    python refresh_metadata.py --dry-run  # Show what would change

This script:
1. Reads data/roster.json (flat tools array)
2. For each tool with a GitHub URL, fetches stars, last push date, and release info
3. Updates the roster with new metadata
4. Writes a summary of changes

Note: The LLMOps Almanac roster uses a flat "tools" array (not nested categories
like the parent AI Infrastructure Almanac).
"""

import argparse
import json
import logging
import os
import re
from datetime import datetime, timezone

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger('refresh_metadata')


def load_roster(path: str) -> dict:
    with open(path, 'r') as f:
        return json.load(f)


def save_roster(path: str, roster: dict) -> None:
    with open(path, 'w') as f:
        json.dump(roster, f, indent=2)


def parse_github_url(notes: str) -> tuple:
    """Extract owner/repo from tool notes or return None."""
    # Try to find github.com/owner/repo pattern in notes
    match = re.search(r'github\.com/([^/\s]+)/([^/\s\)]+)', notes)
    if match:
        return match.group(1), match.group(2)
    return None, None


def simulate_github_api(owner: str, repo: str) -> dict:
    """
    Simulated GitHub API fetch.
    In production, this would use the GitHub REST API with a token:
        curl -H "Authorization: token $GITHUB_TOKEN" \
             https://api.github.com/repos/{owner}/{repo}
    Returns stars, last_push, and release info.
    """
    return {
        'stars': 0,  # placeholder — fetch from https://api.github.com/repos/{owner}/{repo}
        'last_push': datetime.now(timezone.utc).isoformat(),
        'release_count': 0,
        'open_issues': 0,
        'open_prs': 0,
        'fetched_at': datetime.now(timezone.utc).isoformat(),
        'simulated': True
    }


def refresh_tool_metadata(tool: dict, dry_run: bool = False) -> dict:
    """Refresh metadata for a single tool. Returns the updated tool dict."""
    # Try to infer GitHub URL from notes or name
    owner, repo = parse_github_url(tool.get('notes', ''))

    if not owner or not repo:
        # Common mappings for known tools
        known_repos = {
            'Dify': ('langgenius', 'dify'),
            'Flowise': ('FlowiseAI', 'Flowise'),
            'n8n': ('n8n-io', 'n8n'),
            'LangChain': ('langchain-ai', 'langchain'),
            'LangGraph': ('langchain-ai', 'langgraph'),
            'LlamaIndex': ('run-llama', 'llama_index'),
            'CrewAI': ('crewAIInc', 'crewAI'),
            'AutoGen': ('microsoft', 'autogen'),
            'Mastra': ('mastra-ai', 'mastra'),
            'Pydantic AI': ('pydantic', 'pydantic-ai'),
            'DSPy': ('stanfordnlp', 'dspy'),
            'Haystack': ('deepset-ai', 'haystack'),
            'ZenML': ('zenml-io', 'zenml'),
            'Temporal': ('temporalio', 'temporal'),
            'Langfuse': ('langfuse', 'langfuse'),
            'MLflow': ('mlflow', 'mlflow'),
            'Helicone': ('Helicone', 'helicone'),
            'Comet Opik': ('comet-ml', 'opik'),
            'AgentOps': ('AgentOps-AI', 'agentops'),
            'TruLens': ('truera', 'trulens'),
            'Lunary': ('lunary-ai', 'lunary'),
            'RAGflow': ('infiniflow', 'ragflow'),
            'BISHENG': ('dataelement', 'bisheng'),
            'FastGPT': ('labring', 'FastGPT'),
            'Botpress': ('botpress', 'botpress'),
            'Langflow': ('langflow-ai', 'langflow'),
            'Rasa': ('RasaHQ', 'rasa'),
            'Promptfoo': ('promptfoo', 'promptfoo'),
            'OpenLIT': ('openlit', 'openlit'),
        }
        name = tool.get('name', '')
        if name in known_repos:
            owner, repo = known_repos[name]

    if not owner or not repo:
        logger.debug(f"Skipping {tool['name']}: no GitHub URL inferred")
        return tool

    meta = simulate_github_api(owner, repo)

    if not dry_run:
        tool['github_metadata'] = meta
        tool['last_refreshed'] = datetime.now(timezone.utc).isoformat()

    return tool


def main():
    parser = argparse.ArgumentParser(description='Refresh GitHub metadata for the LLMOps roster')
    parser.add_argument('--dry-run', action='store_true', help='Show changes without writing')
    parser.add_argument('--roster', default='../data/roster.json', help='Path to roster.json')
    parser.add_argument('--tier', help='Only refresh a specific tier (A, B, C)')
    args = parser.parse_args()

    roster_path = os.path.join(os.path.dirname(__file__), args.roster)
    roster = load_roster(roster_path)

    tools = roster.get('tools', [])
    total_tools = 0
    refreshed = 0

    for tool in tools:
        if args.tier and tool.get('tier') != args.tier:
            continue
        total_tools += 1
        refresh_tool_metadata(tool, dry_run=args.dry_run)
        refreshed += 1

    # Update meta
    roster['meta']['generated_at'] = datetime.now(timezone.utc).isoformat()
    roster['meta']['version'] = datetime.now(timezone.utc).strftime('%Y-%m')

    if not args.dry_run:
        save_roster(roster_path, roster)
        logger.info(f"Roster updated: {refreshed} tools refreshed, {total_tools} total")
    else:
        logger.info(f"DRY RUN: Would refresh {refreshed} tools, {total_tools} total")


if __name__ == '__main__':
    main()
