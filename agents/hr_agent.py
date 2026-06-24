# Employee & Intern Advisor
# agents/hr_agent.py
import os
import textwrap
from groq import Groq
from prompts.hr_policy_prompt import HR_HYBRID_SYSTEM_PROMPT

# Initialize the central client using the environment variable
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_hr_agent(user_query: str) -> str:
    """
    HR Agent: Provides official corporate policy guidelines using Hybrid Prompting.
    Enforces 0.2 temperature, 0.2 top_p, and 400 max tokens per configuration table.
    """
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # High reasoning capability for policy compliance
        messages=[
            {"role": "system", "content": HR_HYBRID_SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ],
        temperature=0.2,   # Low temperature to minimize any creative risk/hallucination
        top_p=0.2,         # Highly focused on factual tokens from the context
        max_tokens=400     # Ample token limit for structured policy explanations
    )
    
    raw_output = completion.choices[0].message.content.strip()
    
    # Formatter to keep the paragraphs neat and responsive
    wrapped_output = "\n".join([textwrap.fill(line, width=85) for line in raw_output.split('\n')])
    return wrapped_output

    