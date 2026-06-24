# Conveyance & Budget Analyzer
# agents/finance_agent.py
import os
import textwrap
from groq import Groq
from prompts.finance_prompt import FINANCE_SYSTEM_PROMPT

# Initialize the central client using the environment variable
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_finance_agent(user_query: str) -> str:
    """
    Finance Agent: Computes mileage and travel allowance claims based on corporate policies.
    Enforces 0.1 temperature and 250 max tokens per configuration table.
    """
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # Highly efficient for numeric/ReAct flow tasks
        messages=[
            {"role": "system", "content": FINANCE_SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ],
        temperature=0.1,   # Fixed low temperature for deterministic mathematical calculations
        top_p=0.2,         # Controls token selection strictly for accuracy
        max_tokens=250     # Standard constraint as specified in the configuration
    )
    
    raw_output = completion.choices[0].message.content.strip()
    
    # Format the layout to avoid single-line scrolling issues in Jupyter or terminal
    wrapped_output = "\n".join([textwrap.fill(line, width=85) for line in raw_output.split('\n')])
    return wrapped_output