#!/usr/bin/env bash
# =============================================================================
# DragonByte CTF Toolkit - Main CLI Entry Point
# Usage: dragonbyte <module> <action> <target>
# =============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND="$SCRIPT_DIR/backend/engine.py"

# ANSI color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
RESET='\033[0m'

print_banner() {
    echo -e "${CYAN}${BOLD}"
    echo "  ██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗██████╗ ██╗   ██╗████████╗███████╗"
    echo "  ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝"
    echo "  ██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║██████╔╝ ╚████╔╝    ██║   █████╗  "
    echo "  ██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══██╗  ╚██╔╝     ██║   ██╔══╝  "
    echo "  ██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝   ██║      ██║   ███████╗"
    echo "  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝    ╚═╝      ╚═╝   ╚══════╝"
    echo -e "${RESET}"
    echo -e "${GREEN}  CTF Toolkit v1.0  |  Cybersecurity & CTF Challenge Solver${RESET}"
    echo -e "${YELLOW}  ─────────────────────────────────────────────────────────${RESET}"
    echo ""
}

print_help() {
    print_banner
    echo -e "${BOLD}USAGE:${RESET}"
    echo -e "  dragonbyte ${CYAN}<module>${RESET} ${GREEN}<action>${RESET} ${YELLOW}<target>${RESET}"
    echo ""
    echo -e "${BOLD}MODULES:${RESET}"
    echo -e "  ${CYAN}crypto${RESET}    crack, identify                  Hash cracking & identification"
    echo -e "  ${CYAN}stego${RESET}     scan, extract, strings           Steganography analysis"
    echo -e "  ${CYAN}osint${RESET}     domain, email, subdomains        OSINT & reconnaissance"
    echo -e "  ${CYAN}web${RESET}       scan, sqli, headers              Web vulnerability testing"
    echo -e "  ${CYAN}forensic${RESET}  analyze, extract, strings        Digital forensics"
    echo -e "  ${CYAN}misc${RESET}      decode, qr, strings              Miscellaneous decoding"
    echo ""
    echo -e "${BOLD}EXAMPLES:${RESET}"
    echo -e "  dragonbyte crypto crack hash.txt"
    echo -e "  dragonbyte stego scan image.jpg"
    echo -e "  dragonbyte osint domain example.com"
    echo -e "  dragonbyte web scan http://target.com"
    echo -e "  dragonbyte forensic analyze capture.pcap"
    echo -e "  dragonbyte misc decode encoded.txt"
    echo ""
}

# No arguments → show help
if [ $# -eq 0 ]; then
    print_help
    exit 0
fi

# Help flags
if [[ "$1" == "-h" || "$1" == "--help" || "$1" == "help" ]]; then
    print_help
    exit 0
fi

# Version flag
if [[ "$1" == "-v" || "$1" == "--version" ]]; then
    echo -e "${GREEN}DragonByte CTF Toolkit v1.0${RESET}"
    exit 0
fi

# Validate module argument
MODULE="$1"
VALID_MODULES=("crypto" "stego" "osint" "web" "forensic" "misc")
VALID=false
for m in "${VALID_MODULES[@]}"; do
    if [[ "$m" == "$MODULE" ]]; then
        VALID=true
        break
    fi
done

if [ "$VALID" = false ]; then
    echo -e "${RED}[!] Unknown module: '$MODULE'${RESET}"
    echo -e "${YELLOW}[*] Valid modules: crypto, stego, osint, web, forensic, misc${RESET}"
    exit 1
fi

# Check Python3 is available
if ! command -v python3 &>/dev/null; then
    echo -e "${RED}[!] python3 not found. Please run install.sh first.${RESET}"
    exit 1
fi

# Check backend exists
if [ ! -f "$BACKEND" ]; then
    echo -e "${RED}[!] Backend engine not found at: $BACKEND${RESET}"
    exit 1
fi

print_banner

# Pass all arguments to the Python backend
python3 "$BACKEND" "$@"
EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    echo -e "\n${RED}[!] Toolkit exited with errors (code $EXIT_CODE)${RESET}"
fi

exit $EXIT_CODE
