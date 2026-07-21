# Contributing to Al Jazeera 360 MCP Server

Thank you for your interest in contributing! Here's how to get started.

## Development Setup

```bash
git clone https://github.com/ahmedaminsa/aljazeera360-mcp-server.git
cd aljazeera360-mcp-server
pip install -r requirements.txt
pip install -e ".[dev]"  # installs pytest for development
```

## Running Tests

```bash
# Integration tests against live API (requires internet + valid token)
python test_server.py
```

The 8 core tools are tested end-to-end against the production API. Set `AJ360_REFRESH_TOKEN` environment variable for authenticated access. The 16 optional SEO/analytics tools are registered only when `AJ360_ENABLE_SEO_TOOLS=1` (24 tools total).

## Making Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Run tests: `python test_server.py`
5. Commit: `git commit -m "feat: description of change"`
6. Push: `git push origin feature/your-feature`
7. Open a Pull Request

## Commit Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` — New feature or tool
- `fix:` — Bug fix
- `docs:` — Documentation changes
- `refactor:` — Code refactoring
- `test:` — Adding or updating tests
- `chore:` — Maintenance (CI, deps, etc.)

## Adding a New Tool

1. Add the API method to `AlJazeera360Client` class
2. Create the MCP tool function with `@mcp.tool()` decorator
3. Include bilingual docstring (English + Arabic)
4. Add a test case in `test_server.py`
5. Update README with the new tool

## Code Style

- Python 3.10+ type hints
- Async/await for all API calls
- Descriptive variable names
- Comments for non-obvious logic

## Questions?

Open an issue on GitHub.
