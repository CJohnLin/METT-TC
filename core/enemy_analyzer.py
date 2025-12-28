from core.schema import EnemyAssessment, EnemyCOAProb

def analyze_enemy(text: str) -> EnemyAssessment:
    """
    Rule-based probabilistic Enemy COA assessment
    """

    # === 基本規則（你之後可以擴充） ===
    indicators = {
        "defensive": 0.5,
        "counterattack": 0.3,
        "withdrawal": 0.2
    }

    # 正規化（確保加總 = 1）
    total = sum(indicators.values())
    for k in indicators:
        indicators[k] /= total

    coas = {
        "defensive": EnemyCOAProb(
            description="Enemy maintains defensive posture along main avenue of approach",
            probability=round(indicators["defensive"], 2),
            risk_level="Medium"
        ),
        "counterattack": EnemyCOAProb(
            description="Enemy conducts limited counterattack with reserve forces",
            probability=round(indicators["counterattack"], 2),
            risk_level="High"
        ),
        "withdrawal": EnemyCOAProb(
            description="Enemy conducts phased withdrawal to secondary positions",
            probability=round(indicators["withdrawal"], 2),
            risk_level="Low"
        )
    }

    most_likely = max(coas.values(), key=lambda x: x.probability)
    most_dangerous = max(coas.values(), key=lambda x: x.risk_level == "High")

    return EnemyAssessment(
        most_likely=most_likely,
        most_dangerous=most_dangerous,
        all_coas=coas
    )
