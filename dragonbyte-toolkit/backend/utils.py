#!/usr/bin/env python3
"""
DragonByte CTF Toolkit - Utilities
Shared helpers: output formatting, command execution, file validation.
"""

import os
import subprocess
import shutil
from typing import Optional, Tuple

# ANSI color codes
RED    = '\033[0;31m'
GREEN  = '\033[0;32m'
YELLOW = '\033[1;33m'
CYAN   = '\033[0;36m'
BLUE   = '\033[0;34m'
BOLD   = '\033[1m'
RESET  = '\033[0m'


# ---------------------------------------------------------------------------
# Formatted output helpers
# ---------------------------------------------------------------------------

def print_info(msg: str) -> None:
    """Print a standard informational line."""
    print(f"{GREEN}[+]{RESET} {msg}")


def print_warn(msg: str) -> None:
    """Print a warning."""
    print(f"{YELLOW}[!]{RESET} {msg}")


def print_error(msg: str) -> None:
    """Print an error message."""
    print(f"{RED}[✗]{RESET} {msg}")


def print_result(label: str, value: str) -> None:
    """Print a key-value result pair."""
    print(f"  {CYAN}{label:<20}{RESET} {value}")


def print_section(title: str) -> None:
    """Print a section header."""
    width = 60
    print(f"\n{BOLD}{CYAN}{'─' * width}{RESET}")
    print(f"{BOLD}{CYAN}  {title}{RESET}")
    print(f"{BOLD}{CYAN}{'─' * width}{RESET}\n")


def print_subsection(title: str) -> None:
    """Print a sub-section label."""
    print(f"\n{BOLD}{BLUE}[>] {title}{RESET}")
    print(f"{BLUE}{'·' * 40}{RESET}")


# ---------------------------------------------------------------------------
# Command execution
# ---------------------------------------------------------------------------

def run_command(
    cmd: list,
    timeout: int = 120,
    capture: bool = True
) -> Tuple[bool, str]:
    """
    Execute a shell command.

    Args:
        cmd:     Command as a list of strings, e.g. ['ls', '-la']
        timeout: Max seconds to wait (default 120)
        capture: If True, return stdout/stderr; otherwise stream to terminal

    Returns:
        (success: bool, output: str)
    """
    try:
        if capture:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            output = result.stdout + result.stderr
            return result.returncode == 0, output.strip()
        else:
            result = subprocess.run(cmd, timeout=timeout)
            return result.returncode == 0, ""
    except FileNotFoundError:
        return False, f"Command not found: {cmd[0]}"
    except subprocess.TimeoutExpired:
        return False, f"Command timed out after {timeout}s: {' '.join(cmd)}"
    except Exception as e:
        return False, f"Execution error: {e}"


def tool_available(tool_name: str) -> bool:
    """Check whether a CLI tool is available on PATH."""
    return shutil.which(tool_name) is not None


def require_tool(tool_name: str) -> bool:
    """
    Check for a tool and warn the user if it is missing.
    Returns True if available, False otherwise.
    """
    if tool_available(tool_name):
        return True
    print_warn(f"Tool not found: '{tool_name}'. Install it with: apt install {tool_name}")
    return False


# ---------------------------------------------------------------------------
# File validation
# ---------------------------------------------------------------------------

def validate_file(path: Optional[str], label: str = "target file") -> bool:
    """
    Check that a file path is provided and exists.
    Prints an appropriate error message if not.
    """
    if not path:
        print_error(f"No {label} specified.")
        return False
    if not os.path.isfile(path):
        print_error(f"File not found: {path}")
        return False
    return True


def validate_target(target: Optional[str], label: str = "target") -> bool:
    """Check that a non-empty target string was provided."""
    if not target:
        print_error(f"No {label} specified.")
        return False
    return True


def file_size_mb(path: str) -> float:
    """Return the size of a file in megabytes."""
    return os.path.getsize(path) / (1024 * 1024)


def read_file_lines(path: str) -> list:
    """Read a file and return its lines (stripped). Returns [] on error."""
    try:
        with open(path, "r", errors="replace") as f:
            return [line.strip() for line in f.readlines()]
    except Exception as e:
        print_error(f"Could not read file '{path}': {e}")
        return []


def read_file_bytes(path: str) -> Optional[bytes]:
    """Read and return raw bytes from a file. Returns None on error."""
    try:
        with open(path, "rb") as f:
            return f.read()
    except Exception as e:
        print_error(f"Could not read file '{path}': {e}")
        return None
