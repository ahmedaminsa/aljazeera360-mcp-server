# Examples

Standalone scripts demonstrating how to use the Al Jazeera 360 MCP Server tools programmatically.

## Setup

```bash
cd aljazeera360-mcp-server
pip install -r requirements.txt
export AJ360_REFRESH_TOKEN="your-token"  # optional, works in guest mode too
```

## Scripts

| Script | Description |
| :--- | :--- |
| `search_documentaries.py` | Search for videos by topic with direct watch links |
| `trending_content.py` | Fetch homepage featured content and categories |
| `explore_series.py` | Find a series, list seasons, and show episodes |

## Usage

```bash
python examples/search_documentaries.py "فلسطين"
python examples/trending_content.py
python examples/explore_series.py "الدحيح"
```

## Note

These scripts call the same API methods used by the MCP server tools. They are useful for:
- Testing your authentication setup
- Understanding the data structure
- Building custom integrations without MCP
