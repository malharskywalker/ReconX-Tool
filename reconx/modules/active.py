import os

def active_recon(domain):
    print("[+] Running Active Recon")

    # Amass active
    os.system(f"amass enum -active -d {domain} > output/live_hosts.txt")

    # Nmap scan
    print("[+] Scanning services")
    os.system("nmap -iL output/live_hosts.txt -top-ports 1000 > output/services.txt")
