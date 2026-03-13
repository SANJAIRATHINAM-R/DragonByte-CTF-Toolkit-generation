#!/usr/bin/env python3
"""
DragonByte CTF Toolkit - Flag Detector
Scans output text for common CTF flag formats and highlights them.
"""

import re
from typing import List

# Common CTF flag patterns
FLAG_PATTERNS = [
    r'flag\{[^}]+\}',
    r'FLAG\{[^}]+\}',
    r'picoCTF\{[^}]+\}',
    r'HTB\{[^}]+\}',
    r'THM\{[^}]+\}',
    r'CTF\{[^}]+\}',
    r'ctf\{[^}]+\}',
    r'DUCTF\{[^}]+\}',
    r'TBTL\{[^}]+\}',
    r'DawgCTF\{[^}]+\}',
    r'rtcp\{[^}]+\}',
    r'darkCTF\{[^}]+\}',
    r'[A-Z]{2,10}\{[A-Za-z0-9_\-!@#$%^&*()+=<>?./\\|~`]+\}',  # Generic XXX{...}
]

# ANSI colors for highlighting
BOLD   = '\033[1m'
RED    = '\033[0;31m'
GREEN  = '\033[0;32m'
YELLOW = '\033[1;33m'
CYAN   = '\033[0;36m'
RESET  = '\033[0m'


def scan_for_flags(text: str) -> List[str]:
    """
    Scan a block of text for CTF flag patterns.
    Returns a deduplicated list of found flags.
    """
    found = []
    for pattern in FLAG_PATTERNS:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            if match not in found:
                found.append(match)
    return found


def print_flags(flags: List[str]) -> None:
    """Pretty-print detected flags with highlighting."""
    if not flags:
        return

    print(f"\n{YELLOW}{'─' * 50}{RESET}")
    print(f"{BOLD}{GREEN}[🚩] FLAG(S) DETECTED!{RESET}")
    print(f"{YELLOW}{'─' * 50}{RESET}")
    for flag in flags:
        print(f"  {BOLD}{CYAN}{flag}{RESET}")
    print(f"{YELLOW}{'─' * 50}{RESET}\n")


def highlight_flags_in_text(text: str) -> str:
    """
    Return a version of text where detected flags are highlighted with ANSI colors.
    """
    for pattern in FLAG_PATTERNS:
        text = re.sub(
            pattern,
            lambda m: f"{BOLD}{GREEN}{m.group(0)}{RESET}",
            text,
            flags=re.IGNORECASE
        )
    return text
