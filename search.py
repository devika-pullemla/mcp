from ddgs import DDGS


def search_web(query: str, max_results: int = 3):
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=max_results))

    return results