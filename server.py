from mcp.server.fastmcp import FastMCP

from search import search_web
from scraper import fetch_page_content

mcp = FastMCP("Search MCP")


@mcp.tool()
def web_search(query: str):
    """
    Search the web and return content from top results.
    """
    print(f"SEARCH CALLED: {query}")

    search_results = search_web(query)

    final_results = []

    for result in search_results[:3]:
        url = result.get("href")

        content = fetch_page_content(url)

        final_results.append(
            {
                "title": result.get("title"),
                "url": url,
                "snippet": result.get("body"),
                "content": content,
            }
        )

    return final_results


# Create ASGI app for deployment
app = mcp.streamable_http_app()