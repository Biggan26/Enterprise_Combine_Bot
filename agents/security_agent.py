# PII Defense Core

# agents/security_agent.py
import os
import textwrap
from groq import Groq
from prompts.security_prompt import SECURITY_SYSTEM_PROMPT

# Initialize the central client using the environment variable
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_security_agent(user_query: str) -> str:
    """
    Guardrail Agent: Validates employee profile lookup and blocks unauthorized PII leaks.
    Enforces strict 0.0 temperature and 100 max tokens per configuration table.
    """
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SECURITY_SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ],
        temperature=0.0,   # Maximum rule compliance
        top_p=0.1,         # Explores only highly deterministic tokens
        max_tokens=100     # Hard ceiling for precise, secure answers
    )
    
    raw_output = completion.choices[0].message.content.strip()
    
    # Text formatter to handle the single-line output issue in terminal or UI
    wrapped_output = "\n".join([textwrap.fill(line, width=85) for line in raw_output.split('\n')])
    return wrapped_output