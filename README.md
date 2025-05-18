# GitHub Project Summarizer with Agents

## Overview

**GitHub Project Summarizer** is an intelligent, agent-powered tool that automates the process of summarizing a GitHub user's top repositories. Given a person's name, the system uses tools (such as GitHub search) to locate the individual's GitHub profile. It extracts relevant URLs from the search results and intelligently identifies the correct profile. Once the profile is found, the system retrieves metadata from the user's top two repositories and generates concise summaries using a large language model (LLM).

## Features

- **Profile Discovery**: Automatically searches for a GitHub profile based on a person's name.
- **Username Extraction**: Extracts the GitHub username from the profile URL for use in API requests.
- **Repository Analysis**: Gathers metadata and README content from the top two repositories.
- **LLM Summarization**: Uses a structured prompt to pass the collected information to an LLM, which generates:
  - Project details such as:
    - Creation date
    - Last updated date
    - Fork status
    - Repository URL
    - Other relevant metadata

## Prompt Used for LLM

```text
Given the information {information} about GitHub projects, I want you to:
    1. Provide a short summary of each project, including the name of the repository.
    2. List two facts per project, such as the creation date, last update, whether it's a fork, the URL, or any other relevant details in a concise manner.