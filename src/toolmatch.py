import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class ToolMatch:
    team_size: int
    tool_pricing: Dict[str, float]
    development_hours: int
    technical_complexity: int
    maintenance_overhead: int
    integration_challenges: int

    def calculate_cost(self):
        total_cost = 0
        for tool, price in self.tool_pricing.items():
            total_cost += price * self.team_size * self.development_hours
        return total_cost

    def calculate_risk(self):
        risk_score = (self.technical_complexity + self.maintenance_overhead + self.integration_challenges) / 3
        return risk_score

    def get_build_buy_options(self):
        build_option = {
            "cost": self.calculate_cost(),
            "risk_score": self.calculate_risk()
        }
        buy_option = {
            "cost": self.calculate_cost() * 0.8,  # assuming 20% cost reduction for buy option
            "risk_score": self.calculate_risk() * 0.8  # assuming 20% risk reduction for buy option
        }
        return build_option, buy_option

def main():
    tool_match = ToolMatch(
        team_size=10,
        tool_pricing={"tool1": 100, "tool2": 200},
        development_hours=100,
        technical_complexity=5,
        maintenance_overhead=3,
        integration_challenges=4
    )
    build_option, buy_option = tool_match.get_build_buy_options()
    print(json.dumps({"build": build_option, "buy": buy_option}, indent=4))

if __name__ == "__main__":
    main()
