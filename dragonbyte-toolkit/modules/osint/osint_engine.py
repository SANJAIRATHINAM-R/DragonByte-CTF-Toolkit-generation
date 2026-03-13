#!/usr/bin/env python3
"""
DragonByte CTF Toolkit - OSINT Module
Actions: domain, email, subdomains
"""

import os
import sys
import socket
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from backend.utils import (
    print_info, print_warn, print_error, print_result,
    print_subsection, run_command, require_tool, validate_target
)


class OsintEngine:
    """OSINT: domain intel, email harvesting, subdomain enumeration."""

    def run(self, action: str, target: str) -> str:
        if action == "domain":
            return self._domain(target)
        elif action == "email":
            return self._email(target)
        elif action == "subdomains":
            return self._subdomains(target)
        return ""

    # -----------------------------------------------------------------------
    # Domain intelligence
    # -----------------------------------------------------------------------

    def _domain(self, target: str) -> str:
        if not validate_target(target, "domain"):
            return ""
        print_info(f"Target domain: {target}")
        results = []

        # DNS resolution
        print_subsection("DNS Resolution")
        try:
            ips = socket.getaddrinfo(target, None)
            seen = set()
            for res in ips:
                ip = res[4][0]
                if ip not in seen:
                    seen.add(ip)
                    print_result("Resolved IP", ip)
                    results.append(f"IP: {ip}")
        except socket.gaierror as e:
            print_error(f"DNS resolution failed: {e}")

        # WHOIS
        print_subsection("WHOIS Lookup")
        if require_tool("whois"):
            ok, out = run_command(["whois", target], timeout=30)
            if out:
                # Print first 40 lines
                lines = out.splitlines()[:40]
                print("\n".join(lines))
                results.append(out)

        # theHarvester
        print_subsection("theHarvester – Email & Host Harvesting")
        harvester = "theHarvester" if require_tool("theHarvester") else (
            "theharvester" if require_tool("theharvester") else None
        )
        if harvester:
            ok, out = run_command(
                [harvester, "-d", target, "-b", "bing", "-l", "100"],
                timeout=60
            )
            if out:
                print(out)
                results.append(out)
        else:
            print_warn("theHarvester not found. Install: apt install theharvester")

        # nmap basic port scan
        print_subsection("Nmap – Basic Port Scan")
        if require_tool("nmap"):
            ok, out = run_command(["nmap", "-F", "--open", target], timeout=60)
            if out:
                print(out)
                results.append(out)
        else:
            print_warn("Nmap not available.")

        return "\n".join(results)

    # -----------------------------------------------------------------------
    # Email harvesting
    # -----------------------------------------------------------------------

    def _email(self, target: str) -> str:
        if not validate_target(target, "domain"):
            return ""
        print_info(f"Harvesting emails for: {target}")
        results = []

        print_subsection("theHarvester – Email Harvest")
        harvester = "theHarvester" if require_tool("theHarvester") else (
            "theharvester" if require_tool("theharvester") else None
        )
        if harvester:
            ok, out = run_command(
                [harvester, "-d", target, "-b", "all", "-l", "200"],
                timeout=90
            )
            if out:
                print(out)
                results.append(out)
        else:
            print_warn("theHarvester not available.")

        return "\n".join(results)

    # -----------------------------------------------------------------------
    # Subdomain enumeration
    # -----------------------------------------------------------------------

    def _subdomains(self, target: str) -> str:
        if not validate_target(target, "domain"):
            return ""
        print_info(f"Enumerating subdomains for: {target}")
        results = []

        # Amass
        print_subsection("Amass – Subdomain Enumeration")
        if require_tool("amass"):
            ok, out = run_command(
                ["amass", "enum", "-passive", "-d", target],
                timeout=120
            )
            if out:
                print(out)
                results.append(out)
        else:
            print_warn("Amass not found. Install: apt install amass")

        # Gobuster DNS mode
        print_subsection("Gobuster – DNS Brute Force")
        if require_tool("gobuster"):
            wordlist = "/usr/share/wordlists/dns/subdomains-top1million-5000.txt"
            if not os.path.isfile(wordlist):
                wordlist = "/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt"
            if os.path.isfile(wordlist):
                ok, out = run_command(
                    ["gobuster", "dns", "-d", target, "-w", wordlist, "-t", "50"],
                    timeout=120
                )
                if out:
                    print(out)
                    results.append(out)
            else:
                print_warn("DNS wordlist not found; skipping gobuster DNS.")
        else:
            print_warn("Gobuster not available.")

        return "\n".join(results)
