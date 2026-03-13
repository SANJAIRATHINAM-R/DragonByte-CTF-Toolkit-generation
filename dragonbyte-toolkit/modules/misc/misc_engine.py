#!/usr/bin/env python3
"""
DragonByte CTF Toolkit - Misc Module
Actions: decode, qr, strings
"""

import os
import sys
import base64
import binascii
import re

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from backend.utils import (
    print_info, print_warn, print_error, print_result,
    print_subsection, run_command, require_tool,
    validate_file, read_file_lines, read_file_bytes
)


class MiscEngine:
    """Miscellaneous CTF helpers: encoding detection/decode, QR, strings."""

    def run(self, action: str, target: str) -> str:
        if action == "decode":
            return self._decode(target)
        elif action == "qr":
            return self._qr(target)
        elif action == "strings":
            return self._strings(target)
        return ""

    # -----------------------------------------------------------------------
    # Multi-layer encoding detection and decoding
    # -----------------------------------------------------------------------

    def _decode(self, target: str) -> str:
        """Auto-detect and decode common CTF encodings from a file or string."""
        results = []

        # Determine input: file or raw string
        if target and os.path.isfile(target):
            print_info(f"Reading encoded data from: {target}")
            lines = read_file_lines(target)
            data = "\n".join(lines).strip()
        else:
            if not target:
                print_error("No encoded string or file provided.")
                return ""
            data = target.strip()

        print_info(f"Input: {data[:80]}{'…' if len(data) > 80 else ''}")
        print_subsection("Encoding Detection & Decoding")

        attempts = [
            ("Base64",       self._try_base64),
            ("Base32",       self._try_base32),
            ("Hex",          self._try_hex),
            ("ROT13",        self._try_rot13),
            ("ROT47",        self._try_rot47),
            ("Binary",       self._try_binary),
            ("URL-encoded",  self._try_url),
            ("Caesar brute", self._try_caesar_brute),
            ("Morse code",   self._try_morse),
        ]

        decoded_any = False
        for label, fn in attempts:
            decoded = fn(data)
            if decoded:
                print_result(label, decoded[:120])
                results.append(f"{label}: {decoded}")
                decoded_any = True

        if not decoded_any:
            print_warn("Could not detect encoding. Try manual analysis.")

        return "\n".join(results)

    # --- Individual decoders ---

    def _try_base64(self, data: str) -> str:
        try:
            padded = data + "=" * (4 - len(data) % 4)
            decoded = base64.b64decode(padded).decode("utf-8")
            if self._is_printable(decoded):
                return decoded
        except Exception:
            pass
        return ""

    def _try_base32(self, data: str) -> str:
        try:
            decoded = base64.b32decode(data.upper() + "=" * (8 - len(data) % 8))
            decoded = decoded.decode("utf-8")
            if self._is_printable(decoded):
                return decoded
        except Exception:
            pass
        return ""

    def _try_hex(self, data: str) -> str:
        clean = data.replace(" ", "").replace("0x", "").replace(",", "")
        try:
            decoded = bytes.fromhex(clean).decode("utf-8")
            if self._is_printable(decoded):
                return decoded
        except Exception:
            pass
        return ""

    def _try_rot13(self, data: str) -> str:
        return data.translate(str.maketrans(
            'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
            'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
        ))

    def _try_rot47(self, data: str) -> str:
        result = []
        for ch in data:
            code = ord(ch)
            if 33 <= code <= 126:
                result.append(chr(33 + (code - 33 + 47) % 94))
            else:
                result.append(ch)
        return "".join(result)

    def _try_binary(self, data: str) -> str:
        chunks = data.replace("\n", " ").split()
        if not all(re.fullmatch(r'[01]{8}', c) for c in chunks):
            return ""
        try:
            decoded = "".join(chr(int(c, 2)) for c in chunks)
            if self._is_printable(decoded):
                return decoded
        except Exception:
            pass
        return ""

    def _try_url(self, data: str) -> str:
        from urllib.parse import unquote
        decoded = unquote(data)
        return decoded if decoded != data else ""

    def _try_caesar_brute(self, data: str) -> str:
        """Return the ROT shift that produces the most English-like output."""
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        common_words = {'the', 'and', 'for', 'are', 'was', 'you', 'that',
                        'with', 'flag', 'ctf', 'key'}
        best_score, best = 0, ""
        for shift in range(1, 26):
            candidate = ""
            for ch in data:
                if ch.lower() in alphabet:
                    idx = (alphabet.index(ch.lower()) + shift) % 26
                    candidate += alphabet[idx].upper() if ch.isupper() else alphabet[idx]
                else:
                    candidate += ch
            score = sum(1 for w in candidate.lower().split() if w in common_words)
            if score > best_score:
                best_score = score
                best = f"ROT{shift}: {candidate}"
        return best if best_score > 0 else ""

    def _try_morse(self, data: str) -> str:
        MORSE = {
            ".-": "A",   "-...": "B", "-.-.": "C", "-..": "D",  ".": "E",
            "..-.": "F", "--.": "G",  "....": "H", "..": "I",   ".---": "J",
            "-.-": "K",  ".-..": "L", "--": "M",   "-.": "N",   "---": "O",
            ".--.": "P", "--.-": "Q", ".-.": "R",  "...": "S",  "-": "T",
            "..-": "U",  "...-": "V", ".--": "W",  "-..-": "X", "-.--": "Y",
            "--..": "Z", "-----": "0","----.":" 1","---..":"2","--...":"3",
            "-....":"4", ".....":"5", ".....-":"6","...--":"7","..---":"8",
            ".----":"9",
        }
        clean = re.sub(r'[^.\-/ ]', '', data).strip()
        if not re.search(r'[.\-]', clean):
            return ""
        sep = "/" if "/" in clean else "   "
        words = clean.split(sep)
        try:
            decoded = " ".join(
                "".join(MORSE.get(ch.strip(), "?") for ch in word.split())
                for word in words
            )
            return decoded if "?" not in decoded else ""
        except Exception:
            return ""

    def _is_printable(self, text: str) -> bool:
        return all(c.isprintable() or c in "\n\r\t" for c in text)

    # -----------------------------------------------------------------------
    # QR code decoding
    # -----------------------------------------------------------------------

    def _qr(self, target: str) -> str:
        if not validate_file(target, "image file"):
            return ""
        print_info(f"Decoding QR code from: {target}")

        # Try zbarimg first
        print_subsection("zbar – QR/Barcode Decoding")
        if require_tool("zbarimg"):
            ok, out = run_command(["zbarimg", "--quiet", target])
            if out:
                print_info(f"Decoded: {out}")
                return out
        else:
            print_warn("zbarimg not found. Install: apt install zbar-tools")

        # Fallback: Python Pillow + pyzbar
        try:
            from PIL import Image
            from pyzbar.pyzbar import decode as pyzbar_decode
            print_subsection("pyzbar – Python QR Decoder")
            img = Image.open(target)
            barcodes = pyzbar_decode(img)
            if barcodes:
                results = []
                for bc in barcodes:
                    data = bc.data.decode("utf-8")
                    print_result(bc.type, data)
                    results.append(data)
                return "\n".join(results)
            else:
                print_warn("No QR/barcode detected.")
        except ImportError:
            print_warn("pyzbar/Pillow not installed: pip3 install pyzbar Pillow")
        except Exception as e:
            print_error(f"QR decode error: {e}")

        return ""

    # -----------------------------------------------------------------------
    # String extraction
    # -----------------------------------------------------------------------

    def _strings(self, target: str) -> str:
        if not validate_file(target, "file"):
            return ""
        print_subsection("Strings – Printable Extraction")

        if require_tool("strings"):
            ok, out = run_command(["strings", "-n", "4", target])
        else:
            raw = read_file_bytes(target)
            if not raw:
                return ""
            hits = re.findall(rb'[\x20-\x7e]{4,}', raw)
            out = "\n".join(h.decode('ascii', errors='replace') for h in hits)

        if out:
            lines = out.splitlines()[:80]
            print("\n".join(lines))
            if len(out.splitlines()) > 80:
                print_warn(f"… {len(out.splitlines()) - 80} lines omitted.")
        else:
            print_warn("No strings found.")

        return out
