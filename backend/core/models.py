from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class StoryOptionLLM(BaseModel):
  text: str = Field(description="The text of the option presented to the user")
  nextNode: Dict[str, Any] = Field(description="The next node in the story")

class StoryNodeLLM(BaseModel):
  content: str = Field(description="The content of the story node")
  isEnding: bool = Field(description="Whether this node is an ending")
  isWinningEnding: bool = Field(description="Whether this ending is a winning ending")
  options: Optional[List[StoryOptionLLM]] = Field(default=None, description="The options available at this node")

class StoryLLMResponse(BaseModel):
  title: str = Field(description="The title of the story")
  rootNode: StoryNodeLLM = Field(description="The root node of the story")