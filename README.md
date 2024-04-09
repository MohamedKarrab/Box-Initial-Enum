# Box Initial Enumeration

```
██████╗ ██╗███████╗
██╔══██╗██║██╔════╝
██████╔╝██║█████╗  
██╔══██╗██║██╔══╝  
██████╔╝██║███████╗
╚═════╝ ╚═╝╚══════╝
```

This script automates initial enumeration tasks commonly performed on Hack The Box (HTB) and TryHackMe machines. It integrates various tools such as Nmap, Nikto, wfuzz, and ffuf to provide comprehensive analysis of a target's infrastructure and web applications.

## Features

- **Nmap Scans**: Conducts both classic and full port Nmap scans with aggressive options.
- **Subdomain Enumeration**: Utilizes wfuzz to discover subdomains of the specified domain.
- **Directory Fuzzing**: Employs ffuf to perform directory fuzzing on the provided domain.
- **Web Server Scan**: Conducts a web server scan using Nikto, identifying potential vulnerabilities and misconfigurations.
- **Additional Enumeration**: Placeholder for integrating further enumeration tools as needed.

## Prerequisites

- Nmap
- Nikto
- wfuzz
- ffuf

## Usage

```bash
python script.py <ip> [--domain <domain>]
```

- `<ip>`: Mandatory argument specifying the IP address of the target.
- `[--domain <domain>]`: Optional argument providing the domain name of the target.

Example:

```bash
python script.py 10.10.11.242 --domain example.com
```

## Output

Results from the scans and enumerations will be displayed in the terminal and piped accordingly for further analysis.

## Note

- Ensure that you have appropriate permissions before scanning any target.
- Usage of this script for unauthorized access or against targets without proper authorization is strictly prohibited and may be illegal.

## Disclaimer

This script is provided for educational and informational purposes only. Usage of this script for any unauthorized activities is not endorsed or encouraged. The author shall not be responsible for any misuse or damage caused by the script.
