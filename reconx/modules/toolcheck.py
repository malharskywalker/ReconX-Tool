import shutil
import sys

def check_cli_tools():
    tools = [
        "subfinder",
        "amass",
        "theHarvester",
        "whois",
        "nmap"
    ]

    missing = []

    for tool in tools:
        if shutil.which(tool) is None:
            missing.append(tool)

    if missing:
        print("\n[!] Missing external tools:")
        for tool in missing:
            print(f"    - {tool}")

        print("\n[!] Install missing tools and add them to PATH.")
        sys.exit(1)

    print("[+] All external tools found")


def check_python_modules():
    try:
        import requests
    except ImportError:
        print("\n[!] Missing Python module: requests")
        print("    Install using: pip install requests")
        sys.exit(1)

    print("[+] All Python modules found")


def run_prechecks():
    print("[*] Checking required tools...\n")
    check_python_modules()
    check_cli_tools()
    print("\n[+] All requirements satisfied\n")
