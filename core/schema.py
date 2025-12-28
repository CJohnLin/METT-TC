from pydantic import BaseModel
from typing import List
from typing import Dict

class EnemyCOAProb(BaseModel):
    description: str
    probability: float
    risk_level: str

class EnemyAssessment(BaseModel):
    most_likely: EnemyCOAProb
    most_dangerous: EnemyCOAProb
    all_coas: Dict[str, EnemyCOAProb]
class MissionAnalysis(BaseModel):
    specified_tasks: List[str]
    implied_tasks: List[str]
    constraints: List[str]
    essential_task: str

class EnemyCOA(BaseModel):
    most_likely: str
    most_dangerous: str
    assumptions: List[str]
