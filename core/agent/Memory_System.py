from mem0 import MemoryClient
try:
    from  ..utils.db import get_profile
except ImportError as e:
    from core.utils.db import get_profile

from langchain_core.tools import StructuredTool
from mem0 import MemoryClient
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional


class Message(BaseModel):
    role: str = Field(description="Role of the message sender (user or assistant)")
    content: str = Field(description="Content of the message")

class AddMemoryInput(BaseModel):
    messages: List[Message] = Field(description="List of messages to add to memory")
    user_id: str = Field(description="ID of the user associated with these messages")
    output_format: str = Field(description="Version format for the output")
    metadata: Optional[Dict[str, Any]] = Field(description="Additional metadata for the messages", default=None)

    class Config:
        json_schema_extra = {
            "examples": [{
                "messages": [
                    {"role": "user", "content": "Hi, I'm Jarvis(Just A Rather Very Intelligent System).How are you?"},
                    {"role": "assistant", "content": "Hello Jarvis! I am Fine doing well."}
                ],
                "user_id": get_profile(),
                "output_format": "v1.1",
            }]
        }
class GetAllMemoryInput(BaseModel):
    version: str = Field(description="Version of the memory to retrieve")
    filters: Dict[str, Any] = Field(description="Filters to apply to the retrieval")
    page: Optional[int] = Field(description="Page number for pagination", default=1)
    page_size: Optional[int] = Field(description="Number of items per page", default=50)

    class Config:
        json_schema_extra = {
            "examples": [{
                "version": "v2",
                "filters": {
                    "AND": [
                        {"user_id": "alex"},
                        {"created_at": {"gte": "2024-07-01", "lte": "2024-07-31"}},
                        {"categories": {"contains": "food_preferences"}}
                    ]
                },
                "page": 1,
                "page_size": 50
            }]
        }

class SearchMemoryInput(BaseModel):
    query: str = Field(description="The search query string")
    filters: Dict[str, Any] = Field(description="Filters to apply to the search")
    version: str = Field(description="Version of the memory to search")

    class Config:
        json_schema_extra = {
            "examples": [{
                "query": "tell me about my allergies?",
                "filters": {
                    "AND": [
                        {"user_id": "alex"},
                        {"created_at": {"gte": "2024-01-01", "lte": "2024-12-31"}}
                    ]
                },
                "version": "v2"
            }]
        }

class MemoHistory:
    def __init__(self):
        super().__init__()
        self.chat_id = get_profile()
        self.client=MemoryClient(
            api_key="m0-ogT58mxbuMlybILMKqo1naT2HNJCsLbXJ6B7WiE9",
        )

    def add_memory(self,messages: List[Message], user_id: str, output_format: str,
                   metadata: Optional[Dict[str, Any]] = None) -> Any:
        """Add messages to memory with associated user ID and metadata."""
        message_dicts = [msg.dict() for msg in messages]
        return self.client.add(message_dicts, user_id=user_id, output_format=output_format, metadata=metadata)

    def search_memory(self,query: str, filters: Dict[str, Any], version: str) -> Any:
        """Search memory with the given query and filters."""
        return self.client.search(query=query, version=version, filters=filters)

    def get_all_memory(self,version: str, filters: Dict[str, Any], page: int = 1, page_size: int = 50) -> Any:
        """Retrieve all memories matching the specified criteria."""
        return self.client.get_all(version=version, filters=filters, page=page, page_size=page_size)

memory=MemoHistory()
add_tool = StructuredTool(
            name="add_memory",
            description="Add new messages to memory with associated metadata",
            func=memory.add_memory,
            args_schema=AddMemoryInput
)
search_tool = StructuredTool(
        name="search_memory",
        description="Search through memories with a query and filters",
        func=memory.search_memory,
        args_schema=SearchMemoryInput
)

get_all_tool = StructuredTool(
    name="get_all_memory",
    description="Retrieve all memories matching specified filters",
    func=memory.get_all_memory,
    args_schema=GetAllMemoryInput
)

def add_memory(user_input,assistant_output):
    add_input = {
        "messages": [
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": assistant_output}
        ],
        "user_id": get_profile(),
        "output_format": "v1.1",
    }
    add_result = add_tool.invoke(add_input)
    return add_result


def search_memory(query):
    search_input = {
        "query": query,
        "filters": {
            "AND": [
                {"user_id": get_profile()}
            ]
        },
        "version": "v2"
    }
    result = search_tool.invoke(search_input)
    return result

