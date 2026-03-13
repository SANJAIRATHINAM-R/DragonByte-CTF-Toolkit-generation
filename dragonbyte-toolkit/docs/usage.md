# Usage Guide – DragonByte CTF Toolkit

## Command Format

```
dragonbyte <module> <action> [target]
```

---

## Global Flags

| Flag | Description |
|------|-------------|
| `--help` / `-h` | Show help and module list |
| `--version` / `-v` | Show version |

---

## Module Quick Reference

### 🔐 crypto – Hash Cracking

```bash
# Identify hash type from string
dragonbyte crypto identify 5f4dcc3b5aa765d61d8327deb882cf99

# Identify hashes from a file
dragonbyte crypto identify hashes.txt

# Crack hashes in a file (uses John + Hashcat)
dragonbyte crypto crack hashes.txt
```

---

### 🖼️ stego – Steganography

```bash
# Full scan: metadata + binwalk + steghide check + strings
dragonbyte stego scan challenge.png

# Extract hidden files / payloads
dragonbyte stego extract challenge.png

# Dump printable strings
dragonbyte stego strings challenge.png
```

---

### 🌐 osint – Reconnaissance

```bash
# Full domain intelligence: DNS, WHOIS, theHarvester, nmap
dragonbyte osint domain example.com

# Email harvesting
dragonbyte osint email example.com

# Subdomain enumeration (Amass + Gobuster DNS)
dragonbyte osint subdomains example.com
```

---

### 🕷️ web – Web Vulnerability Testing

```bash
# Full web scan: headers + gobuster + nikto
dragonbyte web scan http://target.htb

# SQL injection test
dragonbyte web sqli "http://target.htb/page?id=1"

# Inspect HTTP headers & security posture
dragonbyte web headers http://target.htb
```

---

### 🔬 forensic – Digital Forensics

```bash
# Auto-detect and analyze: pcap, disk image, memory dump, or generic file
dragonbyte forensic analyze capture.pcap
dragonbyte forensic analyze disk.img
dragonbyte forensic analyze memory.vmem

# Carve files (Foremost + Binwalk)
dragonbyte forensic extract challenge.bin

# Dump strings
dragonbyte forensic strings challenge.bin
```

---

### 🎲 misc – Miscellaneous Decoding

```bash
# Auto-detect and decode (Base64, Hex, ROT13, ROT47, Binary, Morse, Caesar…)
dragonbyte misc decode encoded.txt
dragonbyte misc decode "aGVsbG8gd29ybGQ="

# Decode QR code / barcode from an image
dragonbyte misc qr qrcode.png

# Extract strings from any file
dragonbyte misc strings challenge.dat
```

---

## Flag Detection

The toolkit automatically scans all output for CTF flags. Supported patterns:

- `flag{...}`
- `picoCTF{...}`
- `HTB{...}`
- `THM{...}`
- `CTF{...}`
- Any `WORD{...}` pattern

Detected flags are highlighted in bright green with a banner.

---

## Tips

- If a tool is missing, the toolkit will warn you and suggest the apt package.
- Most modules work best on Kali Linux where all tools are pre-available.
- Add your custom wordlists to the `wordlists/` directory.
