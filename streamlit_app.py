import streamlit as st
import matplotlib.pyplot as plt

from core.mission_analyzer import analyze_mission
from core.enemy_analyzer import analyze_enemy

st.set_page_config(
    page_title="MDMP / METT-TC AI 參謀輔助系統",
    layout="wide"
)

# === 標題 ===
st.title("MDMP 第二步驟：任務分析（METT-TC）")
st.markdown("**AI 輔助決策系統（具備規則式備援機制）**")

# === 輸入區 ===
st.subheader("作戰情境輸入（Operational Scenario）")

scenario = st.text_area(
    "請輸入作戰情境、任務背景或敵情概述：",
    height=220,
    value="""我方部隊奉命對目標 ALPHA 發起攻勢，
以奪控關鍵地形並阻止敵軍使用。

敵軍為一個機械化步兵營，
目前於責任地區內採取防禦部署，
並具有限度砲兵支援能力。

作戰區域內仍有平民活動，
交戰規則要求避免造成平民傷亡。"""
)

if st.button("執行 METT-TC 分析"):
    # === 分析 ===
    mission = analyze_mission(scenario)
    enemy = analyze_enemy(scenario)

    col1, col2 = st.columns(2)

    # ===== 任務分析（M）=====
    with col1:
        st.subheader("任務分析（Mission）")

        st.markdown("**特定行動（Specified Tasks）**")
        st.write(mission.specified_tasks)

        st.markdown("**推斷行動（Implied Tasks）**")
        st.write(mission.implied_tasks)

        st.markdown("**限制（Constraints）**")
        st.write(mission.constraints)

        st.markdown("**關鍵行動（Essential Tasks）**")
        st.success(mission.essential_task)
    # ===== 敵情評估（E）=====
    with col2:
        st.subheader("敵情行動方案評估（Enemy COA）")

        if enemy is None:
            st.error("敵情分析未產生結果，請確認 Enemy Analyzer。")
        else:
            st.markdown("**最可能行動方案（Most Likely COA）**")
            st.write(enemy.most_likely.description)
            st.write(f"發生機率：{enemy.most_likely.probability}")

            st.markdown("**最危險行動方案（Most Dangerous COA）**")
            st.write(enemy.most_dangerous.description)
            st.write(f"發生機率：{enemy.most_dangerous.probability}")

            st.markdown("### 敵軍行動方案機率分布")

            labels = []
            values = []

            for key, coa in enemy.all_coas.items():
                labels.append(key)
                values.append(coa.probability)

            if len(labels) == 0:
                st.warning("未產生任何 COA 機率資料")
            else:
                fig, ax = plt.subplots()
                ax.bar(labels, values)
                ax.set_ylabel("機率")
                ax.set_ylim(0, 1)
                st.pyplot(fig)

