@echo off
title King Phisher v3.0.0 - Windows Installation
color 0A

echo ================================================
echo    👑 KING PHISHER v3.0.0 - INSTALLATION
echo ================================================
echo.

:: Check Administrator privileges
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Please run as Administrator
    pause
    exit /b 1
)

:: Check Python installation
echo [1/6] Checking Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Python not found. Installing...
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe -OutFile python_installer.exe"
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    del python_installer.exe
) else (
    echo [OK] Python found
)

:: Install pip if missing
python -m ensurepip --upgrade

:: Upgrade pip
echo [2/6] Upgrading pip...
python -m pip install --upgrade pip

:: Install dependencies
echo [3/6] Installing Python dependencies...
pip install -r requirements.txt

:: Install nmap for Windows
echo [4/6] Installing nmap...
if not exist "C:\Program Files (x86)\Nmap" (
    powershell -Command "Invoke-WebRequest -Uri https://nmap.org/dist/nmap-7.94-setup.exe -OutFile nmap_setup.exe"
    start /wait nmap_setup.exe /S
    del nmap_setup.exe
)

:: Install Nikto for Windows (using WSL or Cygwin alternative)
echo [5/6] Setting up Nikto via WSL...
wsl --install -d Ubuntu >nul 2>&1
wsl sudo apt update
wsl sudo apt install -y nikto

:: Create directories
echo [6/6] Creating directories...
mkdir .king_phisher 2>nul
mkdir reports 2>nul
mkdir wordlists 2>nul
mkdir logs 2>nul
mkdir templates 2>nul
mkdir .king_phisher\phishing_templates 2>nul
mkdir .king_phisher\ssh_keys 2>nul
mkdir .king_phisher\captured_credentials 2>nul

:: Create config
echo Creating default configuration...
(
echo {
echo   "monitoring": {"enabled": true, "port_scan_threshold": 10},
echo   "scanning": {"default_ports": "1-1000", "timeout": 30},
echo   "security": {"auto_block": false, "log_level": "INFO"},
echo   "traffic_generation": {"enabled": true, "max_duration": 300, "allow_floods": false},
echo   "web_server": {"enabled": true, "port": 8080, "host": "0.0.0.0"}
echo }
) > .king_phisher\config.json

:: Add to PATH
echo [INFO] Adding to PATH...
setx PATH "%PATH%;C:\Program Files\Nmap;C:\Program Files (x86)\Nmap"

:: Firewall rules
echo [INFO] Configuring firewall...
netsh advfirewall firewall add rule name="King Phisher Web" dir=in action=allow protocol=TCP localport=8080
netsh advfirewall firewall add rule name="King Phisher Phishing HTTP" dir=in action=allow protocol=TCP localport=8081
netsh advfirewall firewall add rule name="King Phisher Phishing HTTPS" dir=in action=allow protocol=TCP localport=8443

:: Create desktop shortcut
echo [INFO] Creating desktop shortcut...
powershell -Command "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%userprofile%\Desktop\King Phisher.lnk'); $Shortcut.TargetPath = 'cmd.exe'; $Shortcut.Arguments = '/k python %cd%\king_phisher.py'; $Shortcut.Save()"

:: Create start menu shortcut
powershell -Command "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%programdata%\Microsoft\Windows\Start Menu\Programs\King Phisher.lnk'); $Shortcut.TargetPath = 'cmd.exe'; $Shortcut.Arguments = '/k python %cd%\king_phisher.py'; $Shortcut.Save()"

echo.
echo ================================================
echo    ✅ INSTALLATION COMPLETED SUCCESSFULLY!
echo ================================================
echo.
echo To start King Phisher:
echo   1. Double-click the desktop shortcut
echo   2. Or run: python king_phisher.py
echo.
echo Web Interface: http://localhost:8080
echo.
pause