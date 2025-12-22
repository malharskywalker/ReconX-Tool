def generate_report(domain):
    print("[+] Generating final report")

    with open("output/final_report.txt", "w") as f:
        f.write(f"TARGET: {domain}\n")
        f.write("="*40 + "\n\n")

        f.write("SUBDOMAINS:\n")
        f.write(open("output/subdomains.txt").read() + "\n")

        f.write("WHOIS INFORMATION:\n")
        f.write(open("output/whois.txt").read() + "\n")

        f.write("EMAILS & OSINT:\n")
        f.write(open("output/emails.txt").read() + "\n")

        f.write("LIVE HOSTS:\n")
        f.write(open("output/live_hosts.txt").read() + "\n")

        f.write("EXPOSED SERVICES:\n")
        f.write(open("output/services.txt").read())
