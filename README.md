# Agent SDK Practice

Practice project for learning the [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/quickstart) in Python. It contains three small agents that review, fix, and test the code in `utils.py`.

## The agents

| Script | What it does | Tools allowed |
|---|---|---|
| `agent.py` | **Fixer**: finds crash bugs in `utils.py` and fixes them. A system prompt sets the rules: PEP 8, type hints, docstrings, and raising `ValueError` instead of hiding bad input. | Read, Edit, Glob |
| `detector.py` | **Detector**: reports bugs without changing any files. | Read, Glob, Grep (Edit, Write and Bash blocked) |
| `tester.py` | **Tester**: writes unit tests, runs them, and fixes any failures. | Read, Edit, Write, Glob, Grep, Bash |

`utils.py` began as the quickstart's buggy example. `test_utils.py` holds the 24 tests that `tester.py` wrote.

## What I learned

- **`allowed_tools` only auto-approves tools; it doesn't block the others.** To block a tool, use `disallowed_tools`. To limit the agent to a fixed set of tools, use `tools`.
- **`permission_mode="acceptEdits"`** approves file edits automatically, but not shell commands.
- **`system_prompt` vs `prompt`:** the system prompt sets the agent's role and lasting rules, while the prompt is the task for this run.
- **An agent that can run its own tests catches its own mistakes.** Without Bash, the fixer reported success on code that still crashed.
- **`strict_mcp_config=True`** stops the agent from loading MCP connectors from the logged-in account (least privilege).
- **`Done: success` means the agent finished, not that the code is correct.** Check the results yourself.

## Setup

Requirements: Python 3.10+, [uv](https://docs.astral.sh/uv/), and Claude Code logged in.

```bash
uv sync                # install dependencies from uv.lock
uv run detector.py     # report bugs (read-only)
uv run agent.py        # fix bugs
uv run tester.py       # write tests, run them, fix failures
uv run python -m unittest test_utils
```

**Authentication:** for local learning, these scripts use the Claude Code login on this machine. An agent built for other people should use an `ANTHROPIC_API_KEY` from the [Claude Console](https://platform.claude.com/), as the SDK docs say.

## Next steps

- Hooks: block dangerous Bash commands before they run
- Sessions: multi-turn agents that remember the conversation
