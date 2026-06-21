import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class RiskAssessment:
    technical_complexity: float
    maintenance_overhead: float
    integration_challenges: float

    def calculate_risk_score(self) -> float:
        return (self.technical_complexity + self.maintenance_overhead + self.integration_challenges) / 3

@dataclass
class CostModel:
    team_size: int
    tool_pricing: float
    development_hours: int

    def calculate_cost(self) -> float:
        return self.team_size * self.tool_pricing * self.development_hours

def automated_risk_assessment_and_cost_modeling(build_option: Dict, buy_option: Dict) -> Dict:
    build_risk_assessment = RiskAssessment(
        technical_complexity=build_option['technical_complexity'],
        maintenance_overhead=build_option['maintenance_overhead'],
        integration_challenges=build_option['integration_challenges']
    )
    build_cost_model = CostModel(
        team_size=build_option['team_size'],
        tool_pricing=build_option['tool_pricing'],
        development_hours=build_option['development_hours']
    )
    buy_risk_assessment = RiskAssessment(
        technical_complexity=buy_option['technical_complexity'],
        maintenance_overhead=buy_option['maintenance_overhead'],
        integration_challenges=buy_option['integration_challenges']
    )
    buy_cost_model = CostModel(
        team_size=buy_option['team_size'],
        tool_pricing=buy_option['tool_pricing'],
        development_hours=buy_option['development_hours']
    )
    build_risk_score = build_risk_assessment.calculate_risk_score()
    build_cost = build_cost_model.calculate_cost()
    buy_risk_score = buy_risk_assessment.calculate_risk_score()
    buy_cost = buy_cost_model.calculate_cost()
    return {
        'build': {
            'risk_score': round(build_risk_score, 6),
            'cost': build_cost
        },
        'buy': {
            'risk_score': round(buy_risk_score, 6),
            'cost': buy_cost
        }
    }
