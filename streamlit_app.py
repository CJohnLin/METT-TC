import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from core.mission_analyzer import analyze_mission
from core.enemy_analyzer import analyze_enemy

# ===============================
# Page Config
# ===============================
st.set_page_config(
    page_title="MDMP / METT-TC AI Decision Support",
    layout="wide"
)

# ===============================
# Title
# ===============================
st.title("MDMP Mission Analysis (METT-TC)")
st.markdown("**AI-assisted, Human-in-the-loop Decision Support System**")

# ===============================
# Scenario Input
# ===============================
st.subheader("Operational Scenario Input")

scenario = st.text_area(
    "Enter operational situation / mission context:",
    height=220,
    value="""Friendly forces will conduct offensive operations to seize Objective ALPHA
in order to deny enemy use of key terrain.

Enemy forces consist of a mechanized infantry battalion defending in sector
with limited artillery support.

Civilian population remains in the area."""
)

# ===============================
# Run Analysis (ONE-TIME trigger)
# ===============================
if st.button("Run METT-TC Analysis"):
    # Run analysis once
    st.session_state.mission = analyze_mission(scenario)
    st.session_state.enemy = analyze_enemy(scenario)

    # Freeze AI baseline probabilities
    st.session_state.ai_baseline = {
        "Defensive": st.session_state.enemy.all_coas["defensive"].probability,
        "Counterattack": st.session_state.enemy.all_coas["counterattack"].probability,
        "Withdrawal": st.session_state.enemy.all_coas["withdrawal"].probability,
    }

    # Initialize human sliders (only once per analysis)
    st.session_state.human_defensive = st.session_state.ai_baseline["Defensive"]
    st.session_state.human_counterattack = st.session_state.ai_baseline["Counterattack"]
    st.session_state.human_withdrawal = st.session_state.ai_baseline["Withdrawal"]

# ===============================
# Display Results
# ===============================
if "mission" in st.session_state and "enemy" in st.session_state:

    mission = st.session_state.mission
    enemy = st.session_state.enemy
    ai_baseline = st.session_state.ai_baseline

    col1, col2 = st.columns(2)

    # ===========================
    # Mission Analysis (M)
    # ===========================
    with col1:
        st.subheader("Mission Analysis (M)")

        st.markdown("**Specified Tasks**")
        st.write(mission.specified_tasks)

        st.markdown("**Implied Tasks**")
        st.write(mission.implied_tasks)

        st.markdown("**Constraints**")
        st.write(mission.constraints)

        st.markdown("**Essential Task**")
        st.success(mission.essential_task)

    # ===========================
    # Enemy COA + Human-in-the-loop
    # ===========================
    with col2:
        st.subheader("Enemy COA Assessment (E)")

        # ---- AI Baseline ----
        st.markdown("### AI Baseline Assessment")
        st.write(f"**Most Likely COA (AI):** {max(ai_baseline, key=ai_baseline.get)}")
        st.write("**Most Dangerous COA (AI):** Counterattack (doctrine-based)")

        st.markdown("---")

        # ---- Human-in-the-loop ----
        st.markdown("### Human-in-the-loop Adjustment")

        st.slider(
            "Defensive",
            0.0, 1.0, step=0.05,
            key="human_defensive"
        )

        st.slider(
            "Counterattack",
            0.0, 1.0, step=0.05,
            key="human_counterattack"
        )

        st.slider(
            "Withdrawal",
            0.0, 1.0, step=0.05,
            key="human_withdrawal"
        )

        total = (
            st.session_state.human_defensive
            + st.session_state.human_counterattack
            + st.session_state.human_withdrawal
        )

        if total == 0:
            st.error("Total probability must be greater than 0.")
        else:
            # Normalized human-adjusted probabilities
            human_probs = {
                "Defensive": st.session_state.human_defensive / total,
                "Counterattack": st.session_state.human_counterattack / total,
                "Withdrawal": st.session_state.human_withdrawal / total,
            }

            st.markdown("### Human-adjusted Assessment")
            st.success(
                f"**Most Likely COA (Human):** {max(human_probs, key=human_probs.get)}"
            )
            st.warning(
                "**Most Dangerous COA (Human):** Counterattack (doctrine-based)"
            )

            # ===============================
            # AI vs Human Probability Comparison
            # ===============================
            st.markdown("### AI vs Human-adjusted Probability Comparison")

            labels = ["Defensive", "Counterattack", "Withdrawal"]
            ai_values = [ai_baseline[k] for k in labels]
            human_values = [human_probs[k] for k in labels]

            x = np.arange(len(labels))
            width = 0.35

            fig, ax = plt.subplots()

            ax.bar(x - width / 2, ai_values, width, label="AI Baseline")
            ax.bar(x + width / 2, human_values, width, label="Human-adjusted")

            ax.set_ylabel("Probability")
            ax.set_ylim(0, 1)
            ax.set_xticks(x)
            ax.set_xticklabels(labels)
            ax.legend()

            st.pyplot(fig)

# ===============================
# Footer
# ===============================
st.markdown("---")
st.caption(
    "Human-in-the-loop decision support | AI-assisted MDMP | Non-automated command authority"
)
