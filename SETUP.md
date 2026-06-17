# Setting up the GitHub Repository

This guide walks you through pushing the LLMOps Platforms & Workflow Automation Almanac to GitHub and setting up automation for regular updates.

## Step 1: Create the GitHub repository

```bash
# Option A: Via GitHub CLI (if installed)
gh repo create ai-llmops-almanac --public --description "A living encyclopedia of LLMOps platforms, workflow automation, and prompt management tools." --license cc-by-4.0

# Option B: Via GitHub web UI
# 1. Go to https://github.com/new
# 2. Name: ai-llmops-almanac
# 3. Description: A living encyclopedia of LLMOps platforms, workflow automation, and prompt management tools
# 4. Visibility: Public
# 5. License: CC BY 4.0
# 6. Click "Create repository"
```

## Step 2: Initialize and push the local repo

```bash
cd /path/to/ai-llmops-almanac

git init
git add .
git commit -m "Founding edition: 64 LLMOps Platforms & Workflow Automation tools, June 2026"

# Add your GitHub remote
git remote add origin https://github.com/YOUR_USERNAME/ai-llmops-almanac.git
# OR if using SSH:
git remote add origin git@github.com:YOUR_USERNAME/ai-llmops-almanac.git

git branch -M main
git push -u origin main
```

## Step 3: Enable GitHub Actions for automated updates (optional)

Create `.github/workflows/monthly-update.yml`:

```yaml
name: Monthly Edition Update

on:
  schedule:
    - cron: '0 7 1 * *'  # 7:00 AM UTC on the 1st of each month
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      - name: Update metadata
        run: |
          # This is where you'd run a script to refresh GitHub stars,
          # last push dates, release notes, etc.
          echo "$(date +%Y-%m-%d) Monthly update triggered" >> editions/update.log
      - name: Commit and push
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add -A
          git commit -m "Monthly edition update: $(date +%Y-%m)" || echo "No changes"
          git push
```

## Step 4: Set up a cron job for research (local agent)

The research and benchmark updates are run by an agent on a schedule. To set this up in Kimi Work:

```bash
# The cron job has been configured to run monthly on the 15th at 07:00 AM
# It will refresh the research, update editions, and flag new tools for triage.
```

The cron job is configured via the Kimi Work `Cron` tool with:
- **Trigger**: `cron` expression `0 7 15 * *` (monthly, 15th at 7:00 AM)
- **Workspace**: Your local workspace
- **Prompt**: "Refresh the LLMOps Almanac: check for new tools, updated metadata, notable releases, and prepare the next edition draft."

## Directory structure after setup

```
ai-llmops-almanac/
├── README.md                          # Project overview + roster at a glance
├── INTENT.md                          # Philosophy, design principles, governance
├── IMPLEMENTATION.md                    # How the almanac is built
├── TESTING.md                         # Benchmark methodology, harness details
├── TROUBLESHOOTING.md                 # Common issues, debugging, FAQ
├── CONTRIBUTING.md                    # How to contribute
├── architecture.md                    # Stack architecture + test philosophy
├── SETUP.md                           # This file
├── .gitignore
│
├── editions/                          # Monthly editions
│   └── 2026-06.md                   # Founding edition
│
├── benchmarks/                        # Benchmark results (rolling)
│   └── smoke-gate-2026-06.md        # Smoke gate results
│
├── methodology/
│   └── benchmark-harness.md         # Detailed harness spec for LLMOps
│
├── data/
│   └── roster.json                  # Machine-readable catalog (64 tools)
│
├── tools/                             # Per-tool deep-dive pages
│   ├── dify.md
│   ├── flowise.md
│   ├── n8n.md
│   └── ... (31 Tier A tools + 33 Tier B tools)
│
└── assets/                            # Charts, diagrams, screenshots
    └── (populated by editions)
```

## License

Content: CC BY 4.0  
Code/harness: MIT
