#!/usr/local/bin/python
# code by Ari
# xploit-db



import os, sys

def menu():

  print("""

  /$$                                                                 /$$                       /$$               /$$ /$$
  | $$                                                                |__/                      | $$              | $$| $$
 /$$$$$$    /$$$$$$   /$$$$$$  /$$$$$$/$$$$  /$$   /$$ /$$   /$$       /$$ /$$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$ | $$| $$  /$$$$$$   /$$$$$$
|_  $$_/   /$$__  $$ /$$__  $$| $$_  $$_  $$| $$  | $$|  $$ /$$/      | $$| $$__  $$ /$$_____/|_  $$_/   |____  $$| $$| $$ /$$__  $$ /$$__  $$
  | $$    | $$$$$$$$| $$  \__/| $$ \ $$ \ $$| $$  | $$ \  $$$$/       | $$| $$  \ $$|  $$$$$$   | $$      /$$$$$$$| $$| $$| $$$$$$$$| $$  \__/
  | $$ /$$| $$_____/| $$      | $$ | $$ | $$| $$  | $$  >$$  $$       | $$| $$  | $$ \____  $$  | $$ /$$ /$$__  $$| $$| $$| $$_____/| $$
  |  $$$$/|  $$$$$$$| $$      | $$ | $$ | $$|  $$$$$$/ /$$/\  $$      | $$| $$  | $$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$| $$|  $$$$$$$| $$
   \___/   \_______/|__/      |__/ |__/ |__/ \______/ |__/  \__/      |__/|__/  |__/|_______/    \___/   \_______/|__/|__/ \_______/|__/
                                                                                                                                        V.1.0

          ========================================
           1. THC-Hydra install
           2. Metasploit install
           3. Nethunter install
           4. Ubuntu install
           5. Fedora install
           6. Beef-Xss install
           7. Nmap install
           8. Xerosploit install
           9. Dirhunt install
           10. Wapiti install
           11. Shodan install
         -----------------------------------------
           0. Exit
         ==========================================
""")

def main():
    while True:
          try:
              jancok = raw_input("install~#: ")
              if jancok == "1":
                os.system("cd /data/data/com.termux/files/home")
                os.system("pkg update -y")
                os.system("pkg install -y hydra")
                os.system("cd /data/data/com.termux/files/home")
                print("====================================")
                print("[+] THC-Hydra success install")
                print("====================================")
                menu()
                main()
              elif jancok == "2":
                os.system("pkg install -y wget")
                os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
                os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
                os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
                os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
                os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
                os.system("cd /data/data/com.termux/files/home/metasploit-framework && bundle install")
                os.system("cd /data/data/com.termux/files/home/metasploit-framework && bundle update nokogiri")
                os.system("cd /data/data/com.termux/files/home/")
                print("====================================")
                print("[+] Metasploit success install")
                print("====================================")
                main()
              elif jancok == "3":
                os.system("pkg update -y")
                os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Nethunter-In-Termux.git")
                os.system("cd /data/data/com.termux/files/home && cd Nethunter-In-Termux && chmod +x kalinethunter")
                os.system("cd /data/data/com.termux/files/home")
                print("====================================")
                print("[+] Nethunter success install")
                print("====================================")
                menu()
                main()
              elif jancok == "4":
                os.system("pkg update -y")
                os.system("pkg install -y git")
                os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Neo-Oli/termux-ubuntu.git")
                os.system("cd /data/data/com.termux/files/home && cd termux-ubuntu && bash ubuntu.sh")
                print("====================================")
                print("[+] Ubuntu success install")
                print("====================================")
                menu()
                main()
              elif jancok == "5":
                os.system("pkg update -y")
                os.system("pkg install -y git")
                os.system("pkg install -y wget")
                os.system("apt update && apt install wget -y && /data/data/com.termux/files/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh")
                print("====================================")
                print("[+] Fedora success install")
                print("====================================")
                menu()
                main()
              elif jancok == "6":
                os.system("cd /data/data/com.termux/files/home")
                os.system("pkg update -y")
                os.system("pkg install nano")
                os.system("pkg install python -y")
                os.system("pkg install python2 -y")
                os.system("pkg install cat -y")
                os.system('mkdir -p $PREFIX/etc/apt/sources.list.d && printf "deb [trusted=yes] https://hax4us.github.io/termux-tools/ extras main" > $PREFIX/etc/apt/sources.list.d/hax4us.list')
                os.system("pkg update")
                os.system("pkg install beef-xss")
                os.system("cd /data/data/com.termux/files/home")
                print("=============================")
                print("[+] Beef-Xss success install")
                print("=============================")
                menu()
                main()
              elif jancok == "7":
                os.system("cd /data/data/com.termux/files/home")
                os.system("pkg update -y")
                os.system("pkg install -y nmap")
                os.system("cd /data/data/com.termux/files/home")
                print("===========================")
                print("[+] Nmap success install")
                print("===========================")
                menu()
                main()
              elif jancok == "8":
                os.system("cd /data/data/com.termux/files/home")
                os.system("pkg update -y")
                os.system('mkdir -p $PREFIX/etc/apt/sources.list.d && printf "deb [trusted=yes] https://hax4us.github.io/termux-tools/ extras main" > $PREFIX/etc/apt/sources.list.d/hax4us.list')
                os.system("pkg update")
                os.system("cd /data/data/com.termux/files/home")
                os.system("pkg install xerosploit")
                print("==========================")
                print("[+] Xerosploit success install")
                print("==========================")
                menu()
                main()
              elif jancok == "9":
                os.system("cd /data/data/com.termux/files/home")
                os.system("pkg update -y")
                os.system("pkg install python -y")
                os.system("pkg install python pip")
                os.system("pkg install --upgrade pip")
                os.system("pip install dirhunt")
                print("===========================")
                print("[+] Dirhunt success install")
                print("===========================")
                menu()
                main()
              elif jancok == "10":
                os.system("cd /data/data/com.termux/files/home")
                os.system("pkg update -y")
                os.system("pkg install python -y")
                os.system("pkg install python pip")
                os.system("pkg install --upgrade pip")
                os.system("pip install wapiti3")
                print("============================")
                print("[+] wapiti success install ")
                print("Usage: wapiti -h")
                print("===========================")
                menu()
                main()
              elif jancok == "11":
                os.system("cd /data/data/com.termux/files/home")
                os.system("pkg update -y")
                os.system("pkg install python -y")
                os.system("pkg install python pip")
                os.system("pkg install --upgrade pip")
                os.system("pip install shodan")
                print("============================")
                print("[+] Shodan success install ")
                print("============================")
                menu()
                main()
              elif jancok == "0":
                time.sleep(2)
                print("EXITS...")
                exit()

              else:
                  print "Wrong Command => ", jancok
                  main()
          except(KeyboardInterrupt):
              print("\n[*] (Ctrl + C ) Detected, Trying To Exit ..." )
              print("[*] Thank You For Using Termux installer)" )
              exit()

if __name__ == "__main__":
    menu()
    main()
