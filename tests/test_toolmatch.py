import pytest
from toolmatch import automated_risk_assessment_and_cost_modeling

def test_automated_risk_assessment_and_cost_modeling():
    build_option = {
        'technical_complexity': 0.5,
        'maintenance_overhead': 0.3,
        'integration_challenges': 0.2,
        'team_size': 10,
        'tool_pricing': 100.0,
        'development_hours': 100
    }
    buy_option = {
        'technical_complexity': 0.4,
        'maintenance_overhead': 0.2,
        'integration_challenges': 0.1,
        'team_size': 5,
        'tool_pricing': 50.0,
        'development_hours': 50
    }
    result = automated_risk_assessment_and_cost_modeling(build_option, buy_option)
    assert result['build']['risk_score'] == 0.333333
    assert result['build']['cost'] == 100000.0
    assert result['buy']['risk_score'] == 0.233333
    assert result['buy']['cost'] == 12500.0

def test_automated_risk_assessment_and_cost_modeling_edge_case():
    build_option = {
        'technical_complexity': 0.0,
        'maintenance_overhead': 0.0,
        'integration_challenges': 0.0,
        'team_size': 0,
        'tool_pricing': 0.0,
        'development_hours': 0
    }
    buy_option = {
        'technical_complexity': 0.0,
        'maintenance_overhead': 0.0,
        'integration_challenges': 0.0,
        'team_size': 0,
        'tool_pricing': 0.0,
        'development_hours': 0
    }
    result = automated_risk_assessment_and_cost_modeling(build_option, buy_option)
    assert result['build']['risk_score'] == 0.0
    assert result['build']['cost'] == 0.0
    assert result['buy']['risk_score'] == 0.0
    assert result['buy']['cost'] == 0.0
