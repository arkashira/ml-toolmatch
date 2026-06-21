import json
from dataclasses import dataclass
from enum import Enum
from typing import List

class RiskFactor(Enum):
    TECHNICAL_DEBT = 1
    FINANCIAL_STABILITY = 2
    OPERATIONAL_COMPLEXITY = 3
    MARKET_VOLATILITY = 4
    REGULATORY_COMPLIANCE = 5

@dataclass
class RiskAssessment:
    build_option: bool
    risk_factors: List[RiskFactor]
    risk_scores: List[float]

    def calculate_risk_matrix(self):
        risk_matrix = {}
        for factor, score in zip(self.risk_factors, self.risk_scores):
            risk_matrix[factor.name] = score
        return risk_matrix

    def visualize_risk_vs_reward(self):
        # Simplified visualization for demonstration purposes
        risk_scores = [score for score in self.risk_scores]
        reward_scores = [round(1 - score, 1) for score in self.risk_scores] # Round to 1 decimal place
        return risk_scores, reward_scores

def generate_risk_assessment(build_option: bool, risk_factors: List[RiskFactor], risk_scores: List[float]) -> RiskAssessment:
    return RiskAssessment(build_option, risk_factors, risk_scores)
