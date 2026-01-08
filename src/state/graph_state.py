from typing import TypedDict, List
from pydantic import BaseModel
from typing import Literal


class AgentState(TypedDict):
    query: str
    context: str
    validation: Literal["yes", "no"]
    answer: str

class ValidationResponse(BaseModel):
    validation: Literal["yes", "no"]
