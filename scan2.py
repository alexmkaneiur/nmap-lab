import nmap
import datetime
nm = nmap.PortScanner()
timestamp = f"掃描時間: {datetime.datetime.now()}\n"
print(timestamp)
nm.scan("192.168.229.0/24", "22,80", arguments="-sV -sC")

with open('report.txt', 'w') as f:
    f.write(timestamp)
    for host in nm.all_hosts():
        line = f"Host: {host}\n"
        print(line, end='')
        f.write(line)
        for proto in nm[host].all_protocols():
            for port in nm[host][proto].keys():
                state = nm[host][proto][port]["state"]
                service = nm[host][proto][port]['name']
                version = nm[host][proto][port]['version']
                line = f"  [{state.upper()}] {proto}/{port} - {service} {version}\n"
                print(line, end='')
                f.write(line)
print("報告已存入 report.txt")
