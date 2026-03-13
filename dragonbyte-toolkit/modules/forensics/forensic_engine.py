#!/usr/bin/env python3
"""
DragonByte CTF Toolkit - Forensics Module
Actions: analyze, extract, strings
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from backend.utils import (
    print_info, print_warn, print_error, print_result,
    print_subsection, run_command, require_tool,
    validate_file, read_file_bytes
)


class ForensicEngine:
    """Digital forensics: PCAP analysis, file carving, string extraction."""

    def run(self, action: str, target: str) -> str:
        if action == "analyze":
            return self._analyze(target)
        elif action == "extract":
            return self._extract(target)
        elif action == "strings":
            return self._strings(target)
        return ""

    # -----------------------------------------------------------------------
    # Analyze – auto-detect file type and route
    # -----------------------------------------------------------------------

    def _analyze(self, target: str) -> str:
        if not validate_file(target, "forensic file"):
            return ""

        ext = os.path.splitext(target)[1].lower()
        print_info(f"Analyzing: {target}  (extension: {ext or 'none'})")

        if ext in (".pcap", ".pcapng", ".cap"):
            return self._analyze_pcap(target)
        elif ext in (".dd", ".img", ".bin", ".raw"):
            return self._analyze_disk(target)
        elif ext in (".vmem", ".mem", ".dmp"):
            return self._analyze_memory(target)
        else:
            # Generic: file type + strings + foremost
            results = []
            print_subsection("file – Magic Byte Detection")
            if require_tool("file"):
                ok, out = run_command(["file", target])
                print(out)
                results.append(out)

            results.append(self._strings(target))
            results.append(self._extract(target))
            return "\n".join(filter(None, results))

    # -----------------------------------------------------------------------
    # PCAP analysis
    # -----------------------------------------------------------------------

    def _analyze_pcap(self, target: str) -> str:
        results = []

        # tshark summary
        print_subsection("tshark – Packet Capture Summary")
        if require_tool("tshark"):
            # Protocol hierarchy
            ok, out = run_command(
                ["tshark", "-r", target, "-q", "-z", "io,phs"],
                timeout=60
            )
            if out:
                print(out)
                results.append(out)

            # Top conversations
            print_subsection("tshark – Top Conversations")
            ok, out = run_command(
                ["tshark", "-r", target, "-q", "-z", "conv,tcp"],
                timeout=60
            )
            if out:
                print(out[:3000])
                results.append(out)

            # HTTP objects
            print_subsection("tshark – HTTP Objects")
            ok, out = run_command(
                ["tshark", "-r", target, "-Y", "http", "-T", "fields",
                 "-e", "http.request.method", "-e", "http.request.uri",
                 "-e", "http.response.code"],
                timeout=60
            )
            if out:
                print(out[:2000])
                results.append(out)

            # DNS queries
            print_subsection("tshark – DNS Queries")
            ok, out = run_command(
                ["tshark", "-r", target, "-Y", "dns.qry.name",
                 "-T", "fields", "-e", "dns.qry.name"],
                timeout=60
            )
            if out:
                lines = list(set(out.splitlines()))[:50]
                print("\n".join(lines))
                results.append("\n".join(lines))
        else:
            print_warn("tshark not found. Install: apt install tshark")

        # Strings scan for flags
        results.append(self._strings(target))
        return "\n".join(filter(None, results))

    # -----------------------------------------------------------------------
    # Disk image analysis
    # -----------------------------------------------------------------------

    def _analyze_disk(self, target: str) -> str:
        results = []

        print_subsection("file – Image Type")
        if require_tool("file"):
            ok, out = run_command(["file", target])
            print(out)
            results.append(out)

        print_subsection("Foremost – File Carving")
        results.append(self._carve_foremost(target))

        return "\n".join(filter(None, results))

    # -----------------------------------------------------------------------
    # Memory analysis
    # -----------------------------------------------------------------------

    def _analyze_memory(self, target: str) -> str:
        results = []

        print_subsection("Volatility – Memory Analysis")
        vol_cmd = "vol" if require_tool("vol") else (
            "volatility" if require_tool("volatility") else None
        )
        if vol_cmd:
            # Try auto-detect profile and list processes
            ok, out = run_command([vol_cmd, "-f", target, "windows.pslist"], timeout=90)
            if not ok or not out:
                ok, out = run_command([vol_cmd, "-f", target, "linux.pslist"], timeout=90)
            if out:
                print(out[:3000])
                results.append(out)
        else:
            print_warn("Volatility not found. Install: pip3 install volatility3")

        results.append(self._strings(target))
        return "\n".join(filter(None, results))

    # -----------------------------------------------------------------------
    # File carving
    # -----------------------------------------------------------------------

    def _extract(self, target: str) -> str:
        if not validate_file(target, "file"):
            return ""
        results = []

        print_subsection("Foremost – File Carving")
        results.append(self._carve_foremost(target))

        print_subsection("Binwalk – Embedded Archive Extraction")
        if require_tool("binwalk"):
            out_dir = f"{target}_binwalk"
            ok, out = run_command(["binwalk", "-e", "--directory", out_dir, target])
            if out:
                print(out)
                results.append(out)
            if os.path.isdir(out_dir):
                print_info(f"Extracted files: {out_dir}")

        return "\n".join(filter(None, results))

    def _carve_foremost(self, target: str) -> str:
        if require_tool("foremost"):
            out_dir = f"{target}_foremost"
            ok, out = run_command(["foremost", "-o", out_dir, "-i", target], timeout=120)
            if ok:
                print_info(f"Foremost output: {out_dir}")
            if out:
                print(out)
            return out or ""
        else:
            print_warn("Foremost not found. Install: apt install foremost")
            return ""

    # -----------------------------------------------------------------------
    # String extraction
    # -----------------------------------------------------------------------

    def _strings(self, target: str) -> str:
        if not validate_file(target, "file"):
            return ""
        print_subsection("Strings – Printable Character Scan")

        if require_tool("strings"):
            ok, out = run_command(["strings", "-n", "6", target])
        else:
            raw = read_file_bytes(target)
            if not raw:
                return ""
            import re
            hits = re.findall(rb'[\x20-\x7e]{6,}', raw)
            out = "\n".join(h.decode('ascii', errors='replace') for h in hits)

        if out:
            lines = out.splitlines()[:100]
            print("\n".join(lines))
            if len(out.splitlines()) > 100:
                print_warn(f"… {len(out.splitlines()) - 100} more lines omitted.")
        else:
            print_warn("No printable strings found.")

        return out
