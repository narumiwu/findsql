#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created By : Trinity Legion

import os
import sys
import requests
import urllib3
import time
from termcolor import colored

# Matikan warning SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII art untuk "FIND SQL"
BANNER_LINES = [
    "  ______ _           _     ____  _____ _    _ ",
    " |  ____| |         | |   / __ \\|  __ \\ |  | |",
    " | |__  | | ___  ___| |_ | |  | | |  | | |  | |",
    " |  __| | |/ _ \\/ __| __|| |  | | |  | | |  | |",
    " | |    | |  __/\\__ \\ |_ | |__| | |__| | |__| |",
    " |_|    |_|\\___||___/\\__(_)____/|_____/ \\____/ ",
    "",
    "               by Trinity Legion                "
]

def print_banner():
    clear_terminal()
    for line in BANNER_LINES:
        for ch in line + "\n":
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(0.005)
    print()  # kosongkan satu baris

def main():
    print_banner()
    print(colored("[!] Masukkan domain tanpa http:// atau https:// (contoh: example.com)", "yellow"))
    site = input(colored("[+] Enter Site: ", "cyan")).strip()

    # setelah enter, bersihkan layar
    clear_terminal()
    print(colored(f"[+] Processing: {site}", "green"))
    print()

    try:
        with open('data.txt', 'r') as f:
            paths = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(colored("[-] File data.txt tidak ditemukan.", "red"))
        sys.exit(1)

    headers = {
        'User-Agent': (
            "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) "
            "AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 "
            "Mobile/15A372 Safari/604.1"
        )
    }

    for path in paths:
        url = f'http://{site}{path}'
        try:
            resp = requests.get(url, headers=headers, verify=False, timeout=10)
        except requests.RequestException:
            print(colored(f"[!] {url} — Request failed", "red"))
            continue

        if resp.status_code == 200:
            print(colored(f"[+] Yeay! Found it:\n    {resp.url}", "green"))
            again = input(colored("[+] Mau berhenti? (y/n): ", "cyan")).strip().lower()
            if again == 'y':
                print(colored("[+] Job Done! Bye! 😊", "green"))
                sys.exit(0)
            else:
                print(colored("[!] Lanjut scanning...", "red"))
        else:
            print(colored(f"[!] {url} — Not Found ({resp.status_code})", "red"))

    print(colored("[+] Selesai, bye! 😴", "cyan"))

if __name__ == "__main__":
    main()
