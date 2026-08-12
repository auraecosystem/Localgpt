import localgpt

# Start an interactive chat
localgpt chat

# Launch the terminal UI
localgpt tui

# Ask a single question
localgpt ask "What is the capital of France?"

# Use a specific model
localgpt -m anthropic/claude-sonnet-4-5 chat

# Start the daemon
localgpt daemon start

# Search memory
localgpt memory search "project ideas"

# Show memory statistics
localgpt memory stats

# Configuration management
localgpt config init              # Create default config
localgpt config show              # Display loaded config
localgpt config get agent.default_model   # Get a specific value
localgpt config set agent.default_model "claude-cli/opus"

# Check sandbox capabilities
localgpt sandbox status

# Sign LocalGPT.md after editing
localgpt md sign

# View security audit log
localgpt md audit

# Launch world generation (separate binary)
localgpt-gen "create a solar system with planets"

# Test web search provider
localgpt search test

# Initialize config and device keys (first-time setup)
localgpt init

# Run setup diagnostics (config, keys, providers, MCP)
localgpt doctor

# Show resolved directory paths
localgpt paths

# Generate shell completion
localgpt completion bash > /etc/bash_completion.d/localgpt
localgpt completion zsh > "${fpath[1]}/_localgpt"
localgpt completion fish > ~/.config/fish/completions/localgpt.fish

# Manage cron jobs
localgpt cron list
localgpt cron add "0 */6 * * *" "Summarize recent memory and update MEMORY.md"
localgpt cron remove <job-id>

# Manage lifecycle hooks
localgpt hooks list
localgpt hooks set beforeToolCall "/path/to/hook.sh"

# Manage MCP tool servers
localgpt tool list                # List servers with enabled/disabled status
localgpt tool add myserver --command "npx" -- "@anthropic/mcp-searxng"
localgpt tool enable myserver     # Enable a disabled server
localgpt tool disable myserver    # Disable without removing
localgpt tool remove myserver     # Remove from config

# Compaction audit log
localgpt audit show               # Show recent compaction events
localgpt audit show --limit 5     # Show last 5 events
localgpt audit show --json        # JSON output
localgpt audit verify             # Verify hash chain integrity
localgpt audit stats              # Show compaction statistics

# Session management and compaction checkpoints
localgpt session list                          # List recent sessions
localgpt session branch <session-id>           # Branch a session into a new one
localgpt session checkpoints                   # List checkpoints for the latest session
localgpt session restore 2                     # Restore latest session from checkpoint #2

# Run as an MCP server (stdio) for external AI backends
localgpt mcp-server

# Manage TLS certificates for the HTTP server
localgpt cert info                # Show certificate expiry, SANs, and paths
localgpt cert regenerate          # Force certificate regeneration
