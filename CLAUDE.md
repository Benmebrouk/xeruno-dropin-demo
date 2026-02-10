# CLAUDE.md

## Project Overview

Xeruno Drop-in Demo is a minimal Python CLI application demonstrating a drop-in replacement for OpenAI's API using a local LLM via Ollama. The core idea: swap OpenAI for a fully local, zero-cost alternative by changing only 2 lines of code (the `base_url` and `api_key` in the OpenAI client constructor). The project is in **alpha** status.

## Repository Structure

```
.
├── demo.py           # Main demo script (124 lines) - runs OpenAI vs Xeruno comparison
├── run.sh            # Setup script - installs deps, starts Ollama, pulls model
├── requirements.txt  # Single dependency: openai>=1.0.0
├── README.md         # User-facing documentation
├── SPONSORS.md       # Sponsorship information
├── LICENSE.md        # MIT + Commercial Extension License
└── CLAUDE.md         # This file
```

This is an intentionally minimal project with no build system, no test framework, and no configuration files beyond `requirements.txt`.

## Tech Stack

- **Language:** Python 3.8+
- **Package manager:** pip
- **Single dependency:** `openai>=1.0.0` (the official OpenAI Python SDK)
- **Local LLM runtime:** Ollama (system-level dependency, not a pip package)
- **UI:** Terminal with ANSI color codes (no web interface)

## Architecture

The project has a single entry point (`demo.py`) with three functions:

1. **`run_openai()`** - Calls the OpenAI API using the standard SDK. Skipped if `OPENAI_API_KEY` is not set. Uses model `gpt-4o-mini`.
2. **`run_Xeruno()`** - Identical logic but with `base_url="http://127.0.0.1:11434/v1"` and `api_key="xeruno"`, pointing to a local Ollama server. Uses model `llama3`.
3. **`main()`** - Orchestrates both runs and displays a side-by-side comparison of latency, token count, cost, and network usage.

Both functions use the same OpenAI Python SDK with streaming enabled. The only difference between them is the client constructor arguments.

### Data flow

```
main() -> run_openai()  -> OpenAI(default)                 -> api.openai.com
       -> run_Xeruno()  -> OpenAI(base_url=localhost:11434) -> local Ollama
       -> compare metrics and print results
```

Each function returns a dict: `{"tokens": int, "latency": float, "cost": float}`.

## Development Workflow

### Setup

```bash
./run.sh        # Checks prerequisites (python3, curl, ollama), installs deps, starts Ollama, pulls llama3
```

### Running

```bash
python demo.py  # Runs the comparison demo
```

### Prerequisites

- `python3` installed
- `curl` installed
- `ollama` installed and available on PATH (see https://ollama.ai/download)

### Environment Variables

| Variable | Required | Purpose |
|----------|----------|---------|
| `OPENAI_API_KEY` | No | If set, enables the OpenAI comparison. If unset, only the local Xeruno demo runs. |

No `.env` file support exists. All other configuration (Ollama URL, model names, API key) is hardcoded in `demo.py`.

## Key Conventions

### Code Style

- No linter or formatter is configured
- Standard Python conventions (PEP 8 loosely followed)
- ANSI color constants defined at module level (`GREEN`, `BLUE`, `YELLOW`, `RESET`, `BOLD`)
- Functions use snake_case except `run_Xeruno` which uses PascalCase for the product name

### Error Handling

- Missing `OPENAI_API_KEY`: gracefully skips OpenAI demo with a warning
- Ollama not running: caught by try/except in `main()`, prints instructions to run `./run.sh`
- `run.sh` uses `set -e` to exit on first error

### No Tests

There is no test framework, test directory, or CI/CD pipeline. The project is validated by manually running `python demo.py`.

## Important Notes for AI Assistants

- This is a **demo/proof-of-concept** project, not a production application
- The entire codebase is ~160 lines across 2 executable files (`demo.py` + `run.sh`)
- The OpenAI SDK is reused for both remote and local calls - Ollama implements an OpenAI-compatible `/v1` REST API
- The hardcoded values (model names, URLs, cost estimates) are intentional for demo simplicity
- The README mentions `qwen2.5:7b` as recommended model but `demo.py` actually uses `llama3` - this is a known inconsistency
- License is MIT + Commercial Extension: free for non-commercial use, commercial use requires a separate license
