import os

def email_enum(domain):
    print("[+] Running theHarvester")
    os.system(f"theHarvester -d {domain} -b google > output/emails.txt")
