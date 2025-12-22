# ReconX 🔍
A Modular Reconnaissance Automation Framework

ReconX is a Linux-based reconnaissance automation tool built for bug bounty
hunters and penetration testers. It automates passive and active reconnaissance
by integrating multiple industry-standard OSINT and recon tools into a single,
structured workflow to identify an organization’s attack surface.

---

## 🚀 Features

- Passive reconnaissance using public OSINT sources
- Subdomain enumeration
- Certificate Transparency analysis (crt.sh)
- WHOIS information gathering
- OS-aware dependency and tool checks
- Modular and extensible architecture
- Designed for ethical hacking and authorized testing

---

## 🛠️ Integrated Tools

- Subfinder  
- Amass (passive mode)  
- theHarvester  
- crt.sh  
- WHOIS  
- Nmap (for future active reconnaissance)

---

## 📂 Project Structure

reconx/
├── reconx.py
├── requirements.txt
├── modules/
│ ├── toolcheck.py
│ ├── subdomain.py
│ ├── crtsh.py
│ ├── whois_lookup.py
│ └── live_hosts.py
├── output/
└── README.md

yaml
Copy code

---

## ⚙️ Requirements

- Linux (Kali Linux / Ubuntu)
- Python 3.9+
- Go (for ProjectDiscovery tools)

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/reconx.git
cd reconx
pip3 install -r requirements.txt
External tools required:

subfinder

amass

theHarvester

whois

nmap

ReconX automatically checks for missing tools and provides installation guidance.

▶️ Usage
bash
Copy code
python3 reconx.py
Example:

text
Copy code
Enter target domain: testphp.vulnweb.com
📄 Output
ReconX displays reconnaissance progress in the terminal and is designed to
generate a structured recon report summarizing:

Domain and subdomains

Certificate transparency data

WHOIS information

Public IPs and exposed services

Reports are intended to be stored in the output/ directory.

🧪 Legal Testing Targets
This tool should be tested only against authorized or intentionally vulnerable
domains, such as:

testphp.vulnweb.com

demo.testfire.net

scanme.nmap.org

Do NOT scan systems without explicit permission.

⚠️ Disclaimer
This tool is intended strictly for educational purposes and authorized security
testing. The author is not responsible for any misuse or illegal activities.

👤 Author
Mallangouda Biradar
Cybersecurity Enthusiast | VAPT | Bug Bounty
GitHub: https://github.com/malharskywalker

🧠 Future Enhancements
Structured report export (TXT / JSON)

Passive vs Active reconnaissance modes

Parallel execution for faster recon

Improved logging and error handling

Integration with additional recon tools

