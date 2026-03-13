#!/usr/bin/env python3
"""
DragonByte CTF Toolkit - Web Module
Actions: scan, sqli, headers
"""

import os
import sys
import urllib.request
import urllib.error

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from backend.utils import (
    print_info, print_warn, print_error, print_result,
    print_subsection, run_command, require_tool, validate_target
)


class WebEngine:
    """Web vulnerability testing: directory brute force, SQLi, headers."""

    def run(self, action: str, target: str) -> str:
        if action == "scan":
            return self._scan(target)
        elif action == "sqli":
            return self._sqli(target)
        elif action == "headers":
            return self._headers(target)
        return ""

    # -----------------------------------------------------------------------
    # Full scan (headers + directory brute force)
    # -----------------------------------------------------------------------

    def _scan(self, target: str) -> str:
        if not validate_target(target, "URL"):
            return ""
        print_info(f"Target: {target}")
        results = [self._headers(target)]

        # Gobuster directory scan
        print_subsection("Gobuster – Directory Brute Force")
        if require_tool("gobuster"):
            wordlist = self._find_dirlist()
            if wordlist:
                print_info(f"Using wordlist: {wordlist}")
                ok, out = run_command(
                    ["gobuster", "dir", "-u", target, "-w", wordlist,
                     "-t", "30", "--no-error", "-q"],
                    timeout=180
                )
                if out:
                    print(out)
                    results.append(out)
            else:
                print_warn("No directory wordlist found.")
        else:
            print_warn("Gobuster not found. Install: apt install gobuster")

        # Nikto
        print_subsection("Nikto – Web Server Scanner")
        if require_tool("nikto"):
            ok, out = run_command(
                ["nikto", "-h", target, "-maxtime", "60"],
                timeout=90
            )
            if out:
                print(out)
                results.append(out)
        else:
            print_warn("Nikto not available.")

        return "\n".join(filter(None, results))

    # -----------------------------------------------------------------------
    # SQLi testing
    # -----------------------------------------------------------------------

    def _sqli(self, target: str) -> str:
        if not validate_target(target, "URL"):
            return ""
        print_info(f"Testing for SQL injection: {target}")

        print_subsection("SQLmap – Automated SQLi Detection")
        if require_tool("sqlmap"):
            ok, out = run_command(
                ["sqlmap", "-u", target, "--batch", "--level=2",
                 "--risk=1", "--output-dir=/tmp/sqlmap_dragonbyte"],
                timeout=180
            )
            if out:
                print(out)
            return out or ""
        else:
            print_warn("SQLmap not found. Install: apt install sqlmap")
            return ""

    # -----------------------------------------------------------------------
    # HTTP header analysis
    # -----------------------------------------------------------------------

    def _headers(self, target: str) -> str:
        if not validate_target(target, "URL"):
            return ""
        print_subsection("HTTP Header Analysis")
        results = []

        try:
            req = urllib.request.Request(target, method="HEAD")
            req.add_header("User-Agent", "DragonByte-CTF-Toolkit/1.0")
            with urllib.request.urlopen(req, timeout=15) as resp:
                print_result("Status", str(resp.status))
                results.append(f"Status: {resp.status}")
                for key, val in resp.headers.items():
                    print_result(key, val)
                    results.append(f"{key}: {val}")

                # Flag interesting / missing security headers
                security_headers = [
                    "X-Frame-Options",
                    "X-XSS-Protection",
                    "Strict-Transport-Security",
                    "Content-Security-Policy",
                    "X-Content-Type-Options",
                ]
                print_subsection("Security Header Audit")
                present = {k.lower() for k in resp.headers.keys()}
                for hdr in security_headers:
                    if hdr.lower() in present:
                        print_info(f"  ✓ {hdr}")
                    else:
                        print_warn(f"  ✗ MISSING: {hdr}")

        except urllib.error.HTTPError as e:
            print_warn(f"HTTP {e.code}: {e.reason}")
            results.append(f"HTTP Error: {e.code} {e.reason}")
        except Exception as e:
            print_error(f"Could not connect to {target}: {e}")

        return "\n".join(results)

    def _find_dirlist(self) -> str:
        candidates = [
            "/usr/share/wordlists/dirb/common.txt",
            "/usr/share/seclists/Discovery/Web-Content/common.txt",
            "/usr/share/dirbuster/wordlists/directory-list-2.3-small.txt",
        ]
        for p in candidates:
            if os.path.isfile(p):
                return p
        return ""
