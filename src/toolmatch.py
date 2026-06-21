import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Tool:
    name: str
    validation_data: Dict[str, str]

class ToolMatch:
    def __init__(self, knowledge_base: Dict[str, Tool]):
        self.knowledge_base = knowledge_base

    def sync_with_pgvector(self, pgvector_data: List[Dict[str, str]]):
        for tool_data in pgvector_data:
            tool_name = tool_data['name']
            validation_data = tool_data['validation_data']
            self.knowledge_base[tool_name] = Tool(tool_name, validation_data)

    def import_historical_tool_validation_data(self, historical_data: List[Dict[str, str]]):
        for tool_data in historical_data:
            tool_name = tool_data['name']
            validation_data = tool_data['validation_data']
            if tool_name not in self.knowledge_base:
                self.knowledge_base[tool_name] = Tool(tool_name, validation_data)

    def get_tool(self, tool_name: str):
        return self.knowledge_base.get(tool_name)

    def update_tool(self, tool_name: str, new_validation_data: Dict[str, str]):
        if tool_name in self.knowledge_base:
            self.knowledge_base[tool_name].validation_data = new_validation_data
        else:
            raise ValueError("Tool not found in knowledge base")
