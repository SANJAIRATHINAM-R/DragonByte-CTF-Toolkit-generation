# Modules Reference – DragonByte CTF Toolkit

## Architecture

```
dragonbyte.sh          ← Bash CLI entry point
└── backend/
    ├── engine.py       ← Routes commands to modules
    ├── flag_detector.py← Scans output for CTF flags
    └── utils.py        ← Shared utilities

modules/
├── crypto/crypto_engine.py
├── stego/stego_engine.py
├── osint/osint_engine.py
├── web/web_engine.py
├── forensics/forensic_engine.py
└── misc/misc_engine.py
```

---

## crypto

**File:** `modules/crypto/crypto_engine.py`

| Action | Description | Tools Used |
|--------|-------------|------------|
| `identify` | Detect hash algorithm by pattern matching | built-in regex |
| `crack` | Crack hashes via dictionary attack | John the Ripper, Hashcat |

Supports: MD5, SHA-1/224/256/384/512, bcrypt, SHA-512 crypt, CRC-32, Base64, Tiger.

---

## stego

**File:** `modules/stego/stego_engine.py`

| Action | Description | Tools Used |
|--------|-------------|------------|
| `scan` | Full scan: metadata, binwalk, steghide, strings | ExifTool, Binwalk, Steghide |
| `extract` | Extract embedded files/payloads | Binwalk, Steghide |
| `strings` | Dump printable strings (≥4 chars) | strings, Python fallback |

---

## osint

**File:** `modules/osint/osint_engine.py`

| Action | Description | Tools Used |
|--------|-------------|------------|
| `domain` | DNS, WHOIS, email harvest, port scan | whois, theHarvester, nmap |
| `email` | Harvest email addresses for a domain | theHarvester |
| `subdomains` | Enumerate subdomains | Amass, Gobuster DNS |

---

## web

**File:** `modules/web/web_engine.py`

| Action | Description | Tools Used |
|--------|-------------|------------|
| `scan` | Dir brute-force + Nikto scan | Gobuster, Nikto |
| `sqli` | SQL injection testing | SQLmap |
| `headers` | HTTP header analysis + security audit | Python urllib |

---

## forensic

**File:** `modules/forensics/forensic_engine.py`

| Action | Description | Tools Used |
|--------|-------------|------------|
| `analyze` | Auto-detect file type and analyze | tshark, file, Volatility |
| `extract` | Carve embedded files | Foremost, Binwalk |
| `strings` | Dump strings (≥6 chars) | strings, Python fallback |

Auto-routing by extension:
- `.pcap`/`.pcapng` → tshark analysis
- `.img`/`.dd`/`.bin` → disk carving
- `.vmem`/`.mem`/`.dmp` → Volatility memory analysis

---

## misc

**File:** `modules/misc/misc_engine.py`

| Action | Description | Tools Used |
|--------|-------------|------------|
| `decode` | Auto-detect & decode encodings | built-in |
| `qr` | Decode QR / barcodes | zbarimg, pyzbar |
| `strings` | Extract printable strings | strings, Python fallback |

Supported encodings: Base64, Base32, Hex, ROT13, ROT47, Binary, URL-encoding, Caesar brute-force, Morse code.

---

## flag_detector

**File:** `backend/flag_detector.py`

Automatically called after every module run. Scans output for patterns like
`flag{...}`, `picoCTF{...}`, `HTB{...}`, etc. and prints a highlighted banner.

---

## Adding a New Module

1. Create `modules/newmod/newmod_engine.py` with a class `NewmodEngine`
2. Implement `run(self, action: str, target: str) -> str`
3. Register it in `backend/engine.py` → `MODULE_ACTIONS` dict and `load_module()`
4. Add a `__init__.py` to the new directory
