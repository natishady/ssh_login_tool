🛡️ AI-SSH Sentinel
Advanced SSH Automation with Integrated AI Troubleshooting.

🚀 Features
Automated SSH Execution: Multi-server command dispatch.

AI Error Analysis: Uses GPT-4/Ollama to interpret stderr and suggest bash fixes.

Secure Credential Handling: Support for .env and SSH keys.

🛠️ Installation
Bash
git clone https://github.com/0xNati/ssh-login-tool.git
cd ssh-login-tool
pip install -r requirements.txt
📖 Usage
Export your API Key: export OPENAI_API_KEY='your_key'

Run the tool: python ssh_login_tool.py


# AI-SSH Sentinel: Intelligent DevOps & SSH Automation Tool

[![Python Version](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Overview
AI-SSH Sentinel is a Python-based tool designed to automate SSH troubleshooting and provide AI-assisted solutions for remote Linux servers. It combines **SSH automation** with **AI-powered error analysis**, helping DevOps engineers and security professionals resolve issues faster.

## Features
- Connects to remote servers via SSH and executes commands
- Detects errors in command output and analyzes them
- Provides **AI-generated concise suggestions** for fixes
- Easy CLI usage and customizable for various automation tasks

## Requirements
- Python 3.10+
- Packages listed in `requirements.txt`:
  - `paramiko` for SSH connections
  - `openai` for AI suggestions
  - `python-dotenv` for environment variable management

## Installation
1. Clone the repo:
```bash
git clone https://github.com/natishady/ssh_login_tool.git
cd ssh_login_tool
