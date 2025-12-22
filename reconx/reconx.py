import os
from modules.subdomain import subdomain_enum
from modules.whois_lookup import whois_lookup
from modules.osint import email_enum
from modules.active import active_recon
from modules.report import generate_report
from modules.toolcheck import run_prechecks


def menu():
    print("""
[1] Passive Recon
[2] Active Recon
[3] Full Recon
[4] Exit
""")

def main():
    run_prechecks()
    domain = input("Enter target domain: ")
    os.makedirs("output", exist_ok=True)

    while True:
        menu()
        choice = input("Select an option: ")

        if choice == "1":
            subdomain_enum(domain)
            whois_lookup(domain)
            email_enum(domain)
            generate_report(domain)

        elif choice == "2":
            active_recon(domain)
            generate_report(domain)

        elif choice == "3":
            subdomain_enum(domain)
            whois_lookup(domain)
            email_enum(domain)
            active_recon(domain)
            generate_report(domain)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
