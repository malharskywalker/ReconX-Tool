import shutil
import sys
import platform

def check_python_modules():
    try:
        import requests
        print("[+] Python module found: requests")
    except ImportError:
        print("\n[!] Missing Python module: requests")
        print("    Install using:")
        print("    python -m pip install requests\n")
        sys.exit(1)


def check_cli_tools():
    tools = {
        "subfinder": {
            "install": "Download from https://github.com/projectdiscovery/subfinder/releases\n"
                       "Extract subfinder.exe and add it to PATH"
        },
        "amass": {
            "install": "Download from https://github.com/owasp-amass/amass/releases\n"
                       "Extract amass.exe and add it to PATH"
        },
        "theHarvester": {
            "install": "pip install theHarvester"
        },
        "whois": {
            "install": "Download from https://learn.microsoft.com/en-us/sysinternals/downloads/whois\n"
                       "Extract whois.exe and add it to PATH"
        },
        "nmap": {
            "install": "Download from https://nmap.org/download.html\n"
                       "Install and ensure it is added to PATH"
        }
    }

    missing = []

    for tool in tools:
        if shutil.which(tool) is None:
            missing.append(tool)

    if missing:
        print("\n[!] Missing required external tools:\n")
        for tool in missing:
            print(f"[-] {tool}")
            print(f"    How to install:")
            print(f"    {tools[tool]['install']}\n")

        print("[!] Fix the above issues and re-run the tool.\n")
        sys.exit(1)

    print("[+] All external tools found")


def run_prechecks():
    print("\n[*] Running dependency checks...\n")
    check_python_modules()
    check_cli_tools()
    print("\n[+] All requirements satisfied. Starting recon...\n")
