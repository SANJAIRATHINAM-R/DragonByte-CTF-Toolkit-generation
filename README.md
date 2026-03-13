# 🐉 DragonByte CTF Toolkit

A modular, terminal-based toolkit for CTF players and cybersecurity learners.
Runs on Kali Linux with a Bash CLI front-end and Python backend engine.

```
  ██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗██████╗ ██╗   ██╗████████╗███████╗
  ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝
  ██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║██████╔╝ ╚████╔╝    ██║   █████╗  
  ██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══██╗  ╚██╔╝     ██║   ██╔══╝  
  ██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝   ██║      ██║   ███████╗
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝    ╚═╝      ╚═╝   ╚══════╝
```

## Modules

| Module | Actions | Purpose |
|--------|---------|---------|
| `crypto` | `crack`, `identify` | Hash detection & cracking |
| `stego` | `scan`, `extract`, `strings` | Steganography analysis |
| `osint` | `domain`, `email`, `subdomains` | Reconnaissance |
| `web` | `scan`, `sqli`, `headers` | Web vulnerability testing |
| `forensic` | `analyze`, `extract`, `strings` | Digital forensics |
| `misc` | `decode`, `qr`, `strings` | Encoding/decoding |

## Quick Start

```bash
sudo bash install.sh
dragonbyte --help
```

## Example Commands

```bash
dragonbyte crypto crack hashes.txt
dragonbyte stego scan challenge.png
dragonbyte osint domain example.com
dragonbyte web scan http://target.htb
dragonbyte forensic analyze capture.pcap
dragonbyte misc decode "aGVsbG8gY3Rm"
```

## Docs

- [Installation](docs/installation.md)
- [Usage](docs/usage.md)
- [Module Reference](docs/modules.md)

## License

MIT — open-source, free to use and extend.
