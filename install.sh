#!/bin/bash

# King Phisher v3.0.0 - Unix/Linux Installation Script
# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${PURPLE}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║     👑 KING PHISHER v3.0.0 - INSTALLATION SCRIPT           ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Check if running as root
if [[ $EUID -eq 0 ]]; then
   echo -e "${YELLOW}⚠️  Running as root. Some features may have reduced security.${NC}"
fi

# Detect OS
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if [ -f /etc/debian_version ]; then
            OS="debian"
        elif [ -f /etc/redhat-release ]; then
            OS="redhat"
        elif [ -f /etc/arch-release ]; then
            OS="arch"
        elif [ -f /etc/alpine-release ]; then
            OS="alpine"
        else
            OS="linux"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    else
        OS="unknown"
    fi
    echo -e "${GREEN}✅ Detected OS: ${OS}${NC}"
}

# Install dependencies based on OS
install_dependencies() {
    echo -e "${BLUE}📦 Installing system dependencies...${NC}"
    
    case $OS in
        debian)
            sudo apt-get update
            sudo apt-get install -y \
                python3 python3-pip python3-dev python3-venv \
                nmap nikto curl wget \
                tcpdump wireshark-cli \
                net-tools iproute2 iptables \
                arp-scan dnsutils traceroute whois \
                openssh-client sshpass \
                build-essential libffi-dev libssl-dev \
                chromium chromium-driver \
                git vim nano \
                sudo util-linux
            ;;
        redhat)
            sudo yum install -y epel-release
            sudo yum install -y \
                python3 python3-pip python3-devel \
                nmap nikto curl wget \
                tcpdump wireshark-cli \
                net-tools iproute iptables \
                arp-scan bind-utils traceroute whois \
                openssh-clients sshpass \
                gcc gcc-c++ libffi-devel openssl-devel \
                chromium chromedriver \
                git vim-minimal nano \
                sudo util-linux
            ;;
        arch)
            sudo pacman -S --noconfirm \
                python python-pip \
                nmap nikto curl wget \
                tcpdump wireshark-cli \
                net-tools iproute2 iptables \
                arp-scan bind-tools traceroute whois \
                openssh sshpass \
                base-devel libffi openssl \
                chromium chromedriver \
                git vim nano \
                sudo util-linux
            ;;
        alpine)
            sudo apk add --no-cache \
                python3 py3-pip py3-cryptography py3-paramiko \
                py3-requests py3-psutil py3-flask \
                nmap nikto curl wget \
                tcpdump wireshark-cli \
                net-tools iproute2 iptables \
                arp-scan bind-tools traceroute whois \
                openssh-client sshpass \
                build-base libffi-dev openssl-dev \
                chromium chromium-chromedriver \
                git vim nano \
                sudo util-linux
            ;;
        macos)
            # Check if Homebrew is installed
            if ! command -v brew &> /dev/null; then
                echo -e "${YELLOW}📦 Installing Homebrew...${NC}"
                /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            fi
            brew update
            brew install python3 nmap nikto wget tcpdump wireshark \
                 net-tools arp-scan bind traceroute whois openssh \
                 chromedriver git nmap
            ;;
        *)
            echo -e "${RED}❌ Unsupported OS${NC}"
            exit 1
            ;;
    esac
}

# Setup Python virtual environment
setup_venv() {
    echo -e "${BLUE}🐍 Setting up Python virtual environment...${NC}"
    
    # Create virtual environment
    python3 -m venv venv
    
    # Activate virtual environment
    source venv/bin/activate
    
    # Upgrade pip
    pip install --upgrade pip setuptools wheel
    
    # Install Python dependencies
    echo -e "${BLUE}📦 Installing Python packages...${NC}"
    
    # Create requirements.txt if not exists
    cat > requirements.txt << 'EOF'
cryptography>=41.0.0
paramiko>=3.3.0
scapy>=2.5.0
requests>=2.31.0
psutil>=5.9.0
colorama>=0.4.6
qrcode>=7.4.0
pillow>=10.0.0
pyshorteners>=1.0.1
python-whois>=0.8.0
flask>=2.3.0
flask-cors>=4.0.0
discord.py>=2.3.0
telethon>=1.34.0
slack-sdk>=3.21.0
selenium>=4.15.0
webdriver-manager>=4.0.0
netifaces>=0.11.0
dnspython>=2.4.0
python-dotenv>=1.0.0
pyyaml>=6.0
jsonschema>=4.19.0
tabulate>=0.9.0
tqdm>=4.66.0
rich>=13.5.0
EOF
    
    pip install -r requirements.txt
}

# Create configuration directories
create_directories() {
    echo -e "${BLUE}📁 Creating directory structure...${NC}"
    
    mkdir -p .king_phisher/phishing_templates
    mkdir -p .king_phisher/ssh_keys
    mkdir -p .king_phisher/captured_credentials
    mkdir -p .king_phisher/sessions
    mkdir -p .king_phisher/webhooks
    mkdir -p .king_phisher/plugins
    mkdir -p .king_phisher/modules
    mkdir -p reports
    mkdir -p wordlists
    mkdir -p logs
    mkdir -p templates
    mkdir -p .king_phisher/traffic_logs
    mkdir -p .king_phisher/nikto_results
    mkdir -p .king_phisher/ssh_logs
    mkdir -p .king_phisher/time_history
    mkdir -p .king_phisher/workspaces
    mkdir -p .king_phisher/payloads
    mkdir -p .king_phisher/scans
    
    # Set permissions
    chmod -R 755 .king_phisher
    chmod -R 755 reports
}

# Create configuration file
create_config() {
    echo -e "${BLUE}⚙️  Creating configuration file...${NC}"
    
    cat > .king_phisher/config.json << 'EOF'
{
    "monitoring": {
        "enabled": true,
        "port_scan_threshold": 10,
        "alert_on_scan": true
    },
    "scanning": {
        "default_ports": "1-1000",
        "timeout": 30,
        "threads": 100
    },
    "security": {
        "auto_block": true,
        "log_level": "INFO",
        "max_alerts_per_ip": 10
    },
    "nikto": {
        "enabled": true,
        "timeout": 300,
        "tuning": "123456789"
    },
    "traffic_generation": {
        "enabled": true,
        "max_duration": 300,
        "allow_floods": true,
        "default_rate": 100
    },
    "social_engineering": {
        "enabled": true,
        "default_port": 8080,
        "capture_credentials": true,
        "log_failed_attempts": true
    },
    "ssh": {
        "enabled": true,
        "default_timeout": 30,
        "max_connections": 5
    },
    "web_server": {
        "enabled": true,
        "port": 8080,
        "host": "0.0.0.0",
        "ssl_enabled": false
    },
    "discord": {
        "enabled": false,
        "token": "",
        "prefix": "!"
    },
    "telegram": {
        "enabled": false,
        "api_id": "",
        "api_hash": "",
        "bot_token": ""
    },
    "slack": {
        "enabled": false,
        "bot_token": "",
        "channel_id": "",
        "prefix": "!"
    },
    "whatsapp": {
        "enabled": false,
        "phone_number": "",
        "prefix": "/"
    }
}
EOF
}

# Create startup script
create_startup_script() {
    echo -e "${BLUE}🚀 Creating startup script...${NC}"
    
    cat > start_kingphisher.sh << 'EOF'
#!/bin/bash
# King Phisher Startup Script

# Activate virtual environment
source venv/bin/activate

# Set environment variables
export KING_PHISHER_ENV=production
export WEB_PORT=8080
export PHISHING_PORT=8081
export PHISHING_SSL_PORT=8443
export LOG_LEVEL=INFO

# Check if already running
if pgrep -f "king_phisher.py" > /dev/null; then
    echo "King Phisher is already running"
    exit 1
fi

# Start the application
echo "Starting King Phisher v3.0.0..."
python3 king_phisher.py

# Deactivate virtual environment on exit
deactivate
EOF
    
    chmod +x start_kingphisher.sh
}

# Create service file (systemd)
create_service() {
    if [[ "$OS" == "debian" ]] || [[ "$OS" == "redhat" ]] || [[ "$OS" == "arch" ]]; then
        echo -e "${BLUE}🛠️  Creating systemd service...${NC}"
        
        sudo cat > /etc/systemd/system/kingphisher.service << EOF
[Unit]
Description=King Phisher v3.0.0 Security Framework
After=network.target network-online.target
Wants=network-online.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$(pwd)
Environment="PATH=$(pwd)/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
Environment="KING_PHISHER_ENV=production"
ExecStart=$(pwd)/venv/bin/python3 $(pwd)/king_phisher.py
Restart=on-failure
RestartSec=10
StandardOutput=journal
StandardError=journal
SyslogIdentifier=kingphisher

# Security hardening
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=$(pwd)/.king_phisher $(pwd)/reports $(pwd)/logs

[Install]
WantedBy=multi-user.target
EOF
        
        sudo systemctl daemon-reload
        echo -e "${GREEN}✅ Service created. Enable with: sudo systemctl enable kingphisher${NC}"
        echo -e "${GREEN}   Start with: sudo systemctl start kingphisher${NC}"
    fi
}

# Create desktop entry (Linux)
create_desktop_entry() {
    if [[ "$OS" == "debian" ]] || [[ "$OS" == "redhat" ]] || [[ "$OS" == "arch" ]]; then
        cat > ~/.local/share/applications/kingphisher.desktop << EOF
[Desktop Entry]
Name=King Phisher
Comment=Advanced Security Framework
Exec=$(pwd)/start_kingphisher.sh
Icon=$(pwd)/icon.png
Terminal=true
Type=Application
Categories=System;Security;Network;
StartupNotify=true
EOF
        chmod +x ~/.local/share/applications/kingphisher.desktop
        echo -e "${GREEN}✅ Desktop entry created${NC}"
    fi
}

# Setup firewall rules
setup_firewall() {
    echo -e "${BLUE}🔥 Configuring firewall...${NC}"
    
    # Allow required ports
    if command -v ufw &> /dev/null; then
        sudo ufw allow 8080/tcp comment "King Phisher Web"
        sudo ufw allow 8081/tcp comment "King Phisher Phishing HTTP"
        sudo ufw allow 8443/tcp comment "King Phisher Phishing HTTPS"
        echo -e "${GREEN}✅ UFW rules added${NC}"
    elif command -v iptables &> /dev/null; then
        sudo iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
        sudo iptables -A INPUT -p tcp --dport 8081 -j ACCEPT
        sudo iptables -A INPUT -p tcp --dport 8443 -j ACCEPT
        echo -e "${GREEN}✅ iptables rules added${NC}"
    fi
}

# Main installation process
main() {
    echo -e "${CYAN}"
    echo "┌─────────────────────────────────────────────────────────┐"
    echo "│              STARTING INSTALLATION PROCESS              │"
    echo "└─────────────────────────────────────────────────────────┘"
    echo -e "${NC}"
    
    detect_os
    install_dependencies
    setup_venv
    create_directories
    create_config
    create_startup_script
    create_service
    create_desktop_entry
    setup_firewall
    
    echo -e "${GREEN}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║             ✅ INSTALLATION COMPLETED SUCCESSFULLY!          ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
    echo
    echo -e "${CYAN}📖 Usage:${NC}"
    echo "  1. Run: ${GREEN}./start_kingphisher.sh${NC}"
    echo "  2. Or: ${GREEN}source venv/bin/activate && python3 king_phisher.py${NC}"
    echo "  3. Or: ${GREEN}sudo systemctl start kingphisher${NC} (if service installed)"
    echo
    echo -e "${CYAN}🌐 Access:${NC}"
    echo "  Web Interface: ${GREEN}http://localhost:8080${NC}"
    echo
    echo -e "${CYAN}📁 Important paths:${NC}"
    echo "  Config: ${YELLOW}.king_phisher/config.json${NC}"
    echo "  Logs: ${YELLOW}logs/king_phisher.log${NC}"
    echo "  Reports: ${YELLOW}reports/${NC}"
    echo "  Database: ${YELLOW}.king_phisher/king_phisher.db${NC}"
    echo
    echo -e "${YELLOW}⚠️  Note: Run with sudo for full functionality (raw sockets, firewall)${NC}"
    echo
}

# Run main function
main