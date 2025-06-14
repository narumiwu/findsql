#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created By : Trinity Legion

import sys
import requests
import urllib3
import time
from termcolor import colored

# Matikan warning SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()

class warna:
    HEADER    = '\033[95m'
    BLUE      = '\033[94m'
    GREEN     = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'

# ASCII art baru untuk "Trinity Legion"
banner_lines = [
    "  _____           _        _        _               _           ",
    " |_   _|         (_)      | |      (_)             | |          ",
    "   | | ___   ___  _  ___  | |_ ___  _ _ __ ___   __| | ___ _ __ ",
    "   | |/ _ \\ / _ \\| |/ _ \\ | __/ _ \\| | '_ ` _ \\ / _` |/ _ \\ '__|",
    "   | | (_) | (_) | |  __/ | || (_) | | | | | | | (_| |  __/ |   ",
    "   \\_/\\___/ \\___/|_|\\___|  \\__\\___/|_|_| |_| |_|\\__,_|\\___|_|   ",
    "                _/ |                                            ",
    "               |__/                                             ",
    "                     Trinity Legion Exploit Scanner             "
]

# Animasi print banner
for line in banner_lines:
    for ch in line + "\n":
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.005)

print()  # satu baris kosong setelah banner

def main():
    print(warna.WARNING + "[!] Masukkan domain tanpa http:// atau https:// (contoh: example.com)" + warna.ENDC)
    site = input("[+] Enter Site: ").strip()
    time.sleep(1)
    print(warna.GREEN + "[+] Processing: " + site + warna.ENDC)

    try:
        with open('data.txt', 'r') as f:
            paths = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(warna.FAIL + "[-] File data.txt tidak ditemukan." + warna.ENDC)
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
            print(warna.FAIL + f"[!] {url} — Request failed" + warna.ENDC)
            continue

        if resp.status_code == 200:
            print(warna.GREEN + "[+] Yeay! Found it:\n    " + resp.url + warna.ENDC)
            keluar = input("[+] Mau berhenti? (y/n): ").strip().lower()
            if keluar == 'y':
                print(warna.GREEN + "[+] Job Done! Bye! 😊" + warna.ENDC)
                sys.exit(0)
            else:
                print(warna.FAIL + "[!] Lanjut scanning..." + warna.ENDC)
        else:
            print(warna.FAIL + f"[!] {url} — Not Found ({resp.status_code})" + warna.ENDC)

    print("[+] Selesai, bye! 😴")

if __name__ == "__main__":
    main()
