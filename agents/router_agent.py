# Ingestion & Gatekeeper Logic

# agents/router_agent.py
import os
from groq import Groq
from prompts.router_prompt import ROUTER_SYSTEM_PROMPT

# Initialize the central client using the environment variable
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_router_agent(user_query: str) -> str:
    """
    Gatekeeper Agent: Classifies the user input into a specific domain tag.
    Uses strict 0.0 temperature and low top_p for accurate few-shot routing.
    """
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": ROUTER_SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ],
        temperature=0.0,   # Strict deterministic mapping
        top_p=0.1,         # Focuses heavily on the top likelihood tokens
        max_tokens=20      # Prevents conversational fluff, targets just the tag
    )
    
    # Extract and clean the domain tag output
    detected_tag = completion.choices[0].message.content.strip()
    return detected_tag