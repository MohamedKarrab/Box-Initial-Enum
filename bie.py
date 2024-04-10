import argparse
import subprocess
import os
from multiprocessing import Process

def print_banner():
    banner = """
██████╗ ██╗███████╗
██╔══██╗██║██╔════╝
██████╔╝██║█████╗  
██╔══██╗██║██╔══╝  
██████╔╝██║███████╗
╚═════╝ ╚═╝╚══════╝
bie 1.1.0 Author: Mohamed Karrab @Alashwas
"""
    print(banner)

def update_hosts_file(ip, domain):
    try:
        with open('/etc/hosts', 'a') as hosts_file:
            hosts_file.write(f"{ip}\t{domain}\n")
        print("[✓] Updated /etc/hosts with target IP and domain.")
    except Exception as e:
        print(f"[-] Error occurred while updating /etc/hosts: {e}")

def classic_nmap(ip, output_file):
    try:
        print("[+] Starting classic_nmap scan...")
        command = f'nmap -T4 -A -Pn {ip}'
        subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)
        print("[✓] classic_nmap scan finished.")
    except Exception as e:
        print(f"[-] Error occurred during classic_nmap scan: {e}")

def full_nmap(ip, output_file):
    try:
        print("[+] Starting full_nmap scan...")
        command = f'nmap -T4 -sT -Pn -p- {ip}'
        subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)
        print("[✓] full_nmap scan finished.")
    except Exception as e:
        print(f"[-] Error occurred during full_nmap scan: {e}")

def subdomain_enum(domain, output_file):
    try:
        print("[+] Starting subdomain_enum scan...")
        command = f"wfuzz -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-20000.txt -u http://{domain} -H 'Host: FUZZ.{domain}'"
        subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)
        print("[✓] subdomain_enum scan finished.")
    except Exception as e:
        print(f"[-] Error occurred during subdomain_enum: {e}")

def directory_fuzzing(domain, output_file):
    try:
        print("[+] Starting directory_fuzzing scan...")
        command = f"ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://{domain}/FUZZ"
        subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)
        print("[✓] directory_fuzzing scan finished.")
    except Exception as e:
        print(f"[-] Error occurred during directory_fuzzing: {e}")

def nikto_scan(ip, output_file):
    try:
        print("[+] Starting nikto_scan...")
        command = f'nikto -h {ip}'
        subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)
        print("[✓] nikto_scan finished.")
    except Exception as e:
        print(f"[-] Error occurred during nikto_scan: {e}")

def enum4linux(ip, output_file):
    try:
        print("[+] Starting enum4linux scan...")
        command = f'enum4linux {ip}'
        subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)
        print("[✓] enum4linux scan finished.")
    except Exception as e:
        print(f"[-] Error occurred during enum4linux: {e}")

def other_enumeration(ip, output_file):
    pass

if __name__ == "__main__":
    print_banner()

    parser = argparse.ArgumentParser(description='Script to perform various scans and enumeration.')
    parser.add_argument('ip', help='IP address of the target')
    parser.add_argument('-d', '--domain', help='Domain name of the target')

    args = parser.parse_args()

    ip = args.ip
    domain = args.domain

    output_folder = 'bie_scans'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    update_hosts_file(ip, domain)

    processes = []

    with open(os.path.join(output_folder, 'classic_nmap.txt'), 'w') as output_file:
        p = Process(target=classic_nmap, args=(ip, output_file))
        p.start()
        processes.append(p)

    with open(os.path.join(output_folder, 'full_nmap.txt'), 'w') as output_file:
        p = Process(target=full_nmap, args=(ip, output_file))
        p.start()
        processes.append(p)

    if domain:
        with open(os.path.join(output_folder, 'subdomain_enum.txt'), 'w') as output_file:
            p = Process(target=subdomain_enum, args=(domain, output_file))
            p.start()
            processes.append(p)

        with open(os.path.join(output_folder, 'directory_fuzzing.txt'), 'w') as output_file:
            p = Process(target=directory_fuzzing, args=(domain, output_file))
            p.start()
            processes.append(p)

    with open(os.path.join(output_folder, 'nikto_scan.txt'), 'w') as output_file:
        p = Process(target=nikto_scan, args=(ip, output_file))
        p.start()
        processes.append(p)

    nmap_output = subprocess.check_output(['nmap', '-p', '139,445', '--open', '-oG', '-', ip]).decode('utf-8')
    if '139/open' in nmap_output or '445/open' in nmap_output:
        with open(os.path.join(output_folder, 'enum4linux.txt'), 'w') as output_file:
            p = Process(target=enum4linux, args=(ip, output_file))
            p.start()
            processes.append(p)

    with open(os.path.join(output_folder, 'other_enumeration.txt'), 'w') as output_file:
        p = Process(target=other_enumeration, args=(ip, output_file))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
