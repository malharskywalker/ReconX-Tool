import os

def whois_lookup(domain):
    print("[+] Fetching WHOIS information")
    os.system(f"whois {domain} > output/whois.txt")
