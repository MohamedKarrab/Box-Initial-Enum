import argparse
import subprocess
import os
from multiprocessing import Process

output_folder = 'bie_scans'

def print_banner():
    banner = """
██████╗ ██╗███████╗
██╔══██╗██║██╔════╝
██████╔╝██║█████╗  
██╔══██╗██║██╔══╝  
██████╔╝██║███████╗
╚═════╝ ╚═╝╚══════╝
bie 1.1.2 Author: Mohamed Karrab @Alashwas
"""
    print(banner)

def update_hosts_file(ip, domain):
    try:
        with open('/etc/hosts', 'a') as hosts_file:
            hosts_file.write(f"{ip}\t{domain}\n")
        print("[✓] Updated /etc/hosts with target IP and domain.")
    except Exception as e:
        print(f"[-] Error occurred while updating /etc/hosts: {e}")

def classic_nmap(ip):
    try:
        print("[+] Starting classic_nmap scan...")
        output_file_path = os.path.join(output_folder, 'classic_nmap.txt')
        command = f'nmap -T4 -A -Pn {ip}'
        with open(output_file_path, 'w') as output_file:
            output_file.write(f"Executed: {command}\n")
        with open(output_file_path, 'a') as output_file:
            subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)
        print("[✓] classic_nmap scan finished.")
    except Exception as e:
        print(f"[-] Error occurred during classic_nmap scan: {e}")

def full_nmap(ip):
    try:
        print("[+] Starting full_nmap scan...")
        output_file_path = os.path.join(output_folder, 'full_nmap.txt')
        command = f'nmap --min-rate 3000 -Pn -p- {ip}'
        with open(output_file_path, 'w') as output_file:
            output_file.write(f"Executed: {command}\n")
        with open(output_file_path, 'a') as output_file:
            subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)
        print("[✓] full_nmap scan finished.")
    except Exception as e:
        print(f"[-] Error occurred during full_nmap scan: {e}")

def subdomain_enum(domain):
    try:
        print("[+] Starting subdomain_enum scan...")
        output_file_path = os.path.join(output_folder, 'subdomain_enum.txt')
        command = f"wfuzz -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-20000.txt -u http://{domain} -H 'Host: FUZZ.{domain}'"
        with open(output_file_path, 'w') as output_file:
            output_file.write(f"Executed: {command}\n")
        with open(output_file_path, 'a') as output_file:
            subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)
        print("[✓] subdomain_enum scan finished.")
    except Exception as e:
        print(f"[-] Error occurred during subdomain_enum: {e}")

def directory_fuzzing(target):
    try:
        print("[+] Starting directory_fuzzing scan...")
        output_file_path = os.path.join(output_folder, 'directory_fuzzing.txt')
        command = f"ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://{target}/FUZZ"
        with open(output_file_path, 'w') as output_file:
            output_file.write(f"Executed: {command}\n")
        with open(output_file_path, 'a') as output_file:
            subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)
        print("[✓] directory_fuzzing scan finished.")
    except Exception as e:
        print(f"[-] Error occurred during directory_fuzzing: {e}")

def nikto_scan(ip):
    try:
        print("[+] Starting nikto_scan...")
        output_file_path = os.path.join(output_folder, 'nikto_scan.txt')
        command = f'nikto -h {ip}'
        with open(output_file_path, 'w') as output_file:
            output_file.write(f"Executed: {command}\n")
        with open(output_file_path, 'a') as output_file:
            subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)
        print("[✓] nikto_scan finished.")
    except Exception as e:
        print(f"[-] Error occurred during nikto_scan: {e}")

def enum4linux(ip):
    try:
        print("[+] Starting enum4linux scan...")
        output_file_path = os.path.join(output_folder, 'enum4linux.txt')
        command = f'enum4linux {ip}'
        with open(output_file_path, 'w') as output_file:
            output_file.write(f"Executed: {command}\n")
        with open(output_file_path, 'a') as output_file:
            subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)
        print("[✓] enum4linux scan finished.")
    except Exception as e:
        print(f"[-] Error occurred during enum4linux: {e}")

def other_enumeration(ip):
    try:
        print("[+] Starting other_enumeration...")
        output_file_path = os.path.join(output_folder, 'other_enumeration.txt')
        # Add your other enumeration commands here
        print("[✓] other_enumeration finished.")
    except Exception as e:
        print(f"[-] Error occurred during other_enumeration: {e}")


if __name__ == "__main__":
    print_banner()

    parser = argparse.ArgumentParser(description='Script to perform various scans and enumeration.')
    parser.add_argument('ip', help='IP address of the target')
    parser.add_argument('-d', '--domain', help='Domain name of the target')

    args = parser.parse_args()

    ip = args.ip
    domain = args.domain

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    update_hosts_file(ip, domain)

    processes = []

    p = Process(target=classic_nmap, args=(ip,))
    p.start()
    processes.append(p)

    p = Process(target=full_nmap, args=(ip,))
    p.start()
    processes.append(p)

    if domain:
        target = domain
    else:
        target = ip

    p = Process(target=directory_fuzzing, args=(target,))
    p.start()
    processes.append(p)

    if domain:
        p = Process(target=subdomain_enum, args=(domain,))
        p.start()
        processes.append(p)

    p = Process(target=nikto_scan, args=(ip,))
    p.start()
    processes.append(p)

    nmap_output = subprocess.check_output(['nmap', '-p', '139,445', '--open', '-oG', '-', ip]).decode('utf-8')
    if '139/open' in nmap_output or '445/open' in nmap_output:
        p = Process(target=enum4linux, args=(ip,))
        p.start()
        processes.append(p)

    p = Process(target=other_enumeration, args=(ip,))
    p.start()
    processes.append(p)

    for p in processes:
        p.join()
