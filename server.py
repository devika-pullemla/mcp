from mcp.server.fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastmcp import FastMCP
from search import search_web
from scraper import fetch_page_content

mcp = FastMCP("Search MCP")


@mcp.custom_route("/", methods=["GET"])
async def root(request: Request):
    return JSONResponse(
        {
            "service": "Search MCP",
            "status": "running",
        }
    )


@mcp.custom_route("/health", methods=["GET"])
async def health(request: Request):
    return JSONResponse(
        {
            "status": "healthy",
        }
    )


@mcp.custom_route("/test", methods=["GET"])
async def test(request: Request):
    return JSONResponse(
        {
            "message": "Custom route working",
        }
    )
@mcp.tool()
def web_search(query: str):
    """
    Search the web and return content from top results.
    """

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



if __name__ == "__main__":
    port = 8000

    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=port,
    )