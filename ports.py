#!/usr/bin/env python3
import psutil
import colorama

colorama.init(autoreset=True)

def print_conns(proto_name, conns):
    print(colorama.Fore.MAGENTA + f"=== {proto_name} Connections ===")
    print(colorama.Fore.CYAN + f"{'Protocol':<9} {'Local Address':<30} {'Remote Address':<30} {'Status':<15}")
    for conn in conns:
        laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else ""
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else ""
        print(colorama.Fore.GREEN + f"{proto_name:<9} {laddr:<30} {raddr:<30} {conn.status:<15}")

# Fetch all network connections
all_conns = psutil.net_connections(kind='inet')

# Separate TCP and UDP connections
tcp_conns = [c for c in all_conns if c.type == 1]   # SOCK_STREAM
udp_conns = [c for c in all_conns if c.type == 2]   # SOCK_DGRAM

# Sort connections by status
tcp_conns = sorted(tcp_conns, key=lambda c: c.status)
udp_conns = sorted(udp_conns, key=lambda c: c.status)

# Print connections
print_conns("TCP", tcp_conns)
print()  # Blank line between sections
print_conns("UDP", udp_conns)
print()  # Final blank line
