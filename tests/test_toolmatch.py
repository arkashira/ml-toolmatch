import json
from toolmatch import Tool, ToolMatch

def test_tool_creation():
    tool = Tool(
        name='Test Tool',
        description='This is a test tool',
        category='Data Preprocessing',
        roi_score=0.8,
        reviews=['Great tool!', 'Easy to use'],
        pricing_info='Free'
    )
    assert tool.name == 'Test Tool'
    assert tool.description == 'This is a test tool'
    assert tool.category == 'Data Preprocessing'
    assert tool.roi_score == 0.8
    assert tool.reviews == ['Great tool!', 'Easy to use']
    assert tool.pricing_info == 'Free'

def test_toolmatch_add_tool():
    toolmatch = ToolMatch()
    tool = Tool(
        name='Test Tool',
        description='This is a test tool',
        category='Data Preprocessing',
        roi_score=0.8,
        reviews=['Great tool!', 'Easy to use'],
        pricing_info='Free'
    )
    toolmatch.add_tool(tool)
    assert len(toolmatch.tools) == 1
    assert toolmatch.tools[0].name == 'Test Tool'

def test_toolmatch_filter_by_category():
    toolmatch = ToolMatch()
    tool1 = Tool(
        name='Test Tool 1',
        description='This is a test tool',
        category='Data Preprocessing',
        roi_score=0.8,
        reviews=['Great tool!', 'Easy to use'],
        pricing_info='Free'
    )
    tool2 = Tool(
        name='Test Tool 2',
        description='This is another test tool',
        category='Model Training',
        roi_score=0.9,
        reviews=['Excellent tool!', 'Hard to use'],
        pricing_info='Paid'
    )
    toolmatch.add_tool(tool1)
    toolmatch.add_tool(tool2)
    filtered_tools = toolmatch.filter_by_category('Data Preprocessing')
    assert len(filtered_tools) == 1
    assert filtered_tools[0].name == 'Test Tool 1'

def test_toolmatch_sort_by_roi():
    toolmatch = ToolMatch()
    tool1 = Tool(
        name='Test Tool 1',
        description='This is a test tool',
        category='Data Preprocessing',
        roi_score=0.8,
        reviews=['Great tool!', 'Easy to use'],
        pricing_info='Free'
    )
    tool2 = Tool(
        name='Test Tool 2',
        description='This is another test tool',
        category='Model Training',
        roi_score=0.9,
        reviews=['Excellent tool!', 'Hard to use'],
        pricing_info='Paid'
    )
    toolmatch.add_tool(tool1)
    toolmatch.add_tool(tool2)
    sorted_tools = toolmatch.sort_by_roi()
    assert len(sorted_tools) == 2
    assert sorted_tools[0].name == 'Test Tool 2'
    assert sorted_tools[1].name == 'Test Tool 1'

def test_toolmatch_get_tool_details():
    toolmatch = ToolMatch()
    tool = Tool(
        name='Test Tool',
        description='This is a test tool',
        category='Data Preprocessing',
        roi_score=0.8,
        reviews=['Great tool!', 'Easy to use'],
        pricing_info='Free'
    )
    toolmatch.add_tool(tool)
    tool_details = toolmatch.get_tool_details('Test Tool')
    assert tool_details.name == 'Test Tool'
    assert tool_details.description == 'This is a test tool'
    assert tool_details.category == 'Data Preprocessing'
    assert tool_details.roi_score == 0.8
    assert tool_details.reviews == ['Great tool!', 'Easy to use']
    assert tool_details.pricing_info == 'Free'

def test_toolmatch_save_to_json():
    toolmatch = ToolMatch()
    tool = Tool(
        name='Test Tool',
        description='This is a test tool',
        category='Data Preprocessing',
        roi_score=0.8,
        reviews=['Great tool!', 'Easy to use'],
        pricing_info='Free'
    )
    toolmatch.add_tool(tool)
    toolmatch.save_to_json('tools.json')
    with open('tools.json', 'r') as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]['name'] == 'Test Tool'
    assert data[0]['description'] == 'This is a test tool'
    assert data[0]['category'] == 'Data Preprocessing'
    assert data[0]['roi_score'] == 0.8
    assert data[0]['reviews'] == ['Great tool!', 'Easy to use']
    assert data[0]['pricing_info'] == 'Free'
