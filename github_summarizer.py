from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from typing import List

from src.agents.github_lookup_agent import lookup
from src.utils.common import (
    get_user_repos,
    extract_fields_from_n_recent_repos,
    is_valid_url,
)

from pprint import pformat
from dotenv import load_dotenv
from pprint import pprint
import json

from urllib.parse import urlparse
from output_parsers import summary_parser, Summary


def github_summarizer(name: str) -> List[Summary]:
    top_n_repo_data = {}

    github_profile_url = lookup(name=name)
    print(github_profile_url)

    if is_valid_url(github_profile_url):
        username = github_profile_url.rstrip("/").split("/")[-1]
        print(username)

        repos = get_user_repos(username=username).json()
        top_n_repo_data = extract_fields_from_n_recent_repos(repos=repos, top_n=2)


    summary_template = """Given the information {information} about GitHub projects, I want you to:
    1. A short summary of each project with the name of the repo.
    2. two facts such as creation date, last update, whether it's a fork, URL, and other relevant details in a concise manner.
    \n{format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template, partial_variables={"format_instructions": summary_parser.get_format_instructions()}

    )

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    chain = summary_prompt_template | llm | summary_parser

    res:Summary = chain.invoke(input={"information": pformat(top_n_repo_data)})

    print("Response Content:\n")
    return res


if __name__ == "__main__":
    load_dotenv()

    print("GITHUB Projects Summarizer")

    res = github_summarizer(name="Sanket Panaskar")
    print(res)
