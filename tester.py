import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage


async def main():
    # Agent that writes tests, runs them, and fixes failures
    async for message in query(
        prompt="Write unit tests for utils.py, run them, and fix any failures.",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Edit", "Write", "Glob", "Grep", "Bash"],  # Bash = run commands
            permission_mode="acceptEdits",  # Auto-approve file edits
            strict_mcp_config=True,  # Only MCP servers listed in mcp_servers (none)
            system_prompt=(
                "You are a senior Python developer. Always follow PEP 8. "
                "Never hide bad input by returning default values like 0 or empty strings; "
                "raise a ValueError with a clear message instead. "
                "This project uses uv: run Python with `uv run python` and tests with "
                "`uv run python -m unittest`. Test edge cases such as empty input and None."
            ),
        ),
    ):
        # Print human-readable output
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)  # Claude's reasoning
                elif hasattr(block, "name"):
                    # Also show the command when the agent uses Bash
                    command = block.input.get("command") if block.name == "Bash" else None
                    print(f"Tool: {block.name}" + (f" -> {command}" if command else ""))
        elif isinstance(message, ResultMessage):
            print(f"Done: {message.subtype}")  # Final result


asyncio.run(main())
