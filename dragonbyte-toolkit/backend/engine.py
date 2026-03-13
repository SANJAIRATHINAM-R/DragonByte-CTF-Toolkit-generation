#!/usr/bin/env python3
"""
DragonByte CTF Toolkit - Backend Engine
Routes CLI commands to the correct module engine.
"""

import sys
import os

# Ensure the project root is in the Python path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from backend.utils import print_info, print_error, print_section
from backend.flag_detector import scan_for_flags


# Supported modules and their valid actions
MODULE_ACTIONS = {
    "crypto":   ["crack", "identify"],
    "stego":    ["scan", "extract", "strings"],
    "osint":    ["domain", "email", "subdomains"],
    "web":      ["scan", "sqli", "headers"],
    "forensic": ["analyze", "extract", "strings"],
    "misc":     ["decode", "qr", "strings"],
}


def load_module(module_name: str):
    """Dynamically import the requested module engine."""
    try:
        if module_name == "crypto":
            from modules.crypto.crypto_engine import CryptoEngine
            return CryptoEngine()
        elif module_name == "stego":
            from modules.stego.stego_engine import StegoEngine
            return StegoEngine()
        elif module_name == "osint":
            from modules.osint.osint_engine import OsintEngine
            return OsintEngine()
        elif module_name == "web":
            from modules.web.web_engine import WebEngine
            return WebEngine()
        elif module_name == "forensic":
            from modules.forensics.forensic_engine import ForensicEngine
            return ForensicEngine()
        elif module_name == "misc":
            from modules.misc.misc_engine import MiscEngine
            return MiscEngine()
    except ImportError as e:
        print_error(f"Failed to load module '{module_name}': {e}")
        sys.exit(1)


def main():
    args = sys.argv[1:]  # Strip script name; bash passes remaining args

    if len(args) < 2:
        print_error("Usage: dragonbyte <module> <action> [target]")
        print_info("Run 'dragonbyte --help' for usage.")
        sys.exit(1)

    module_name = args[0].lower()
    action      = args[1].lower()
    target      = args[2] if len(args) > 2 else None

    # Validate module
    if module_name not in MODULE_ACTIONS:
        print_error(f"Unknown module: '{module_name}'")
        print_info(f"Valid modules: {', '.join(MODULE_ACTIONS.keys())}")
        sys.exit(1)

    # Validate action
    valid_actions = MODULE_ACTIONS[module_name]
    if action not in valid_actions:
        print_error(f"Unknown action '{action}' for module '{module_name}'")
        print_info(f"Valid actions: {', '.join(valid_actions)}")
        sys.exit(1)

    print_section(f"Module: {module_name.capitalize()} | Action: {action}")

    # Load and dispatch to module
    engine = load_module(module_name)
    result = engine.run(action, target)

    # Post-process: scan output for CTF flags
    if result:
        print("\n" + result)
        flags = scan_for_flags(result)
        if flags:
            from backend.flag_detector import print_flags
            print_flags(flags)

    print_info("Module completed.\n")


if __name__ == "__main__":
    main()
