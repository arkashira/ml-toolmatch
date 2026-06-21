import pytest
from toolmatch import ToolMatch, Tool

def test_sync_with_pgvector():
    knowledge_base = {}
    pgvector_data = [
        {'name': 'tool1', 'validation_data': {'key1': 'value1'}},
        {'name': 'tool2', 'validation_data': {'key2': 'value2'}}
    ]
    tool_match = ToolMatch(knowledge_base)
    tool_match.sync_with_pgvector(pgvector_data)
    assert len(tool_match.knowledge_base) == 2
    assert tool_match.knowledge_base['tool1'].name == 'tool1'
    assert tool_match.knowledge_base['tool1'].validation_data == {'key1': 'value1'}

def test_import_historical_tool_validation_data():
    knowledge_base = {}
    historical_data = [
        {'name': 'tool1', 'validation_data': {'key1': 'value1'}},
        {'name': 'tool2', 'validation_data': {'key2': 'value2'}}
    ]
    tool_match = ToolMatch(knowledge_base)
    tool_match.import_historical_tool_validation_data(historical_data)
    assert len(tool_match.knowledge_base) == 2
    assert tool_match.knowledge_base['tool1'].name == 'tool1'
    assert tool_match.knowledge_base['tool1'].validation_data == {'key1': 'value1'}

def test_get_tool():
    knowledge_base = {
        'tool1': Tool('tool1', {'key1': 'value1'})
    }
    tool_match = ToolMatch(knowledge_base)
    tool = tool_match.get_tool('tool1')
    assert tool.name == 'tool1'
    assert tool.validation_data == {'key1': 'value1'}

def test_update_tool():
    knowledge_base = {
        'tool1': Tool('tool1', {'key1': 'value1'})
    }
    tool_match = ToolMatch(knowledge_base)
    new_validation_data = {'key2': 'value2'}
    tool_match.update_tool('tool1', new_validation_data)
    assert tool_match.knowledge_base['tool1'].validation_data == {'key2': 'value2'}

def test_update_tool_not_found():
    knowledge_base = {}
    tool_match = ToolMatch(knowledge_base)
    with pytest.raises(ValueError):
        tool_match.update_tool('tool1', {'key1': 'value1'})
