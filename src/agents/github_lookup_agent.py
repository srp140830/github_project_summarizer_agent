import os
import sys
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub
from src.tools.tools import search_github_by_name


def lookup(name: str) -> str:
    load_dotenv()
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    template = """ given the full name {name_of_person} I want you to get me a link to their github profile page.
                    Your answer should only contain a url"""

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    tools_for_agent = [
        Tool(
            name="Search github by full name",
            func=search_github_by_name,
            description="useful for when you need to get the github url from full name",
        )
    ]
    react_agent = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_agent)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    github_profile_url = result["output"]
    return github_profile_url
