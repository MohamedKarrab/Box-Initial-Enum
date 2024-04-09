import argparse
import subprocess

def classic_nmap(ip):
    command = f'nmap -T4 -A -Pn {ip}'
    subprocess.run(command, shell=True)

def full_nmap(ip):
    command = f'nmap -T4 -A -Pn -p- {ip}'
    subprocess.run(command, shell=True)

def subdomain_enum(domain):
    command = f"wfuzz -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-20000.txt -u http://{domain} -H 'Host: FUZZ.{domain}'"
    subprocess.run(command, shell=True)

def directory_fuzzing(domain):
    command = f"ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://{domain}/FUZZ"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script to perform various scans and enumeration.')
    parser.add_argument('target', help='IP address or domain name')

    args = parser.parse_args()

    target = args.target

    # Assuming the input can be either IP address or domain name
    try:
        # Checking if the input is an IP address
        ip = target
        classic_nmap(ip)
        full_nmap(ip)
    except ValueError:
        # If not an IP address, assuming it's a domain name
        domain = target
        subdomain_enum(domain)
        directory_fuzzing(domain)
