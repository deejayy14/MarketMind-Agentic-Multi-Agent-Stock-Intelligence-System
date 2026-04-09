# 📈 MarketMind: Agentic Multi-Agent Stock Intelligence System

An **agentic AI system** that autonomously discovers trending companies, conducts real-time financial research, and selects the best investment opportunity using a coordinated multi-agent workflow.

---

## 👉🏾 LIVE DEMO  :  https://huggingface.co/spaces/deejay14/MarketMind-Stock_Intelligence_System

---

## 🚀 Key Highlights

* 🧠 **Agentic AI Workflow** — end-to-end autonomous decision-making
* 🤖 **Multi-Agent Orchestration (CrewAI)** — specialized agents collaborating under a manager
* 🌐 **Real-Time Web Search** — grounded in latest market data (not static LLM knowledge)
* 🧩 **YAML-Driven Architecture** — modular, configurable agent and task design
* 🧠 **Memory Systems** — long-term, short-term, and entity memory for contextual reasoning
* 🔔 **Actionable Output** — sends investment decision via notification + detailed report

---

## 🧠 Key Learnings

* Designing agent workflows using **CrewAI hierarchical processes**
* Forcing **tool-based reasoning for real-time intelligence**
* Managing **memory in agent systems (LTM, STM, Entity Memory)**
* Structuring AI systems using **YAML-driven configurations**

---

## 🧩 Architecture

```
User Input (Sector)
        ↓
Manager Agent (delegation)
        ↓
Trending Company Finder  →  (Real-time news via search)
        ↓
Financial Researcher     →  (Deep analysis of companies)
        ↓
Stock Picker             →  (Final decision + notification)
        ↓
Structured Output (Markdown Report)
```

---

## ⚙️ Tech Stack

* **CrewAI** — multi-agent orchestration
* **OpenAI (GPT-4o-mini)** — reasoning engine
* **Serper API** — real-time web search
* **Gradio** — interactive UI
* **Pydantic** — structured outputs
* **SQLite + RAG Storage** — memory systems

---

## 🧠 How It Works

1. **Discovers trending companies** using real-time news search
2. **Performs deep financial research** on each company
3. **Evaluates investment potential** using structured reasoning
4. **Selects the best stock** and explains the decision
5. **Stores context in memory** for improved future reasoning

---

## 🌐 Deployment

Deployed on **Hugging Face Spaces** using a Gradio interface.

---

## 📌 Why I chose to do this Project

* Demonstrates **true agentic system design** 
* Implements **multi-agent collaboration with delegation**
* Uses **real-time data grounding via search tools**
* Integrates **memory for context-aware reasoning**
* Built with **modularity and scalability in mind**
