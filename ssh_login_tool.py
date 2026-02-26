import paramiko
import sys
import os
from openai import OpenAI # Or use 'ollama' for local AI

# Configuration - In a real app, use environment variables!
AI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=AI_API_KEY)

class SSHAIAnalyzer:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def execute_and_analyze(self, command):
        try:
            print(f"[*] Connecting to {self.host}...")
            self.client.connect(self.host, username=self.user, password=self.password)
            
            stdin, stdout, stderr = self.client.exec_command(command)
            error = stderr.read().decode()
            output = stdout.read().decode()

            if error:
                print(f"[!] Remote Error Detected: {error}")
                self.get_ai_solution(error)
            else:
                print(f"[+] Command Output:\n{output}")

        except Exception as e:
            print(f"[X] Connection Failed: {e}")
        finally:
            self.client.close()

    def get_ai_solution(self, error_msg):
        print("[*] Consulting AI for a fix...")
        prompt = f"The following error occurred on a Linux server during an SSH session: '{error_msg}'. Provide a concise 1-sentence fix."
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        print(f"💡 AI Suggestion: {response.choices[0].message.content}")

if __name__ == "__main__":
    # Quick CLI usage
    tool = SSHAIAnalyzer("192.168.1.10", "root", "password123")
    tool.execute_and_analyze("systemctl status nginx")
