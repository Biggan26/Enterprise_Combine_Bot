# Friendly CoT Communicator
# agents/support_agent.py
import os
import textwrap
from groq import Groq
from prompts.general_support_prompt import SUPPORT_CoT_SYSTEM_PROMPT

# Initialize the central client using the environment variable
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_support_agent(user_query: str) -> str:
    """
    Support Agent: Handles greetings and administrative onboarding FAQs using CoT.
    Enforces 0.5 temperature, 0.6 top_p, and 350 max tokens per configuration table.
    """
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # Best for understanding human intent and CoT breakdown
        messages=[
            {"role": "system", "content": SUPPORT_CoT_SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ],
        temperature=0.5,   # Moderate creativity for a warm and welcoming tone
        top_p=0.6,         # Balanced distribution for dynamic conversational style
        max_tokens=350     # Strict ceiling as per the setup requirement
    )
    
    raw_output = completion.choices[0].message.content.strip()
    
    # Keeping the response well-wrapped so it looks great on terminal/UI
    wrapped_output = "\n".join([textwrap.fill(line, width=85) for line in raw_output.split('\n')])
    return wrapped_output
    