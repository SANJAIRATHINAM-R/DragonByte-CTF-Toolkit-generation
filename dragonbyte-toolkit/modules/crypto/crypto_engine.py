#!/usr/bin/env python3
"""
DragonByte CTF Toolkit - Crypto Module
Actions: crack, identify
"""

import re
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from backend.utils import (
    print_info, print_warn, print_error, print_result,
    print_subsection, run_command, require_tool,
    validate_file, validate_target, read_file_lines
)


class CryptoEngine:
    """Handles hash identification and password cracking."""

    # Hash signatures: (regex pattern, label)
    HASH_SIGNATURES = [
        (r'^[a-f0-9]{32}$',   'MD5'),
        (r'^[a-f0-9]{40}$',   'SHA-1'),
        (r'^[a-f0-9]{56}$',   'SHA-224'),
        (r'^[a-f0-9]{64}$',   'SHA-256'),
        (r'^[a-f0-9]{96}$',   'SHA-384'),
        (r'^[a-f0-9]{128}$',  'SHA-512'),
        (r'^\$2[aby]\$',      'bcrypt'),
        (r'^\$6\$',           'SHA-512 crypt'),
        (r'^\$5\$',           'SHA-256 crypt'),
        (r'^\$1\$',           'MD5 crypt'),
        (r'^[a-f0-9]{8}$',    'CRC-32 / Adler-32'),
        (r'^[A-Za-z0-9+/]{24}={0,2}$', 'Base64-encoded (possible hash)'),
        (r'^[a-f0-9]{48}$',   'Tiger-192 / SHA-3-192'),
    ]

    def run(self, action: str, target: str) -> str:
        """Dispatch action."""
        if action == "crack":
            return self._crack(target)
        elif action == "identify":
            return self._identify(target)
        return ""

    # -----------------------------------------------------------------------
    # Hash identification
    # -----------------------------------------------------------------------

    def _identify(self, target: str) -> str:
        """Identify the type of a hash string or hashes in a file."""
        results = []

        if target and os.path.isfile(target):
            print_info(f"Reading hashes from file: {target}")
            hashes = read_file_lines(target)
        else:
            if not validate_target(target, "hash string or file"):
                return ""
            hashes = [target]

        print_subsection("Hash Identification")
        for h in hashes:
            h = h.strip()
            if not h:
                continue
            detected = self._detect_hash_type(h)
            print_result(h[:30] + ("…" if len(h) > 30 else ""), detected)
            results.append(f"{h} → {detected}")

        return "\n".join(results)

    def _detect_hash_type(self, hash_str: str) -> str:
        """Return the likely hash type for a given string."""
        hash_str = hash_str.strip()
        for pattern, label in self.HASH_SIGNATURES:
            if re.match(pattern, hash_str, re.IGNORECASE):
                return label
        return "Unknown / Custom hash"

    # -----------------------------------------------------------------------
    # Hash cracking
    # -----------------------------------------------------------------------

    def _crack(self, target: str) -> str:
        """Attempt to crack hashes using hashcat and/or john."""
        if not validate_file(target, "hash file"):
            return ""

        print_info(f"Target hash file: {target}")
        output_parts = []

        # Detect hash types in file
        print_subsection("Detecting Hash Types")
        hashes = read_file_lines(target)
        for h in hashes:
            if h:
                htype = self._detect_hash_type(h)
                print_result(h[:40], htype)

        # Try John the Ripper
        print_subsection("John the Ripper")
        if require_tool("john"):
            wordlist = self._find_wordlist()
            cmd = ["john", target]
            if wordlist:
                print_info(f"Using wordlist: {wordlist}")
                cmd += [f"--wordlist={wordlist}"]
            else:
                print_warn("No wordlist found; using John's default mode")

            print_info("Running john… (this may take a while)")
            success, out = run_command(cmd, timeout=60)
            print_info("John output:")
            print(out or "(no output)")
            output_parts.append(out)

            # Show cracked passwords
            ok, cracked = run_command(["john", "--show", target])
            if cracked:
                print_info("Cracked credentials:")
                print(cracked)
                output_parts.append(cracked)
        else:
            print_warn("Skipping John the Ripper.")

        # Try Hashcat
        print_subsection("Hashcat")
        if require_tool("hashcat"):
            wordlist = self._find_wordlist()
            if wordlist:
                print_info(f"Running hashcat with wordlist: {wordlist}")
                cmd = ["hashcat", "-a", "0", target, wordlist, "--force", "-O"]
                success, out = run_command(cmd, timeout=120)
                print(out or "(no output)")
                output_parts.append(out)
            else:
                print_warn("No wordlist found; skipping hashcat.")
        else:
            print_warn("Skipping Hashcat.")

        return "\n".join(output_parts)

    def _find_wordlist(self):
        """Look for rockyou.txt in common Kali locations."""
        candidates = [
            "/usr/share/wordlists/rockyou.txt",
            "/usr/share/wordlists/rockyou.txt.gz",
            os.path.join(os.path.dirname(__file__), '..', '..', 'wordlists', 'rockyou.txt'),
        ]
        for path in candidates:
            if os.path.isfile(path):
                return path
        return None
