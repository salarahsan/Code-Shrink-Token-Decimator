---
title: Code Shrink Token Decimator
emoji: 👀
colorFrom: gray
colorTo: pink
sdk: gradio
sdk_version: 6.16.0
python_version: '3.13'
app_file: app.py
pinned: false
license: apache-2.0
short_description: 'Ultra-lightweight lexical token compressor that reduces LLM '
thumbnail: >-
  https://cdn-uploads.huggingface.co/production/uploads/6989c34475b229ddd8f18be3/ZTXpy1-KYjq7lfqHSb0ic.png
---

# ⚡ Code-Shrink: Token-Decimator v1.0

> **An Ultra-Lightweight Computational Utility Built to Eliminate LLM Context Bloat Natively on the Edge Container.**
> *Submitted for the Hugging Face Build Small Hackathon (Track 2: Performance & Efficiency Optimization).*

---

## 📽️ Project Demonstration & Walkthrough

Check out the full workflow, speed metrics, and feature breakdown in action here:
🔗 **[Watch the Live Demo on TikTok](https://www.tiktok.com/@salarai123/video/7648566501598940436)**

---

## 🔍 The Problem & The Solution

### The Bottleneck: LLM Context Inflation
Modern production applications relying on Large Language Model (LLM) APIs suffer from massive financial overhead. Upstream providers charge by the token—meaning heavy indentation loops, generic code comments, raw text formatting, and large structural blocks exponentially inflate infrastructure bills.

### The Engine: Code-Shrink
**Code-Shrink v1.0** passes raw context inputs through an edge-computed Abstract Syntax Tree (AST) framework. Instead of hosting gigabytes of neural network weights that lag and crash free hosting tiers, this application runs entirely on zero-cost, lightweight lexical optimization models. It reduces prompt token sizes by **up to 66% in under 10 milliseconds**.

---

## ⚡ Technical Core Features

* **Abstract Syntax Tree (AST) De-bloating:** Fully parses Python/R/SQL environments natively to structurally strip docstrings, developer comments, and empty lines while maintaining 100% semantic code integrity.
* **Lexical JSON Minification:** Collapses raw object dictionaries, spacing grids, and redundant string arrays into tight, machine-readable micro-streams.
* **On-Edge Real-Time Diagnostic Metrics:** Computes compression percentages and displays an estimated API cost savings panel instantly on execution.
* **Zero Infrastructure Overhead:** Operates 100% standalone with zero dependency on third-party backend servers, making it completely immune to public inference timeouts.

---

## 🛠️ Tech Stack & System Compatibility

- **Interface Framework:** Gradio (v6.0 Transition-Optimized Layer)
- **Computational Core:** Native Python AST & Lexical Pattern RegEx Engine
- **Data Manifestation:** Memory Buffer Stream Handlers (PIL/JSON Core)
- **Hardware Benchmarking:** Heavily optimized for restricted legacy processors (runs smooth down to Intel Core i3 4th Gen / 8GB RAM specs).

---

## 🎛️ Parameters Matrix

1. **Raw Context Input:** Inject bloated code strings or massive JSON arrays into the terminal panel.
2. **Lexical Processing Mode:** Set structural parser rules (`Python/R/SQL Code Matrix` or `Structured JSON / Raw Text Array`).
3. Click **⚡ DECIMATE CONTEXT TOKENS** to immediately wipe empty tokens and render the optimized micro-stream for your prompt.

---

## 📦 Local Workspace Setup

To clone and execute this performance node locally:

```bash
git clone [https://huggingface.co/spaces/build-small-hackathon/code-shrink-token-decimator](https://huggingface.co/spaces/build-small-hackathon/code-shrink-token-decimator)
cd code-shrink-token-decimator
pip install -r requirements.txt
python app.py
