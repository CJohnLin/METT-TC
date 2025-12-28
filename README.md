🧠 AI 輔助 MDMP 任務分析系統（METT-TC）

AI-assisted, Human-in-the-loop Decision Support System for MDMP Mission Analysis

本專案實作一套 AI 輔助之 MDMP（Military Decision-Making Process）任務分析系統，聚焦於 METT-TC 架構中的 Mission 與 Enemy 分析，並引入 Human-in-the-loop（人機協作）設計，在保留指揮官最終決策權的前提下，提升任務分析效率與結構化程度。

本系統以 決策輔助（Decision Support） 為核心定位，不進行自動化決策，符合軍事 AI 使用原則。

📌 專案目標（Objectives）

將傳統高度仰賴人工經驗的 METT-TC 任務分析流程結構化

提供 敵情行動方案（Enemy COA）之機率化初始評估

設計 Human-in-the-loop 機制，使參謀可即時修正 AI 建議

建立一套 可展示、可驗證、可擴充 的 MDMP 決策輔助系統原型

🧭 系統定位與設計原則
系統定位

適用於 MDMP Step 2：Mission Analysis

屬於 Decision Support System（DSS）

AI 為輔助角色，非自動決策

設計原則

Human-in-the-loop（人機協作）

AI 非單點失效（具備規則式備援）

結果可解釋、可比較、可重現

不需任務資料集或模型預訓練

🧩 系統架構概述
作戰情境文字輸入
        ↓
Mission Analyzer（任務分析）
Enemy COA Analyzer（敵情行動方案）
        ↓
AI 初始機率評估（Baseline）
        ↓
Human-in-the-loop 人工修正
        ↓
結構化 METT-TC 輸出與視覺化比較

🔍 功能模組說明
1️⃣ Mission Analysis（M）

輸入：自然語言作戰情境

輸出（結構化）：

Specified Tasks（特定行動）

Implied Tasks（推斷行動）

Constraints（限制條件）

Essential Task（關鍵任務）

2️⃣ Enemy COA Analysis（E）

預設敵軍行動方案：

Defensive

Counterattack

Withdrawal

輸出：

各 COA 發生機率

Most Likely COA

Most Dangerous COA（Doctrine-based）

3️⃣ Human-in-the-loop（人機協作）

AI 提供初始機率（Baseline）

參謀可透過滑桿即時調整

系統自動正規化並重新計算結果

提供 AI vs Human 並列比較圖表

📊 視覺化與比較

使用 並列柱狀圖（Side-by-side Bar Chart）

清楚比較：

AI Baseline

Human-adjusted

圖表採用英文標示，避免跨平台字型問題

適用於：

PPT 簡報

論文 Figure

實施報告截圖

🛠️ 技術實作

Python 3.x

Streamlit（互動式介面）

Matplotlib（視覺化）

Rule-based + Probabilistic Reasoning

模組化設計（可替換 AI / 規則）

▶️ 執行方式
1️⃣ 安裝套件
pip install -r requirements.txt

2️⃣ 啟動系統
streamlit run streamlit_app.py


瀏覽器將自動開啟：

http://localhost:8501

📂 專案結構（簡化）
METT-TC/
├─ core/
│  ├─ mission_analyzer.py
│  ├─ enemy_analyzer.py
│  └─ schema.py
├─ streamlit_app.py
├─ app.py
├─ requirements.txt
└─ README.md

📚 研究與應用價值

✔ AI 輔助 MDMP 任務分析之可行性驗證

✔ Human-in-the-loop 決策支援系統設計範例

✔ 可作為：

課程實作專案

實施報告

論文前期系統原型

軍事決策輔助展示

🔮 未來擴充方向（Future Work）

Terrain / OCOKA 分析模組

Troops & Time（兵力與時間）評估

COA Comparison Matrix（支援 MDMP Step 3/4）

差異量化指標（Δ AI vs Human）

決策歷程紀錄與匯出（實驗用）

⚠️ 免責聲明（Disclaimer）

本專案為 研究與教學用途之系統原型，
不構成任何實際軍事指揮或作戰建議。

👤 作者

林佳宏（Chiahung “John” Lin）
AI-assisted Military Decision Support Research
