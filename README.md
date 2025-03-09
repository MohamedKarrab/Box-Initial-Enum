# Box Initial Enumeration

```
██████╗ ██╗███████╗
██╔══██╗██║██╔════╝
██████╔╝██║█████╗  
██╔══██╗██║██╔══╝  
██████╔╝██║███████╗
╚═════╝ ╚═╝╚══════╝
```

Bie automates initial enumeration and scanning performed on HackTheBox (HTB) and TryHackMe machines. It integrates many tools such as Nmap, Nikto, ffuf, enum4linux.. to be as comprehensive as possible.

## Features

- **Nmap Scans**: Conducts full port and classic Nmap scans with the needed options.
- **Subdomain Enumeration**: Utilizes wfuzz to discover subdomains of the specified domain.
- **Directory Fuzzing**: Fast ffuf directory fuzzing.
- **Web Server Scan**: Conducts a web server scan using Nikto.
- **SMB enumeration**: Using enum4linux if ports 139 or 445 are available.
- **Additional Enumeration**: You can use your own tools here.

## Prerequisites

- Nmap
- Nikto
- wfuzz
- ffuf
- enum4linux

## Usage

```bash
sudo python3 bie.py <IP> [-d <domain>]
```

- `<ip>`: Mandatory argument specifying the IP address of the target.
- `[-d/--domain <domain>]`: Optional argument providing the domain name of the target (for subdomain enumeration).

Example:

```bash
sudo python3 bie.py 10.10.11.242 -d somedomain
```

## Configuration and hints

How to filter valid subdomains? (change 154 with the repeating number of Chars)
```bash
cat subdomain_enum.txt | grep -v "154 Ch" 
```

You may need to change wordlists location (inside bie.py) to where you have them, this is the default configuration:
![image](https://github.com/MohamedKarrab/Box-Initial-Enum/assets/107933631/9e344ba9-5252-4e29-acd1-00002951b751)


## Note

- This script needs to be ran using sudo for the /etc/hosts changes to take place.
- Ensure that you have appropriate permissions before scanning any target.
- Usage of this script for unauthorized access or against targets without proper authorization is strictly prohibited.

## Disclaimer

This script is provided for educational and informational purposes only. Usage of this script for any unauthorized activities is not endorsed or encouraged. The author shall not be responsible for any misuse or damage caused by the script.
