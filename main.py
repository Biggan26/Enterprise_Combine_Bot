# main.py
print("[DEBUG LOG 1]: Python script started execution...")

import os
import sys
from dotenv import load_dotenv

print("[DEBUG LOG 2]: Dependencies imported successfully. Loading variables...")

# Load environment variables from .env file
load_dotenv()

# 1. Importing all dedicated agent modules from the agents package
from agents.router_agent import run_router_agent
from agents.security_agent import run_security_agent
from agents.finance_agent import run_finance_agent
from agents.hr_agent import run_hr_agent
from agents.support_agent import run_support_agent

print("[DEBUG LOG 3]: All custom agent modules imported successfully.")

# Verify that the Groq API key is configured correctly
if not os.getenv("GROQ_API_KEY"):
    print("[CRITICAL ERROR]: GROQ_API_KEY is missing or empty in your .env file!")
    sys.exit(1)

def central_orchestrator_pipeline(user_query: str):
    """
    The Master Controller: Receives user input, queries the Router Agent,
    and dynamically dispatches the query to the designated specialist agent.
    """
    print("\n" + "="*60)
    print(f"🕵️  Input Query: '{user_query}'")
    print("-" * 60)
    
    try:
        detected_tag = run_router_agent(user_query)
        print(f"⚡ [SYSTEM LOG] -> Router Classified As: {detected_tag}")
        print("-" * 60)
    except Exception as e:
        print(f"[ROUTER ERROR]: Failed to classify query. Reason: {e}")
        return

    response = ""
    try:
        if "[SECURITY_ALERT]" in detected_tag:
            response = run_security_agent(user_query)
        elif "[FINANCE]" in detected_tag:
            response = run_finance_agent(user_query)
        elif "[HR_POLICY]" in detected_tag:
            response = run_hr_agent(user_query)
        elif "[GENERAL_SUPPORT]" in detected_tag:
            response = run_support_agent(user_query)
        else:
            print("⚠️ [SYSTEM WARNING]: Unexpected tag. Defaulting to Support Agent.")
            response = run_support_agent(user_query)
            
    except Exception as e:
        response = f"[AGENT EXECUTION ERROR]: An error occurred inside the sub-agent. Reason: {e}"

    print(response)
    print("="*60 + "\n")

# Main Loop Trigger without the restrictive __main__ wrap to ensure it fires
print("[DEBUG LOG 4]: Reached the main interactive CLI loop setup...")

print("=" * 60)
print("🚀 GoML SMART MULTI-AGENT ENTERPRISE SYSTEM OPERATIONAL 🚀")
print("=" * 60)
print("Type 'exit' or 'quit' to terminate the application.\n")

while True:
    try:
        user_input = input("Ask GoML Bot: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ['exit', 'quit']:
            print("\nShutting down Enterprise Bot. Have a great day!")
            break
            
        central_orchestrator_pipeline(user_input)
        
    except KeyboardInterrupt:
        print("\nSystem forced termination. Exiting...")
        break
    except Exception as e:
        print(f"\n[CRITICAL RUNTIME ERROR]: {str(e)}")