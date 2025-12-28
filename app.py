from core.mission_analyzer import analyze_mission
from core.enemy_analyzer import analyze_enemy

scenario = """
Friendly forces will conduct offensive operations to seize Objective ALPHA
in order to deny enemy use of key terrain.

Enemy forces consist of a mechanized infantry battalion defending in sector
with limited artillery support.
"""

mission = analyze_mission(scenario)
enemy = analyze_enemy(scenario)

print("=== Mission Analysis ===")
print(mission.model_dump_json(indent=2))

print("\n=== Enemy Assessment (Probabilistic) ===")
print(enemy.model_dump_json(indent=2))
