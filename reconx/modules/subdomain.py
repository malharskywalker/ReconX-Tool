import os
import requests

def subdomain_enum(domain):
    print("[+] Running Subdomain Enumeration")

    os.system(f"subfinder -d {domain} -silent > output/subfinder.txt")
    os.system(f"amass enum -passive -d {domain} > output/amass.txt")

    # crt.sh
    print("[+] Fetching crt.sh data")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    response = requests.get(url)

    subs = set()
    if response.status_code == 200:
        for entry in response.json():
            subs.add(entry['name_value'])

    with open("output/crtsh.txt", "w") as f:
        for sub in subs:
            f.write(sub + "\n")

    # Merge all
    os.system("cat output/subfinder.txt output/amass.txt output/crtsh.txt | sort -u > output/subdomains.txt")

    print("[+] Subdomain enumeration completed")
