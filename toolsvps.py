import os
import colorama
from colorama import Fore
import time

def menu_utama():
    while True:
        os.system("clear")
        print(''' _____    _                _____                   
|  ___|__| |__  _ __ _   _| ____|_ __  ___ ________
| |_ / _ \ '_ \| '__| | | |  _| | '_ \/ __|_  /_  /
|  _|  __/ |_) | |  | |_| | |___| | | \__ \/ / / / 
|_|  \___|_.__/|_|   \__, |_____|_| |_|___/___/___|
                     |___/                         ''')
        print("=== Menu Tools VPS ===")
        print(" ")
        print("1. Auto Install [Free]")
        print("2. Rebuild VPS [Little Problem]")
        print("3. Keluar")
        
        pilihan = input(Fore.RED + '''┌──(root㉿Febry404)-[~]\n└─# ''' + Fore.RESET)
        
        if pilihan == "1":
            setup_ssh()
        elif pilihan == "2":
            menu_rebuild_vps()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan Tools VPS")
            time.sleep(2)
            print("Keluar dari Tools VPS")
            break
        else:
            print("Input Invaild")

def setup_ssh():
    while True:
        os.system("clear")
        print(''' _____    _                _____                   
|  ___|__| |__  _ __ _   _| ____|_ __  ___ ________
| |_ / _ \ '_ \| '__| | | |  _| | '_ \/ __|_  /_  /
|  _|  __/ |_) | |  | |_| | |___| | | \__ \/ / / / 
|_|  \___|_.__/|_|   \__, |_____|_| |_|___/___/___|
                     |___/                         ''')
        print("Ohh Iya Semua Auto Install Dari Github Jadi Gada Campur Tangan Sama Saya")
        print("=== Menu Auto Install ===")
        print("1. UDP")
        print("2. SSH & VMESS")
        print("3. HYSTRIA")
        print("4. Kembali Kemenu Utama")
        
        pilihan = input(Fore.RED + '''┌──(root㉿Febry404)-[~]\n└─# ''' + Fore.RESET)
        
        if pilihan == "1":
            auto_udp()
        elif pilihan == "2":
            auto_ssh()
        elif pilihan == "3":
            auto_hystria()
        elif pilihan == "4":
            break
        else:
            print("Input Invalid")

def auto_hystria():
    os.system('''wget https://github.com/khaledagn/AGN-UDP/raw/main/install_agnudp.sh")
    os.system("chmod +x install_agnudp.sh; ./install_agnudp.sh''')
    exit()
    
def auto_udp():
    os.system('''wget "https://raw.githubusercontent.com/prjkt-nv404/UDP-Custom-Installer-Manager/main/install.sh" -O install.sh && chmod +x install.sh && ./install.sh''')
    exit()

def auto_ssh():
    os.system('''apt update && apt upgrade -y && apt install -y wget screen && wget -q https://raw.githubusercontent.com/scvps/scriptvps/main/setup.sh && chmod +x setup.sh && screen -S setup ./setup.sh''')
    exit()
   
def menu_rebuild_vps():
    while True:
        os.system("clear")
        print(''' _____    _                _____                   
|  ___|__| |__  _ __ _   _| ____|_ __  ___ ________
| |_ / _ \ '_ \| '__| | | |  _| | '_ \/ __|_  /_  /
|  _|  __/ |_) | |  | |_| | |___| | | \__ \/ / / / 
|_|  \___|_.__/|_|   \__, |_____|_| |_|___/___/___|
                     |___/                         ''')
        print("=== Menu Rebuild VPS ===")
        print(" ")
        print("1. DigitalOcean")
        print("2. Linode")
        print("3. Vultr")
        print("4. Kembali ke Menu Utama")
        
        pilihan = input(Fore.RED + '''┌──(root㉿Febry404)-[~]\n└─# ''' + Fore.RESET)
        
        if pilihan == "1":
            rebuild_digitalocean()
        elif pilihan == "2":
            rebuild_linode()
        elif pilihan == "3":
            rebuild_vultr()
        elif pilihan == "4":
            break
        else:
            print("Input Invaild")

def rebuild_digitalocean():
    print("Rebuild VPS DigitalOcean")
    os.system("doctl compute droplet-action rebuild <droplet_id> --image <image_id>")

def rebuild_linode():
    print("Rebuild VPS Linode")
    os.system("linode-cli linodes rebuild <linode_id> --image <image_id>")

def rebuild_vultr():
    print("Rebuild VPS Vultr")
    os.system("vultr-cli compute instance rebuild <instance_id> --image <image_id>")

menu_utama()