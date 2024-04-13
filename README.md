# Box Initial Enumeration

```
██████╗ ██╗███████╗
██╔══██╗██║██╔════╝
██████╔╝██║█████╗  
██╔══██╗██║██╔══╝  
██████╔╝██║███████╗
╚═════╝ ╚═╝╚══════╝
```

This script automates initial enumeration tasks commonly performed on Hack The Box (HTB) and TryHackMe machines. It integrates many tools such as Nmap, Nikto, ffuf.. to provide comprehensive scanning and enumeration of a target's infrastructure and web applications.

## Features

- **Nmap Scans**: Conducts both classic and full port Nmap scans with aggressive options.
- **Subdomain Enumeration**: Utilizes wfuzz to discover subdomains of the specified domain.
- **Directory Fuzzing**: Employs ffuf to perform directory fuzzing on the provided domain.
- **Web Server Scan**: Conducts a web server scan using Nikto.
- **Additional Enumeration**: Placeholder for integrating further enumeration tools as needed.

## Prerequisites

- Nmap
- Nikto
- wfuzz
- ffuf
- enum4linux

## Usage

```bash
python script.py <ip> [-d <domain>]
```

- `<ip>`: Mandatory argument specifying the IP address of the target.
- `[-d/--domain <domain>]`: Optional argument providing the domain name of the target (for subdomain enumeration).

Example:

```bash
python script.py <IP> --domain example.com
```

## Note

- This script needs to be ran using sudo for the /etc/hosts changes to take place.
- Ensure that you have appropriate permissions before scanning any target.
- Usage of this script for unauthorized access or against targets without proper authorization is strictly prohibited and may be illegal.

## Disclaimer

This script is provided for educational and informational purposes only. Usage of this script for any unauthorized activities is not endorsed or encouraged. The author shall not be responsible for any misuse or damage caused by the script.
