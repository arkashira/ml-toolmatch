import pytest
from risk_assessment import RiskAssessment, RiskFactor, generate_risk_assessment

def test_calculate_risk_matrix():
    risk_factors = [RiskFactor.TECHNICAL_DEBT, RiskFactor.FINANCIAL_STABILITY]
    risk_scores = [0.5, 0.8]
    assessment = generate_risk_assessment(True, risk_factors, risk_scores)
    risk_matrix = assessment.calculate_risk_matrix()
    assert risk_matrix["TECHNICAL_DEBT"] == 0.5
    assert risk_matrix["FINANCIAL_STABILITY"] == 0.8

def test_visualize_risk_vs_reward():
    risk_factors = [RiskFactor.TECHNICAL_DEBT, RiskFactor.FINANCIAL_STABILITY]
    risk_scores = [0.5, 0.8]
    assessment = generate_risk_assessment(True, risk_factors, risk_scores)
    risk_scores, reward_scores = assessment.visualize_risk_vs_reward()
    assert risk_scores == [0.5, 0.8]
    assert reward_scores == [0.5, 0.2]

def test_generate_risk_assessment():
    risk_factors = [RiskFactor.TECHNICAL_DEBT, RiskFactor.FINANCIAL_STABILITY]
    risk_scores = [0.5, 0.8]
    assessment = generate_risk_assessment(True, risk_factors, risk_scores)
    assert assessment.build_option
    assert assessment.risk_factors == risk_factors
    assert assessment.risk_scores == risk_scores

def test_edge_case_empty_risk_factors():
    risk_factors = []
    risk_scores = []
    assessment = generate_risk_assessment(True, risk_factors, risk_scores)
    risk_matrix = assessment.calculate_risk_matrix()
    assert risk_matrix == {}
    risk_scores, reward_scores = assessment.visualize_risk_vs_reward()
    assert risk_scores == []
    assert reward_scores == []
