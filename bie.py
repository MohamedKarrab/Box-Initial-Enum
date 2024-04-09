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

def nikto_scan(ip):
    command = f'nikto -h {ip}'
    subprocess.run(command, shell=True)

def other_enumeration(ip):
    # Add other enumeration tools here as needed
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script to perform various scans and enumeration.')
    parser.add_argument('ip', help='IP address of the target')
    parser.add_argument('--domain', help='Domain name of the target (optional)')

    args = parser.parse_args()

    ip = args.ip
    domain = args.domain

    classic_nmap(ip)
    full_nmap(ip)
    if domain:
        subdomain_enum(domain)
        directory_fuzzing(domain)
    nikto_scan(ip)
    other_enumeration(ip)
