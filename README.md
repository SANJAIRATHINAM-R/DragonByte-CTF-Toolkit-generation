<div align="center">

```
██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗     ██████╗ ██╗   ██╗████████╗███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║     ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝
██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║     ██████╔╝ ╚████╔╝    ██║   █████╗  
██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║     ██╔══██╗  ╚██╔╝     ██║   ██╔══╝  
██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║     ██████╔╝   ██║      ██║   ███████╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝    ╚═╝      ╚═╝   ╚══════╝
```

# 🐉 DragonByte CTF Toolkit 
# 👤created by Sanjairathinam

**The ultimate terminal-based toolkit for CTF players & cybersecurity learners**

[![Version](https://img.shields.io/badge/version-1.0.0-cyan?style=for-the-badge)](https://github.com/SANJAIRATHINAM-R/DragonByte-CTF-Toolkit-generation)
[![Platform](https://img.shields.io/badge/platform-Kali%20Linux-557C94?style=for-the-badge&logo=linux)](https://www.kali.org/)
[![Python](https://img.shields.io/badge/python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Bash](https://img.shields.io/badge/bash-5.0%2B-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)](https://www.gnu.org/software/bash/)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![Open Source](https://img.shields.io/badge/open--source-%E2%9D%A4-brightgreen?style=for-the-badge)](https://github.com/SANJAIRATHINAM-R/DragonByte-CTF-Toolkit-generation)
[![Stars](https://img.shields.io/github/stars/SANJAIRATHINAM-R/DragonByte-CTF-Toolkit-generation?style=for-the-badge&color=yellow)](https://github.com/SANJAIRATHINAM-R/DragonByte-CTF-Toolkit-generation/stargazers)
[![Author](https://img.shields.io/badge/author-Sanjai%20Rathinam-red?style=for-the-badge)](https://github.com/SANJAIRATHINAM-R)

> *Crack hashes. Decode stego. Hunt subdomains. Analyze PCAPs. Capture every flag.*
> *All from one terminal command.*

[🚀 Quick Start](#-quick-start) •
[📦 Modules](#-modules) •
[📖 Usage](#-full-usage-reference) •
[⚙️ Installation](#️-installation) •
[👤 Author](#-author) •
[🤝 Contributing](#-contributing)

---

</div>

---

## 👤 Author

<div align="center">

<img src="https://avatars.githubusercontent.com/SANJAIRATHINAM-R" width="100" style="border-radius:50%" alt="Sanjai Rathinam"/>

### Sanjai Rathinam

**Founder of DragonByte | Cybersecurity Enthusiast | CTF Player**

> *"I create tools and resources to help beginners and enthusiasts learn ethical hacking and solve CTF challenges efficiently."*

[![GitHub](https://img.shields.io/badge/GitHub-SANJAIRATHINAM--R-181717?style=for-the-badge&logo=github)](https://github.com/SANJAIRATHINAM-R)
[![DragonByte](https://img.shields.io/badge/Project-DragonByte-cyan?style=for-the-badge&logo=dragonframe)](https://github.com/SANJAIRATHINAM-R/DragonByte-CTF-Toolkit-generation)

**DragonByte** is a community-driven cybersecurity initiative and terminal-based toolkit that integrates modules for cryptography, steganography, OSINT, web exploitation, forensics, and miscellaneous challenges — designed to simplify learning and CTF problem-solving for everyone.

</div>

---

## 🎯 What is DragonByte?

DragonByte CTF Toolkit is a **modular, open-source, terminal-based toolkit** built for
[Capture The Flag](https://ctftime.org) competitions and cybersecurity learners on Kali Linux.

Instead of juggling 10+ separate tools across different terminals, DragonByte wraps them
all into **one clean, consistent command interface** with automatic flag detection built in.

```bash
dragonbyte <module> <action> <target>
```

Whether you're cracking a hash, extracting hidden data from an image, enumerating
subdomains, or analysing a packet capture — DragonByte has you covered.

---

## ✨ Key Features

|  | Feature | Description |
|--|---------|-------------|
| 🧩 | **6 Specialist Modules** | Crypto, Stego, OSINT, Web, Forensics, Misc |
| 🚩 | **Auto Flag Detection** | Scans every output for `flag{...}`, `HTB{...}`, `picoCTF{...}` and more |
| 🔧 | **20+ Tool Integrations** | Hashcat, John, Binwalk, SQLmap, tshark, Gobuster, Volatility & more |
| 🐍 | **Hybrid Architecture** | Bash CLI frontend + Python backend engine |
| 📦 | **One-Command Install** | `sudo bash install.sh` handles every dependency |
| 🔌 | **Easily Extensible** | Add new modules in minutes with a simple class interface |
| 🎨 | **Professional Output** | Colour-coded, well-formatted terminal output every time |
| 🛡️ | **Graceful Degradation** | Missing tools are reported cleanly — the rest still runs |

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/SANJAIRATHINAM-R/DragonByte-CTF-Toolkit-generation.git

# 2. Enter the directory
cd DragonByte-CTF-Toolkit-generation

# 3. Run the installer (installs all tools & dependencies)
sudo bash install.sh

# 4. You're ready!
dragonbyte --help
```

### ⚡ One-liner Install

```bash
git clone https://github.com/SANJAIRATHINAM-R/DragonByte-CTF-Toolkit-generation.git && cd DragonByte-CTF-Toolkit-generation && sudo bash install.sh
```

### 🧪 Instant Test (no files needed)

```bash
dragonbyte misc decode "ZmxhZ3t3ZWxjb21lX3RvX2RyYWdvbmJ5dGV9"
```

Expected output:
```
──────────────────────────────────────────────────────────────
  Module: Misc | Action: decode
──────────────────────────────────────────────────────────────

[>] Encoding Detection & Decoding
········································
  Base64               flag{welcome_to_dragonbyte}

──────────────────────────────────────
[🚩] FLAG(S) DETECTED!
──────────────────────────────────────
  flag{welcome_to_dragonbyte}
──────────────────────────────────────
```

---

## 📦 Modules

### 🔐 `crypto` — Hash Cracking & Identification

Automatically detect hash algorithms and launch dictionary attacks.

```bash
# Identify a single hash
dragonbyte crypto identify 5f4dcc3b5aa765d61d8327deb882cf99

# Identify hashes from a file
dragonbyte crypto identify hashes.txt

# Crack hashes (John the Ripper + Hashcat + rockyou.txt)
dragonbyte crypto crack hashes.txt
```

**Supported hash formats:**

| Hash | Length | Example |
|------|--------|---------|
| MD5 | 32 chars | `5f4dcc3b5aa765d61d8327deb882cf99` |
| SHA-1 | 40 chars | `5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8` |
| SHA-256 | 64 chars | `...` |
| SHA-512 | 128 chars | `...` |
| bcrypt | starts `$2b$` | `$2b$12$...` |
| SHA-512 crypt | starts `$6$` | `$6$salt$...` |

**Tools:** `john` · `hashcat`

---

### 🖼️ `stego` — Steganography Analysis

Reveal data hidden inside images and binary files.

```bash
# Full scan — metadata + embedded data + strings
dragonbyte stego scan challenge.png

# Extract hidden payloads and embedded archives
dragonbyte stego extract challenge.png

# Dump all printable strings
dragonbyte stego strings challenge.png
```

**What the scan does:**

```
[1] ExifTool  → metadata (GPS, comments, author, software)
[2] Binwalk   → embedded files, compressed archives, signatures
[3] Steghide  → hidden payload check (no-password attempt)
[4] strings   → printable character extraction
[5] Flag scan → auto-highlight any CTF flags found
```

**Tools:** `exiftool` · `binwalk` · `steghide` · `strings`

---

### 🌐 `osint` — Reconnaissance & Intelligence

Gather open-source intelligence on domains and organisations.

```bash
# Full domain recon — DNS, WHOIS, emails, ports
dragonbyte osint domain example.com

# Email address harvesting
dragonbyte osint email example.com

# Subdomain enumeration
dragonbyte osint subdomains example.com
```

**Domain action pipeline:**

```
[1] DNS Resolution   → resolve IPs
[2] WHOIS            → registrar, owner, dates
[3] theHarvester     → emails, hosts, names
[4] Nmap             → open ports (fast scan)
```

**Subdomain pipeline:**

```
[1] Amass      → passive subdomain enumeration
[2] Gobuster   → DNS brute-force with wordlist
```

**Tools:** `whois` · `nmap` · `theHarvester` · `amass` · `gobuster`

---

### 🕷️ `web` — Web Vulnerability Testing

Find hidden directories, injection points, and security misconfigurations.

```bash
# Full scan — directories + Nikto
dragonbyte web scan http://target.htb

# SQL injection testing
dragonbyte web sqli "http://target.htb/login?id=1"

# HTTP header analysis + security audit
dragonbyte web headers http://target.htb
```

**Security headers audited:**

| Header | Checks |
|--------|--------|
| `X-Frame-Options` | Clickjacking protection |
| `X-XSS-Protection` | XSS filter |
| `Strict-Transport-Security` | HSTS enforcement |
| `Content-Security-Policy` | CSP presence |
| `X-Content-Type-Options` | MIME sniffing |

**Tools:** `gobuster` · `nikto` · `sqlmap`

---

### 🔬 `forensic` — Digital Forensics

Analyse packet captures, disk images, memory dumps, and binary files.

```bash
# Auto-detect file type and analyse
dragonbyte forensic analyze capture.pcap
dragonbyte forensic analyze disk.img
dragonbyte forensic analyze memory.vmem
dragonbyte forensic analyze unknown.bin

# Carve embedded files
dragonbyte forensic extract challenge.bin

# Extract strings
dragonbyte forensic strings challenge.bin
```

**Auto-routing by file extension:**

| Extension | Engine | What it does |
|-----------|--------|--------------|
| `.pcap` `.pcapng` `.cap` | tshark | Protocol stats, HTTP objects, DNS queries, conversations |
| `.img` `.dd` `.bin` `.raw` | Foremost | File carving from disk images |
| `.vmem` `.mem` `.dmp` | Volatility 3 | Process list, memory analysis |
| *(anything else)* | file + strings | Magic detection + string extraction |

**Tools:** `tshark` · `foremost` · `binwalk` · `volatility3` · `file`

---

### 🎲 `misc` — Encoding Detection & Decoding

Stop guessing encodings manually. DragonByte tries them all at once.

```bash
# Auto-detect and decode any encoding
dragonbyte misc decode "aGVsbG8gY3Rm"
dragonbyte misc decode encoded.txt

# Decode QR codes and barcodes from images
dragonbyte misc qr qrcode.png

# Extract readable strings
dragonbyte misc strings file.bin
```

**Encodings tried automatically:**

| Encoding | Example Input |
|----------|--------------|
| Base64 | `aGVsbG8=` |
| Base32 | `NBSWY3DPEB3W64TMMQ======` |
| Hex | `68656c6c6f` |
| ROT13 | `uryyb` |
| ROT47 | `96==@` |
| Binary | `01101000 01100101 01101100` |
| URL encoding | `%68%65%6c%6c%6f` |
| Morse code | `.... . .-.. .-.. ---` |
| Caesar brute-force | All 25 shifts scored |

**Tools:** `zbarimg` · `pyzbar` · `strings`

---

## 🚩 Flag Detection Engine

Every single module run is **automatically scanned** for CTF flags.
When a flag is found, a highlighted banner is printed:

```
──────────────────────────────────────────────────
[🚩] FLAG(S) DETECTED!
──────────────────────────────────────────────────
  flag{hidden_in_plain_sight}
──────────────────────────────────────────────────
```

**All supported flag formats:**

```
flag{...}        picoCTF{...}      HTB{...}
CTF{...}         THM{...}          DUCTF{...}
rtcp{...}        darkCTF{...}      TBTL{...}
DawgCTF{...}     WORD{...}  ← any ALL-CAPS prefix
```

---

## ⚙️ Installation

### System Requirements

| Requirement | Minimum |
|------------|---------|
| OS | Kali Linux 2022+ (or Debian-based) |
| Python | 3.8+ |
| Privileges | sudo / root |
| Disk space | ~500 MB (tools + wordlists) |

### Step-by-Step

```bash
# Clone
git clone https://github.com/SANJAIRATHINAM-R/DragonByte-CTF-Toolkit-generation.git
cd DragonByte-CTF-Toolkit-generation

# Install
sudo bash install.sh

# Verify
dragonbyte --version
dragonbyte --help
```

### What the Installer Does

```
[1] Checks Python 3 and pip3
[2] Installs Python packages (requests, Pillow, pyzbar, colorama, volatility3)
[3] Installs system tools via apt:
      exiftool  binwalk    steghide   tshark     foremost
      nmap      gobuster   sqlmap     nikto      john
      hashcat   amass      theharvester  whois   zbar-tools
[4] Decompresses rockyou.txt if gzipped
[5] Creates /usr/local/bin/dragonbyte symlink
[6] Creates all Python package __init__.py files
```

### Manual Symlink (if needed)

```bash
sudo ln -sf ~/DragonByte-CTF-Toolkit-generation/dragonbyte.sh /usr/local/bin/dragonbyte
```

### Run Without Installing

```bash
cd DragonByte-CTF-Toolkit-generation
bash dragonbyte.sh --help
bash dragonbyte.sh misc decode "aGVsbG8="
```

---

## 📁 Project Structure

```
DragonByte-CTF-Toolkit-generation/
│
├── 🐚 dragonbyte.sh                  ← Bash CLI: parses args, calls Python
├── 🔧 install.sh                     ← Installs all tools & dependencies
├── 📄 README.md
│
├── backend/
│   ├── engine.py                     ← Validates input, routes to modules
│   ├── flag_detector.py              ← Regex scanner for CTF flag patterns
│   └── utils.py                      ← print_info/warn/error, run_command,
│                                        validate_file, tool_available, etc.
│
├── modules/
│   ├── crypto/
│   │   └── crypto_engine.py          ← Hash ID + John/Hashcat cracking
│   ├── stego/
│   │   └── stego_engine.py           ← ExifTool + Binwalk + Steghide
│   ├── osint/
│   │   └── osint_engine.py           ← WHOIS + theHarvester + Amass
│   ├── web/
│   │   └── web_engine.py             ← Gobuster + Nikto + SQLmap
│   ├── forensics/
│   │   └── forensic_engine.py        ← tshark + Foremost + Volatility
│   └── misc/
│       └── misc_engine.py            ← Multi-encoding decoder + QR
│
├── wordlists/                        ← Drop custom wordlists here
│   └── (rockyou.txt auto-detected)
│
└── docs/
    ├── installation.md
    ├── usage.md
    └── modules.md
```

---

## 📖 Full Usage Reference

```
USAGE:
  dragonbyte <module> <action> [target]

MODULES:
  crypto    identify <hash|file>        Detect hash algorithm by pattern
            crack    <hashfile>         Dictionary attack via John + Hashcat

  stego     scan     <file>             Full scan: meta + binwalk + steghide
            extract  <file>             Extract hidden payloads
            strings  <file>             Dump printable strings

  osint     domain   <domain>           DNS + WHOIS + harvest + nmap
            email    <domain>           Harvest email addresses
            subdomains <domain>         Amass + Gobuster DNS enum

  web       scan     <url>              Gobuster dir scan + Nikto
            sqli     <url>              SQLmap injection test
            headers  <url>              HTTP headers + security audit

  forensic  analyze  <file>             Auto-detect & analyse
            extract  <file>             Carve files (Foremost + Binwalk)
            strings  <file>             Extract strings

  misc      decode   <string|file>      Auto-detect & decode encoding
            qr       <imagefile>        Decode QR code / barcode
            strings  <file>             Extract printable strings

GLOBAL FLAGS:
  --help, -h          Show help
  --version, -v       Show version
```

---

## 💡 Real CTF Scenarios

```bash
# ── Challenge: suspicious PNG ──────────────────────────────────
dragonbyte stego scan challenge.png
# ExifTool → Binwalk → Steghide → strings → flag scan

# ── Challenge: crack this hash ─────────────────────────────────
echo "482c811da5d5b4bc6d497ffa98491e38" > hash.txt
dragonbyte crypto crack hash.txt
# MD5 identified → John + Hashcat → password123

# ── Challenge: weird encoded string ────────────────────────────
dragonbyte misc decode ".... - -... . . . ---. ..... "
# Morse code detected → HTB{...}

# ── Challenge: web login page ──────────────────────────────────
dragonbyte web sqli "http://challenge.ctf.io/login?user=test"
# SQLmap → vulnerable parameter found → DB dumped

# ── Challenge: pcap analysis ───────────────────────────────────
dragonbyte forensic analyze traffic.pcapng
# tshark → HTTP objects → flag in plaintext

# ── Challenge: CTF recon ───────────────────────────────────────
dragonbyte osint domain target.ctf.com
# DNS → WHOIS → subdomains → open ports
```

---

## 🔌 Adding a New Module

DragonByte is designed to be extended. Adding a new module takes 4 steps:

**1. Create the engine file:**
```python
# modules/pwn/pwn_engine.py
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from backend.utils import print_info, print_subsection

class PwnEngine:
    def run(self, action: str, target: str) -> str:
        if action == "checksec":
            return self._checksec(target)
        return ""

    def _checksec(self, target: str) -> str:
        print_subsection("checksec")
        # your logic here
        return "result"
```

**2. Add `__init__.py`:**
```bash
touch modules/pwn/__init__.py
```

**3. Register in `backend/engine.py`:**
```python
MODULE_ACTIONS = {
    ...
    "pwn": ["checksec", "rop"],   # add this line
}

def load_module(module_name):
    ...
    elif module_name == "pwn":
        from modules.pwn.pwn_engine import PwnEngine
        return PwnEngine()
```

**4. Use it:**
```bash
dragonbyte pwn checksec ./binary
```

---

## 🛠️ Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| `dragonbyte: command not found` | Symlink missing | `sudo ln -sf ~/DragonByte-CTF-Toolkit-generation/dragonbyte.sh /usr/local/bin/dragonbyte` |
| `install.sh: No such file or directory` | Wrong directory | `cd DragonByte-CTF-Toolkit-generation` first |
| `python3 not found` | Python not installed | `sudo apt install python3` |
| `ModuleNotFoundError` | Python package missing | `sudo bash install.sh` again |
| Tool shows `[!] not found` | Tool not installed | `sudo apt install <toolname>` |
| `Permission denied` | Script not executable | `chmod +x dragonbyte.sh` |
| Hashcat `--force` errors | VM / no GPU | Normal on VMs, results still work |

---

## 🗺️ Roadmap

- [ ] PWN module (checksec, ROPgadget, pwntools integration)
- [ ] Reverse engineering module (Ghidra CLI, strings, ltrace/strace)
- [ ] Cloud OSINT (S3 buckets, Azure blobs, GCP storage)
- [ ] Password mutation engine in crypto module
- [ ] Output save to file (`--output report.txt`)
- [ ] Docker container for portable use
- [ ] CTF platform integration (HTB API, TryHackMe API)
- [ ] Web UI dashboard (optional)

---

## 🤝 Contributing

All contributions are welcome — new modules, bug fixes, better wordlists, docs.

```bash
# Fork on GitHub, then:
git clone https://github.com/SANJAIRATHINAM-R/DragonByte-CTF-Toolkit-generation.git
cd DragonByte-CTF-Toolkit-generation
git checkout -b feature/your-feature-name

# Make changes, test them, then:
git add .
git commit -m "feat: describe your change"
git push origin feature/your-feature-name
# Open a Pull Request
```

**Contribution ideas:**
- New encoding types in `misc`
- Additional OSINT sources
- Better hash identification patterns
- More CTF flag regex patterns
- Improve Volatility integration
- Add progress bars for long-running tools

---

## 📄 License

```
MIT License

Copyright (c) 2026 Sanjairathinam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## ⚠️ Legal Disclaimer

> **DragonByte CTF Toolkit is intended for LEGAL USE ONLY.**
>
> Use this toolkit only in:
> - CTF competitions
> - Authorised penetration testing engagements
> - Your own lab / test environments
> - Cybersecurity education and research
>
> **Do NOT** use against any system you do not own or have explicit written
> permission to test. The authors accept no liability for misuse.

---

<div align="center">

---

### 🐉 Built for CTF players, by CTF players

*Created with ❤️ by **[Sanjairathinam](https://github.com/SANJAIRATHINAM-R)** — Founder of DragonByte*

*If DragonByte helped you capture a flag, give it a ⭐ on GitHub!*

**Happy hacking — legally.** 🔐

---

[![GitHub stars](https://img.shields.io/github/stars/SANJAIRATHINAM-R/DragonByte-CTF-Toolkit-generation?style=social)](https://github.com/SANJAIRATHINAM-R/DragonByte-CTF-Toolkit-generation)
[![GitHub forks](https://img.shields.io/github/forks/SANJAIRATHINAM-R/DragonByte-CTF-Toolkit-generation?style=social)](https://github.com/SANJAIRATHINAM-R/DragonByte-CTF-Toolkit-generation/fork)
[![GitHub issues](https://img.shields.io/github/issues/SANJAIRATHINAM-R/DragonByte-CTF-Toolkit-generation?style=social)](https://github.com/SANJAIRATHINAM-R/DragonByte-CTF-Toolkit-generation/issues)

</div>
