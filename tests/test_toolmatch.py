from toolmatch import ToolMatch

def test_calculate_cost():
    tool_match = ToolMatch(
        team_size=10,
        tool_pricing={"tool1": 100, "tool2": 200},
        development_hours=100,
        technical_complexity=5,
        maintenance_overhead=3,
        integration_challenges=4
    )
    assert tool_match.calculate_cost() == 300000

def test_calculate_risk():
    tool_match = ToolMatch(
        team_size=10,
        tool_pricing={"tool1": 100, "tool2": 200},
        development_hours=100,
        technical_complexity=5,
        maintenance_overhead=3,
        integration_challenges=4
    )
    assert tool_match.calculate_risk() == 4

def test_get_build_buy_options():
    tool_match = ToolMatch(
        team_size=10,
        tool_pricing={"tool1": 100, "tool2": 200},
        development_hours=100,
        technical_complexity=5,
        maintenance_overhead=3,
        integration_challenges=4
    )
    build_option, buy_option = tool_match.get_build_buy_options()
    assert build_option["cost"] == 300000
    assert build_option["risk_score"] == 4
    assert buy_option["cost"] == 240000
    assert buy_option["risk_score"] == 3.2

def test_edge_case_zero_team_size():
    tool_match = ToolMatch(
        team_size=0,
        tool_pricing={"tool1": 100, "tool2": 200},
        development_hours=100,
        technical_complexity=5,
        maintenance_overhead=3,
        integration_challenges=4
    )
    assert tool_match.calculate_cost() == 0
    assert tool_match.calculate_risk() == 4
