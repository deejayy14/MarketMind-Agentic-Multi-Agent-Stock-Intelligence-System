import sys
import os

sys.path.append(os.path.abspath("src"))

import gradio as gr
from src.stock_picker.crew import StockPicker

def run_stock_picker(sector):
    try:
        result = StockPicker().crew().kickoff(inputs={"sector": sector})
        return result.raw
    except Exception as e:
        return f"Error: {str(e)}"

demo = gr.Interface(
    fn=run_stock_picker,
    inputs=gr.Textbox(label="Enter sector (e.g., Technology)"),
    outputs=gr.Markdown(label="Investment Decision"),
    title="📈 Agentic Multi-Agent Stock Picker",
    description="CrewAI-based system that analyzes trending companies and selects the best investment."
)

demo.launch(inbrowser=True)