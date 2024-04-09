import argparse
import subprocess
import os

def classic_nmap(ip, output_file):
    command = f'nmap -T4 -A -Pn {ip}'
    subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)

def full_nmap(ip, output_file):
    command = f'nmap -T4 -sT -Pn -p- {ip}'
    subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)

def subdomain_enum(domain, output_file):
    command = f"wfuzz -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-20000.txt -u http://{domain} -H 'Host: FUZZ.{domain}'"
    subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)

def directory_fuzzing(domain, output_file):
    command = f"ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://{domain}/FUZZ"
    subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)

def nikto_scan(ip, output_file):
    command = f'nikto -h {ip}'
    subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)

def enum4linux(ip, output_file):
    command = f'enum4linux {ip}'
    subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)

def other_enumeration(ip, output_file):
    # Add other enumeration tools here as needed
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script to perform various scans and enumeration.')
    parser.add_argument('ip', help='IP address of the target')
    parser.add_argument('-d', '--domain', help='Domain name of the target')

    args = parser.parse_args()

    ip = args.ip
    domain = args.domain

    output_folder = 'bie_scans'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(os.path.join(output_folder, 'classic_nmap.txt'), 'w') as output_file:
        classic_nmap(ip, output_file)

    with open(os.path.join(output_folder, 'full_nmap.txt'), 'w') as output_file:
        full_nmap(ip, output_file)

    if domain:
        with open(os.path.join(output_folder, 'subdomain_enum.txt'), 'w') as output_file:
            subdomain_enum(domain, output_file)

        with open(os.path.join(output_folder, 'directory_fuzzing.txt'), 'w') as output_file:
            directory_fuzzing(domain, output_file)

    with open(os.path.join(output_folder, 'nikto_scan.txt'), 'w') as output_file:
        nikto_scan(ip, output_file)

    nmap_output = subprocess.check_output(['nmap', '-p', '139,445', '--open', '-oG', '-', ip]).decode('utf-8')
    if '139/open' in nmap_output or '445/open' in nmap_output:
        with open(os.path.join(output_folder, 'enum4linux.txt'), 'w') as output_file:
            enum4linux(ip, output_file)

    with open(os.path.join(output_folder, 'other_enumeration.txt'), 'w') as output_file:
        other_enumeration(ip, output_file)
