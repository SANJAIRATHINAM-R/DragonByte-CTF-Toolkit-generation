#!/usr/bin/env bash
# =============================================================================
# DragonByte CTF Toolkit - Installer
# Supports Kali Linux / Debian-based systems
# =============================================================================

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
BOLD='\033[1m'
RESET='\033[0m'

info()  { echo -e "${GREEN}[+]${RESET} $1"; }
warn()  { echo -e "${YELLOW}[!]${RESET} $1"; }
error() { echo -e "${RED}[✗]${RESET} $1"; exit 1; }
step()  { echo -e "\n${BOLD}${CYAN}──────────────────────────────────────${RESET}"; echo -e "${BOLD}${CYAN}  $1${RESET}"; echo -e "${BOLD}${CYAN}──────────────────────────────────────${RESET}"; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${CYAN}${BOLD}"
echo "  DragonByte CTF Toolkit – Installer"
echo "  Target: Kali Linux / Debian"
echo -e "${RESET}"

# ── Root check ────────────────────────────────────────────────────────────────
if [ "$EUID" -ne 0 ]; then
    warn "Not running as root. Some apt installs may fail."
    warn "Re-run with: sudo bash install.sh"
fi

# ── Python check ──────────────────────────────────────────────────────────────
step "Checking Python 3"
if command -v python3 &>/dev/null; then
    PY_VER=$(python3 --version)
    info "Found $PY_VER"
else
    error "Python 3 not found. Install it: apt install python3"
fi

# ── Pip check ─────────────────────────────────────────────────────────────────
step "Checking pip3"
if ! command -v pip3 &>/dev/null; then
    warn "pip3 not found. Attempting install..."
    apt-get install -y python3-pip || warn "Could not install pip3 automatically."
fi

# ── Python dependencies ───────────────────────────────────────────────────────
step "Installing Python dependencies"
pip3 install --quiet --upgrade \
    requests \
    Pillow \
    pyzbar \
    python-magic \
    colorama \
    2>/dev/null && info "Python packages installed." || warn "Some Python packages failed to install."

# ── Kali/Debian apt tools ─────────────────────────────────────────────────────
step "Installing system tools via apt"

APT_TOOLS=(
    exiftool
    binwalk
    steghide
    tshark
    foremost
    nmap
    gobuster
    sqlmap
    nikto
    john
    hashcat
    amass
    theharvester
    whois
    zbar-tools
    strings
)

for tool in "${APT_TOOLS[@]}"; do
    if dpkg -s "$tool" &>/dev/null 2>&1; then
        info "  ✓ $tool already installed"
    else
        info "  Installing $tool..."
        apt-get install -y "$tool" &>/dev/null \
            && info "  ✓ $tool installed" \
            || warn "  ✗ Could not install $tool (may require manual install)"
    fi
done

# ── Volatility 3 ──────────────────────────────────────────────────────────────
step "Checking Volatility 3"
if command -v vol &>/dev/null || command -v volatility &>/dev/null; then
    info "Volatility already available."
else
    warn "Volatility not found. Installing via pip3..."
    pip3 install --quiet volatility3 2>/dev/null \
        && info "Volatility 3 installed." \
        || warn "Volatility install failed. Manual install: pip3 install volatility3"
fi

# ── wordlists ─────────────────────────────────────────────────────────────────
step "Setting up wordlists"
WORDLIST_DIR="$SCRIPT_DIR/wordlists"
mkdir -p "$WORDLIST_DIR"

if [ -f /usr/share/wordlists/rockyou.txt.gz ] && [ ! -f /usr/share/wordlists/rockyou.txt ]; then
    info "Decompressing rockyou.txt..."
    gunzip /usr/share/wordlists/rockyou.txt.gz && info "Done."
fi

if [ -f /usr/share/wordlists/rockyou.txt ]; then
    info "rockyou.txt found at /usr/share/wordlists/rockyou.txt"
else
    warn "rockyou.txt not found. Place it at /usr/share/wordlists/rockyou.txt"
fi

# ── Make dragonbyte executable & install to PATH ───────────────────────────────
step "Installing dragonbyte command"
chmod +x "$SCRIPT_DIR/dragonbyte.sh"

if [ -d /usr/local/bin ]; then
    ln -sf "$SCRIPT_DIR/dragonbyte.sh" /usr/local/bin/dragonbyte \
        && info "Installed: dragonbyte → /usr/local/bin/dragonbyte" \
        || warn "Could not create symlink. Add manually: ln -s $SCRIPT_DIR/dragonbyte.sh /usr/local/bin/dragonbyte"
fi

# ── Module __init__.py files ───────────────────────────────────────────────────
step "Creating package init files"
for dir in backend modules modules/crypto modules/stego modules/osint modules/web modules/forensics modules/misc; do
    touch "$SCRIPT_DIR/$dir/__init__.py"
done
info "Package structure initialized."

# ── Final check ───────────────────────────────────────────────────────────────
step "Installation complete"
echo ""
info "Run the toolkit with:"
echo ""
echo -e "  ${CYAN}dragonbyte --help${RESET}"
echo ""
echo -e "  ${CYAN}dragonbyte crypto crack hash.txt${RESET}"
echo -e "  ${CYAN}dragonbyte stego scan image.jpg${RESET}"
echo -e "  ${CYAN}dragonbyte misc decode encoded.txt${RESET}"
echo ""
