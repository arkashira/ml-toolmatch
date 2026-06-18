import json
from ml_toolmatch import recommend_tools, Tool

def test_recommend_tools():
    configuration = {
        'tools': [
            {'name': 'Tool 1', 'description': 'Description 1', 'required_input': 'input1'},
            {'name': 'Tool 2', 'description': 'Description 2', 'required_input': 'input2'}
        ]
    }
    input_data = {'input1': 'value1', 'input2': 'value2'}
    recommended_tools = recommend_tools(configuration, input_data)
    assert len(recommended_tools) == 2
    assert recommended_tools[0].name == 'Tool 1'
    assert recommended_tools[1].name == 'Tool 2'

def test_recommend_tools_empty_input():
    configuration = {
        'tools': [
            {'name': 'Tool 1', 'description': 'Description 1', 'required_input': 'input1'},
            {'name': 'Tool 2', 'description': 'Description 2', 'required_input': 'input2'}
        ]
    }
    input_data = {}
    recommended_tools = recommend_tools(configuration, input_data)
    assert len(recommended_tools) == 0

def test_recommend_tools_empty_configuration():
    configuration = {'tools': []}
    input_data = {'input1': 'value1', 'input2': 'value2'}
    recommended_tools = recommend_tools(configuration, input_data)
    assert len(recommended_tools) == 0
