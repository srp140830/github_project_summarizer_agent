from typing import Any
import requests
import os
from urllib.parse import urlparse


def get_user_repos(username):
    url = f"{os.getenv('api_github_endpoint')}/users/{username}/repos"
    response = requests.get(
        url,
        headers={
            "Accept": os.getenv("github_headers_json"),  # <-- raw content
            "Authorization": f'Bearer {os.getenv("GITHUB_API_KEY")}',
        },
    )
    if response.status_code == 200:
        return response
    else:
        return []


def extract_fields_from_n_recent_repos(
    repos: list[dict[str, Any]], top_n: int = 2
) -> list[dict[str, Any]]:
    """
    Extracts key fields from a list of repos.

    Args:
        repo: A list of dictionaries, it is the output of api call to github to get repos
        top_n: How many most recently updated repos to return.

    Returns:
        A list of the top N most recently updated repo dicts with selected keys.

    """
    sorted_repos = sorted(
        repos, key=lambda repo: repo.get("updated_at", ""), reverse=True
    )

    top_n_repos = sorted_repos[:top_n]

    filtered_repo = []
    for repo in top_n_repos:

        username = repo.get("owner", {}).get("login")
        repo_name = repo.get("name")
        readme_api_url = (
            f"{os.getenv('api_github_endpoint')}/repos/{username}/{repo_name}/readme"
        )

        readme_response = requests.get(
            readme_api_url,
            headers={
                "Accept": os.getenv("github_headers_raw"),  # <-- raw content
                "Authorization": f'Bearer {os.getenv("GITHUB_API_KEY")}',
            },
        )
        if readme_response.status_code == 200:
            readme_data = readme_response.text
        else:
            readme_data = "(No Readme found)"

        filtered_repo.append(
            {
                "Repository name": repo.get("name"),
                "Languages used": repo.get("language"),
                "URL": repo.get("html_url"),
                "README": readme_data[:3000],
                "Is Forked": "Yes" if repo.get("fork") else "No",
                "Stars": repo.get("stargazers_count", 0),
                "Open Issues": repo.get("open_issues_count", 0),
                "Last Updated": repo.get("updated_at", "")[:10],
            }
        )

    return filtered_repo


def is_valid_url(url: str) -> bool:
    """
    Checks if the url is valid.

    Args:
        url in str
    Returns: True or False
    """
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])
