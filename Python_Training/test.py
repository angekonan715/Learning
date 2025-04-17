import requests
from bs4 import BeautifulSoup

def scrape_rfc1149():
    """
    Scrapes the text content of RFC 1149.
    """

    url = "https://pythonscraping.com/linkedin/ietf.html"  # URL for RFC 1149

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # The content is plain text, so we don't need BeautifulSoup for parsing
        rfc_text = response.text

        return rfc_text

    except requests.exceptions.RequestException as e:
        print(f"Error fetching RFC 1149: {e}")
        return None

if __name__ == "__main__":
    rfc1149_content = scrape_rfc1149()
    if rfc1149_content:
        print(rfc1149_content)