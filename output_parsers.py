from typing import List, Dict, Any
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class Summary(BaseModel):
    summary: str = Field(description="summary")
    facts: List[str] = Field(description="facts about the repo")

    def to_dict(self) -> Dict[str, Any]:
        return {"summary": self.summary, "facts":self.facts}
    
class GitHubProjectsOutput(BaseModel):
    projects: List[Summary]

summary_parser = PydanticOutputParser(pydantic_object=GitHubProjectsOutput)


