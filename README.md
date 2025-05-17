# GitHub Project Summarizer with Agents

## Overview

**GitHub Project Summarizer** is an intelligent tool powered by agents that automates the process of summarizing the top repositories from a GitHub user's profile. Given a person's name, the system discovers their GitHub profile, extracts relevant data from their top two repositories, and generates concise summaries using a language model (LLM).

## Features

- 🔍 **Profile Discovery**: Automatically searches for a GitHub profile URL based on a person's name.
- 👤 **Username Extraction**: Extracts the GitHub username from the profile URL to make API requests.
- 📦 **Repository Analysis**: Retrieves metadata and README contents for the top two repositories.
- 🤖 **LLM Summarization**: Passes the collected information to an LLM with a structured prompt to generate:
  - A short summary of each project based on the README.
  - Project details such as:
    - Creation date
    - Last updated date
    - Fork status
    - Other relevant metadata

## Prompt Used for LLM

```text
Given the information {information} about the GitHub projects, I want you to create:
  1. A short summary of each project by reading the README contents
  2. When it was created, last updated and if it was forked, and other details from the information passed
