import sys
import types
import ast
import re
import json

# 🚨 DYNAMIC FIX: Python 3.13 Compatibility Core Patches
if 'audioop' not in sys.modules:
    dummy_audioop = types.ModuleType('audioop')
    dummy_audioop.error = Exception
    sys.modules['audioop'] = dummy_audioop

if 'pyaudioop' not in sys.modules:
    dummy_pyaudioop = types.ModuleType('pyaudioop')
    dummy_pyaudioop.error = Exception
    sys.modules['pyaudioop'] = dummy_pyaudioop

try:
    import huggingface_hub
except ImportError:
    huggingface_hub = types.ModuleType('huggingface_hub')
    sys.modules['huggingface_hub'] = huggingface_hub

if not hasattr(huggingface_hub, 'HfFolder'):
    class DummyHfFolder:
        @staticmethod
        def get_token(): return None
        @staticmethod
        def save_token(token): pass
        @staticmethod
        def delete_token(): pass
    huggingface_hub.HfFolder = DummyHfFolder

import gradio as gr

def estimate_tokens(text):
    """Ultra-fast local token estimator (Roughly 1 token = 4 chars for code/text setup)"""
    if not text:
        return 0
    return max(1, len(text) // 4 + text.count(' ') // 2)

def shrink_python_code(source_code):
    """Parses and strips syntax trees to remove bloat tokens natively"""
    try:
        tree = ast.parse(source_code)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
                if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant) and isinstance(node.body[0].value.value, str):
                    node.body.pop(0)
                    
        clean_code = ast.unparse(tree)
        clean_code = re.sub(r'\n\s*\n', '\n', clean_code)
        return clean_code.strip()
    except Exception:
        code = re.sub(r'#.*', '', source_code)
        code = re.sub(r'\"\"\"[\s\S]*?\"\"\"', '', code)
        code = re.sub(r'\'\'\'[\s\S]*?\'\'\'', '', code)
        code = re.sub(r'\n\s*\n', '\n', code)
        return code.strip()

def shrink_generic_text(raw_data):
    """Minifies structured JSON/Data arrays and repetitive text strings"""
    try:
        parsed_json = json.loads(raw_data)
        return json.dumps(parsed_json, separators=(',', ':'))
    except Exception:
        text = re.sub(r'\s+', ' ', raw_data)
        text = text.replace(", ", ",").replace(": ", ":").replace("; ", ";")
        return text.strip()

def decimator_engine(input_payload, mode):
    if not input_payload.strip():
        return "", "### ⚠️ System Warning\nPlease input your code or data block first!", 0, "0%", "$0.00"

    initial_tokens = estimate_tokens(input_payload)
    
    if mode == "Python/R/SQL Code Matrix":
        decimated_output = shrink_python_code(input_payload)
    else:
        decimated_output = shrink_generic_text(input_payload)
        
    final_tokens = estimate_tokens(decimated_output)
    
    token_delta = initial_tokens - final_tokens
    reduction_percentage = 0 if initial_tokens == 0 else (token_delta / initial_tokens) * 100
    estimated_savings = (token_delta / 1000) * 0.015
    if estimated_savings < 0: 
        estimated_savings = 0.0

    report_markdown = f"""
    ### 📊 Token Decimation Analytics Matrix
    - **Original Payload Footprint:** `{initial_tokens}` estimated tokens.
    - **Optimized Stream Footprint:** `{final_tokens}` estimated tokens.
    - **Tokens Destroyed Successfully:** `{token_delta}` tokens wiped from context.
    """
    
    pct_string = f"{reduction_percentage:.1f}%"
    savings_string = f"${estimated_savings:.4f}"
    
    return decimated_output, report_markdown, token_delta, pct_string, savings_string

# Custom Cyber Matrix Terminal UI Theme for Judges
# Extended .margin-top-class to substitute the invalid row inline style attribute parameter safely
custom_css = """
body, .gradio-container { background-color: #050811 !important; font-family: 'Courier New', monospace; color: #00ff66 !important; }
.decimate-btn { background: linear-gradient(135deg, #00ff66, #047857) !important; color: #050811 !important; font-weight: bold !important; border: 1px solid #00ff66 !important; border-radius: 4px !important; letter-spacing: 1px; }
.decimate-btn:hover { box-shadow: 0 0 20px rgba(0,255,102,0.6); color: white !important; }
.panel-border { border: 1px solid #1e293b !important; border-radius: 6px; padding: 15px; background: #090d1a !important; box-shadow: inset 0 0 10px rgba(0,255,102,0.05); }
.metric-box { background: #0d1527 !important; border: 1px solid #00ff66 !important; border-radius: 4px; padding: 10px; text-align: center; }
.margin-top-class { margin-top: 20px !important; }
textarea, input { background-color: #02040a !important; color: #38bdf8 !important; border: 1px solid #1e293b !important; font-family: 'Consolas', monospace !important; }
textarea:focus { border-color: #00ff66 !important; }
"""

# 🔥 FIXED: Removed css parameters from gr.Blocks initialization wrapper
with gr.Blocks(title="Code-Shrink v1.0") as demo:
    gr.HTML(
        """
        <div style="text-align: center; margin-bottom: 20px; padding: 20px; background: #090d1a; border-radius: 6px; border: 1px solid #00ff66; box-shadow: 0 0 15px rgba(0,255,102,0.1);">
            <h1 style='margin: 0; font-size: 28px; color: #00ff66; letter-spacing: 3px;'>⚡ CODE-SHRINK: TOKEN-DECIMATOR</h1>
            <p style='margin: 5px 0 0 0; color: #94a3b8; font-size: 13px;'>Algorithmic Context Optimization Matrix // Bypassing LLM Budget Inflation Natively</p>
        </div>
        """
    )
    
    with gr.Row():
        with gr.Column(scale=3, elem_classes="panel-border"):
            gr.Markdown("### 📥 Raw Context Payload Injection")
            payload_input = gr.Textbox(
                placeholder="Paste your bloated Python code, SQL queries, or huge JSON dictionaries here...",
                label="Raw Context Input",
                lines=12
            )
            
            with gr.Row():
                mode_dropdown = gr.Dropdown(
                    choices=["Python/R/SQL Code Matrix", "Structured JSON / Raw Text Array"],
                    value="Python/R/SQL Code Matrix",
                    label="Lexical Processing Mode"
                )
            
            gr.HTML("<br>")
            process_btn = gr.Button("⚡ DECIMATE CONTEXT TOKENS", elem_classes="decimate-btn")
            
        with gr.Column(scale=3, elem_classes="panel-border"):
            gr.Markdown("### 📤 Optimized Micro-Stream Output")
            payload_output = gr.Textbox(
                label="Decimated Token Stream (Ready for LLM Prompt)",
                lines=12,
                interactive=False
            )
            
            gr.HTML("<br>")
            with gr.Row():
                with gr.Column(scale=1, elem_classes="metric-box"):
                    gr.Markdown("<span style='color:#94a3b8; font-size:11px;'>COMPRESSION</span>")
                    pct_output = gr.HTML("<b style='color:#00ff66; font-size:22px;'>0%</b>")
                with gr.Column(scale=1, elem_classes="metric-box"):
                    gr.Markdown("<span style='color:#94a3b8; font-size:11px;'>TOKENS WIPED</span>")
                    delta_output = gr.HTML("<b style='color:#38bdf8; font-size:22px;'>0</b>")
                with gr.Column(scale=1, elem_classes="metric-box"):
                    gr.Markdown("<span style='color:#94a3b8; font-size:11px;'>EST. API SAVINGS</span>")
                    savings_output = gr.HTML("<b style='color:#e879f9; font-size:22px;'>$0.00</b>")

    # 🔥 FIXED: Replaced inline style injection parameters with valid custom css mapping selectors
    with gr.Row(elem_classes=["panel-border", "margin-top-class"]):
        diagnostics_output = gr.Markdown("`System Engine: Standing by. Awaiting dynamic payload mapping signals...`")

    process_btn.click(
        fn=decimator_engine,
        inputs=[payload_input, mode_dropdown],
        outputs=[payload_output, diagnostics_output, delta_output, pct_output, savings_output]
    )

# 🔥 FIXED: Passed custom UI styling matrices explicitly inside launcher execution limits
demo.launch(css=custom_css)

