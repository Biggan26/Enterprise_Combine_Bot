# this directory a python package
# agents/__init__.py
# Marks the agents directory as a Python package for clean, modular imports.

from .router_agent import run_router_agent
from .security_agent import run_security_agent
from .finance_agent import run_finance_agent
from .hr_agent import run_hr_agent
from .support_agent import run_support_agent

# Exposing core agent pipeline functions globally at the package level
__all__ = [
    "run_router_agent",
    "run_security_agent",
    "run_finance_agent",
    "run_hr_agent",
    "run_support_agent"
]

