import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage


async def main():
    # Read-only agent: finds bugs and reports them, never changes files
    async for message in query(
        prompt=(
            "Review utils.py for bugs that would cause crashes. "
            "Do NOT fix anything. For each bug, report the function name, "
            "an example input that crashes it, and the error it raises."
        ),
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Glob", "Grep"],  # Auto-approve these (read-only)
            disallowed_tools=["Edit", "Write", "Bash"],  # Block these completely
            strict_mcp_config=True,  # Only MCP servers listed in mcp_servers (none)
        ),
    ):
        # Print human-readable output
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)  # Claude's reasoning
                elif hasattr(block, "name"):
                    print(f"Tool: {block.name}")  # Tool being called
        elif isinstance(message, ResultMessage):
            print(f"Done: {message.subtype}")  # Final result


asyncio.run(main())
