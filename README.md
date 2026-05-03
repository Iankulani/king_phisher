# king_phisher

<img width="1536" height="900" alt="kingphisher" src="https://github.com/user-attachments/assets/b8c9d3c0-2c4a-4c65-8d55-da7e143ff5ea" />


[![GitHub stars](https://img.shields.io/github/stars/Iankulani/king_phisher?style=for-the-badge&logo=github)](https://github.com/Iankulani/king_phisher/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Iankulani/king_phisher?style=for-the-badge&logo=github)](https://github.com/Iankulani/king_phisher/network)
[![GitHub watchers](https://img.shields.io/github/watchers/Iankulani/king_phisher?style=for-the-badge&logo=github)](https://github.com/Iankulani/king_phisher/watchers)
[![GitHub contributors](https://img.shields.io/github/contributors/Iankulani/king_phisher?style=for-the-badge&logo=github)](https://github.com/Iankulani/king_phisher/graphs/contributors)
[![GitHub last commit](https://img.shields.io/github/last-commit/Iankulani/king_phisher?style=for-the-badge&logo=git)](https://github.com/Iankulani/king_phisher/commits/main)
[![Docker Pulls](https://img.shields.io/badge/docker-available-blue?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/r/iankulaniking_phisher) <!-- Replace with actual Docker Hub link if available -->
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows-blue?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Iankulani/king_phisher)
[![GitHub watchers](https://img.shields.io/github/watchers/Iankulani/king_phisher?style=for-the-badge&logo=github)](https://github.com/Iankulani/king_phisher/watchers)

King Phisher is an open-source, professional-grade cybersecurity tool designed for simulating sophisticated phishing attacks and conducting social engineering campaigns . Developed initially by Accurate Cyber Defence (ACD), and currently maintained within the security community, it is widely used by Red Teams, SOC (Security Operations Centers) teams, and penetration testers to assess the "human firewall" of an organization .

Unlike basic email senders, King Phisher operates on a flexible client-server architecture. This allows security professionals to manage multiple campaigns simultaneously, clone legitimate web environments in real-time, and harvest credentials, all while providing detailed analytics on user behavior.


## 2. Key Features & Technical

 Capabilities

# 📧 Multi-Channel Communication Engine
While King Phisher is historically renowned for email phishing (SMTP support), the modern iteration recognizes that social engineering happens everywhere. The tool facilitates campaign delivery across Telegram, Discord, Slack, iMessage, and Web Apps .

Email Engine: Supports advanced SMTP configurations (Gmail, Office 365, Custom SMTP) including SPF validation and DKIM checks to improve email deliverability and authenticity .

Web Integration: It is not just limited to messages; the tool integrates deeply with web applications to create realistic login portals.

# 🎨 Dynamic Credential Harvesting & Web Cloning
One of the most powerful features of King Phisher is its ability to bypass simple awareness training by simulating realistic scenarios.

Real-time Cloning: It can clone legitimate web pages (e.g., Office 365, corporate VPN portals) to host fake landing pages.

Two-Factor Harvesting: Advanced versions support "phishing-resistant" techniques, including harvesting 2FA tokens (pass-through proxies) to simulate real-world Advanced Persistent Threat (APT) tactics .

# 📊 Real-Time Analytics & SOC Metrics
King Phisher provides a comprehensive dashboard that allows security teams to measure the effectiveness of their security posture:

Live Tracking: See exactly who opened the email, who clicked the link, and who entered credentials in real-time .

Geo-location: Track the geographic location of targets who interact with the phishing link.

SOC Testing Metrics: It generates specific KPIs for SOC teams, including Detection Rate (percentage of campaigns caught by security tools) and Response Time (how fast the SOC reacted to a simulated breach) .

# 🛠️ Installation & Environment
Platform Support: The server runs on Linux (Ubuntu 20.04/22.04/24.04) and is pre-packaged in Kali Linux for ease of use. The client interface is available for both Linux and Windows .

One-Click Installer: Modern distributions (like AKUMA editions) feature automated installation scripts that configure PostgreSQL databases, Python dependencies, and SSL certificates without manual intervention .

# 3. How It Works: The Attack (Simulation) Chain
King Phisher allows operators to build a campaign in four simple steps, mirroring a real cybercriminal's workflow:

Target Ingestion: Import a CSV file containing the target list (Name, Email, Department). This allows for departmental segmentation (e.g., testing Finance vs. HR separately) .

Template Selection: Choose or craft an email template. Users can utilize pre-built HTML templates (corporate login alerts, security updates) or create custom messages for specific platforms (Discord DMs or Slack DMs) .

The Lure: The tool sends out messages via the selected vector (Email, Slack, etc.). If the user clicks the embedded link, they are routed through the King Phisher web server.

Data Exfiltration (The Catch): The target lands on a cloned webpage. If they enter their username/password or 2FA code, the data is captured, stored locally on the testing server, and displayed in the operator's dashboard .

# 4. Use Cases & Target Audience
For Red Teams:

* Simulating targeted "Spear Phishing" attacks against key personnel.

* Testing email gateway security (bypassing filters).

* Performing credential harvesting exercises without malware.

# For SOC / Blue Teams:

* Human Risk Assessment: Identifying which departments are most susceptible to clicking malicious links .

* Training Validation: Running drills via Slack or Discord to train employees on spotting social engineering in workplace chat tools.

* SIEM Integration: Feeding campaign data into SIEM systems to tune detection rules for real phishing attempts.

# For General Security Awareness

* Creating internal "cyber drills" to educate staff on the dangers of credential reuse and urgency-based lures .

# 5. Legal & Ethical Considerations (Disclaimer)
 
It is crucial to note that King Phisher is a double-edged sword.

Authorization Required: Use of this tool is only legal on networks you own or have explicit written permission to test (e.g., formal penetration testing contracts). Unauthorized use constitutes wire fraud and computer misuse .

Ethical Use: It is designed for education and hardening, not exploitation.

# 6. Summary
King Phisher stands out because it moves beyond simple email blasts. By integrating Telegram, Slack, iMessage, and Web Apps into a single unified testing platform, it addresses the modern reality of social engineering. For any organization looking to test its resilience against data theft, King Phisher provides the enterprise-grade tools necessary to clone, launch, capture, and analyze—all from a user-friendly desktop client.

# How to clone 
```bash
git clone https://github.com/Iankulani/king_phisher.git
cd king_phisher
```

  # How to run
  ```bash
python king_phisher.py
```


# Quick Start Commands

# Complete setup
```bash
pip install -r requirements.txt
```
```bash
python3 king_phisher.py
```

# Or using the installer
```bash
chmod +x install.sh
./install.sh
```
# Or using Docker
```bash
docker build -t king-phisher .
docker run -it --privileged -p 8080:8080 king-phisher
```
# Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Iankulani/king_phisher&type=Date)](https://star-history.com/#Iankulani/king_phisher&Date)
