from langchain_community.tools.tavily_search import TavilySearchResults
import os
import requests


def get_profile_url_tavily(name: str):
    """Searches for Github Profile Page."""

    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res


def search_github_by_name(full_name: str) -> str:
    """
    Search github user by a full name and return the best matching url;
    """

    query = f"fullname:{full_name}"
    url = f"https://api.github.com/search/users?q={query}"

    github_token = os.getenv("GITHUB_API_KEY")

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {github_token}",
    }
    response = requests.get(url, headers=headers)
    return response.json()
