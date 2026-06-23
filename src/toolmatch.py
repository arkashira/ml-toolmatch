import json
from dataclasses import dataclass
from typing import List

@dataclass
class Tool:
    name: str
    description: str
    category: str
    roi_score: float
    reviews: List[str]
    pricing_info: str

class ToolMatch:
    def __init__(self):
        self.tools = []

    def add_tool(self, tool: Tool):
        self.tools.append(tool)

    def filter_by_category(self, category: str):
        return [tool for tool in self.tools if tool.category == category]

    def sort_by_roi(self):
        return sorted(self.tools, key=lambda tool: tool.roi_score, reverse=True)

    def get_tool_details(self, tool_name: str):
        for tool in self.tools:
            if tool.name == tool_name:
                return tool
        return None

    def save_to_json(self, filename: str):
        data = []
        for tool in self.tools:
            data.append({
                'name': tool.name,
                'description': tool.description,
                'category': tool.category,
                'roi_score': tool.roi_score,
                'reviews': tool.reviews,
                'pricing_info': tool.pricing_info
            })
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_from_json(self, filename: str):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            for tool_data in data:
                tool = Tool(
                    name=tool_data['name'],
                    description=tool_data['description'],
                    category=tool_data['category'],
                    roi_score=tool_data['roi_score'],
                    reviews=tool_data['reviews'],
                    pricing_info=tool_data['pricing_info']
                )
                self.add_tool(tool)
        except FileNotFoundError:
            pass
