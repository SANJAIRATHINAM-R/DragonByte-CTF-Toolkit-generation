#!/usr/bin/env python3
"""
DragonByte CTF Toolkit - Steganography Module
Actions: scan, extract, strings
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from backend.utils import (
    print_info, print_warn, print_error, print_result,
    print_subsection, run_command, require_tool,
    validate_file, read_file_bytes
)


class StegoEngine:
    """Steganography analysis: metadata, hidden data, strings."""

    def run(self, action: str, target: str) -> str:
        if action == "scan":
            return self._scan(target)
        elif action == "extract":
            return self._extract(target)
        elif action == "strings":
            return self._strings(target)
        return ""

    # -----------------------------------------------------------------------
    # Full scan (metadata + binwalk + steghide attempt)
    # -----------------------------------------------------------------------

    def _scan(self, target: str) -> str:
        if not validate_file(target, "image/file"):
            return ""
        print_info(f"Scanning: {target}")
        results = []

        # ExifTool – metadata
        print_subsection("ExifTool – Metadata Extraction")
        if require_tool("exiftool"):
            ok, out = run_command(["exiftool", target])
            if out:
                print(out)
                results.append(out)
            else:
                print_warn("No metadata returned.")
        else:
            print_warn("Skipping ExifTool.")

        # Binwalk – hidden files / embedded data
        print_subsection("Binwalk – Embedded Data Detection")
        if require_tool("binwalk"):
            ok, out = run_command(["binwalk", target])
            if out:
                print(out)
                results.append(out)
            else:
                print_warn("Binwalk returned no results.")
        else:
            print_warn("Skipping Binwalk.")

        # Steghide – attempt extraction without password
        print_subsection("Steghide – Hidden Data Check")
        if require_tool("steghide"):
            ok, out = run_command(["steghide", "info", "-p", "", target], timeout=15)
            if out:
                print(out)
                results.append(out)
            else:
                print_warn("Steghide found no embedded data (or password required).")
        else:
            print_warn("Skipping Steghide.")

        # Quick strings check
        results.append(self._strings(target))

        return "\n".join(filter(None, results))

    # -----------------------------------------------------------------------
    # Extract hidden archive / payload
    # -----------------------------------------------------------------------

    def _extract(self, target: str) -> str:
        if not validate_file(target, "image/file"):
            return ""
        print_info(f"Attempting extraction from: {target}")
        results = []

        print_subsection("Binwalk – Carve Embedded Files")
        if require_tool("binwalk"):
            out_dir = f"{target}_extracted"
            ok, out = run_command(["binwalk", "-e", "--directory", out_dir, target])
            if out:
                print(out)
                results.append(out)
            if os.path.isdir(out_dir):
                print_info(f"Extracted files saved to: {out_dir}")
        else:
            print_warn("Binwalk not available.")

        print_subsection("Steghide – Extract Payload")
        if require_tool("steghide"):
            out_file = f"{target}.steghide_out"
            ok, out = run_command(
                ["steghide", "extract", "-sf", target, "-p", "", "-f", "-xf", out_file],
                timeout=15
            )
            if out:
                print(out)
                results.append(out)
        else:
            print_warn("Steghide not available.")

        return "\n".join(filter(None, results))

    # -----------------------------------------------------------------------
    # String scanning
    # -----------------------------------------------------------------------

    def _strings(self, target: str) -> str:
        if not validate_file(target, "file"):
            return ""
        print_subsection("Strings – Printable Character Extraction")

        # Use system `strings` if available, otherwise manual scan
        if require_tool("strings"):
            ok, out = run_command(["strings", "-n", "4", target])
        else:
            print_warn("'strings' binary not found; using Python fallback.")
            raw = read_file_bytes(target)
            if not raw:
                return ""
            import re
            hits = re.findall(rb'[\x20-\x7e]{4,}', raw)
            out = "\n".join(h.decode('ascii', errors='replace') for h in hits)

        if out:
            # Limit output to first 80 lines to avoid flooding terminal
            lines = out.splitlines()
            preview = lines[:80]
            print("\n".join(preview))
            if len(lines) > 80:
                print_warn(f"… {len(lines) - 80} more lines omitted.")
        else:
            print_warn("No printable strings found.")

        return out
