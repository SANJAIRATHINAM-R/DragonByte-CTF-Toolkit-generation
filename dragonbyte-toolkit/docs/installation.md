# Installation Guide – DragonByte CTF Toolkit

## Requirements

- Kali Linux (recommended) or any Debian-based Linux distro
- Python 3.8+
- sudo / root privileges for tool installation

---

## Quick Install

```bash
git clone https://github.com/youruser/dragonbyte-toolkit.git
cd dragonbyte-toolkit
sudo bash install.sh
```

After installation, the `dragonbyte` command will be available system-wide.

---

## What the Installer Does

1. Checks Python 3 and pip3 availability
2. Installs Python packages: `requests`, `Pillow`, `pyzbar`, `python-magic`, `colorama`
3. Installs Kali/Debian system tools via apt:
   - `exiftool`, `binwalk`, `steghide` – steganography
   - `tshark`, `foremost` – forensics
   - `nmap`, `gobuster`, `sqlmap`, `nikto` – web/network
   - `john`, `hashcat` – crypto / password cracking
   - `amass`, `theharvester`, `whois` – OSINT
   - `zbar-tools` – QR code decoding
4. Installs Volatility 3 via pip3 (memory forensics)
5. Decompresses rockyou.txt wordlist if gzipped
6. Creates `/usr/local/bin/dragonbyte` symlink

---

## Manual Dependency Install

If the automated installer fails for a specific tool:

```bash
# Kali / Debian
sudo apt install exiftool binwalk steghide tshark foremost nmap \
    gobuster sqlmap nikto john hashcat amass theharvester zbar-tools

# Python packages
pip3 install requests Pillow pyzbar python-magic colorama volatility3
```

---

## Wordlists

Place wordlists in the `wordlists/` directory or ensure Kali's default
paths are available:

- `/usr/share/wordlists/rockyou.txt`
- `/usr/share/wordlists/dirb/common.txt`
- `/usr/share/seclists/` (optional, from `apt install seclists`)

---

## Verify Installation

```bash
dragonbyte --version
dragonbyte --help
```
