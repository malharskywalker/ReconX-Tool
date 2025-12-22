import shutil
import sys
import platform

# -------------------------------
# Python dependency check
# -------------------------------
def check_python_modules():
    try:
        import requests
        print("[+] Python module found: requests")
    except ImportError:
        print("\n[!] Missing Python module: requests")
        print("    Install using:")
        print("    python3 -m pip install requests\n")
        sys.exit(1)


# -------------------------------
# External tool check (OS-aware)
# -------------------------------
def check_cli_tools():
    os_type = platform.system().lower()

    if os_type == "linux":
        tools = {
            "subfinder": {
                "install": "go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest\n"
                           "export PATH=$PATH:$HOME/go/bin"
            },
            "amass": {
                "install": "sudo apt install amass"
            },
            "theHarvester": {
                "install": "pip3 install theHarvester"
            },
            "whois": {
                "install": "sudo apt install whois"
            },
            "nmap": {
                "install": "sudo apt install nmap"
            }
        }

    elif os_type == "windows":
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

    else:
        print(f"[!] Unsupported OS detected: {os_type}")
        sys.exit(1)

    missing = []

    for tool in tools:
        if shutil.which(tool) is None:
            missing.append(tool)

    if missing:
        print("\n[!] Missing required external tools:\n")
        for tool in missing:
            print(f"[-] {tool}")
            print("    Install using:")
            print(f"    {tools[tool]['install']}\n")

        print("[!] Install the missing tools and re-run reconx.\n")
        sys.exit(1)

    print("[+] All external tools found")


# -------------------------------
# Entry function
# -------------------------------
def run_prechecks():
    print("\n[*] Running dependency checks...\n")
    check_python_modules()
    check_cli_tools()
    print("\n[+] All requirements satisfied. Starting recon...\n")
