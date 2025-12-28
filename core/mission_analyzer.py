import json
import os
from dotenv import load_dotenv

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

from core.schema import MissionAnalysis

load_dotenv()

def analyze_mission(text: str) -> MissionAnalysis:
    """
    AI-first with rule-based fallback
    """

    # === Fallback result（保證系統不會停） ===
    fallback_result = {
        "specified_tasks": ["Secure Objective ALPHA"],
        "implied_tasks": ["Establish supply route"],
        "constraints": ["Avoid civilian casualties"],
        "essential_task": "Secure Objective ALPHA within specified time"
    }

    # 如果 OpenAI 不可用，直接回退
    if not OPENAI_AVAILABLE or not os.getenv("OPENAI_API_KEY"):
        return MissionAnalysis(**fallback_result)

    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        with open("prompts/mission_prompt.txt", "r", encoding="utf-8") as f:
            system_prompt = f.read()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ],
            temperature=0.2
        )

        data = json.loads(response.choices[0].message.content)
        return MissionAnalysis(**data)

    except Exception as e:
        # === AI 失敗 → fallback ===
        print(f"[WARN] AI unavailable, fallback activated: {e}")
        return MissionAnalysis(**fallback_result)
