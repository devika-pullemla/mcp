import requests
from bs4 import BeautifulSoup


def fetch_page_content(url: str):
    try:
        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        text = soup.get_text(separator=" ", strip=True)

        return text[:5000]

    except Exception as e:
        return f"Error fetching page: {str(e)}"