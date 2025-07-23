import os
import subprocess
from datetime import datetime
from colorama import Fore, Style, init

init()

TOOLS_PATH = os.path.abspath(os.getcwd())
DATE = datetime.now().strftime("%Y%m%d")

def build_output_path(tool, target):
    folder = os.path.join(TOOLS_PATH, tool)
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, f"{tool}_{target}_{DATE}.txt")

def print_banner():
    print(Fore.MAGENTA + """
██████╗ ██╗   ██╗ ██████╗     ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
██╔══██╗██║   ██║██╔════╝     ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
██████╔╝██║   ██║██║  ███╗    ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
██╔══██╗██║   ██║██║   ██║    ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝╚██████╔╝    ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
╚═════╝  ╚═════╝  ╚═════╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                                                                                    
    """ + Style.RESET_ALL)
    print(Fore.YELLOW + "  by Bob Marley  |  " + Fore.LIGHTYELLOW_EX + "@marleyybob123\n")

def print_menu():
    print(f"{Fore.CYAN}🔎 Enter domain to recon (e.g. domain.com):{Style.RESET_ALL} ", end='')

def print_options():
    print(f"\n{Fore.CYAN}Choose your option (1–7):{Style.RESET_ALL}")
    print(Fore.CYAN + "-------------------------------" + Style.RESET_ALL)
    print(Fore.CYAN + "[1] Run Subfinder")
    print("[2] Run Httpx")
    print("[3] Run Paramspider")
    print("[4] Run FFUF")
    print("[5] Run Dalfox")
    print("[6] Run Sqlmap URL filter")
    print("[7] Run ALL steps" + Style.RESET_ALL)

def run_subfinder(target):
    print(Fore.GREEN + "\n[1] Running Subfinder..." + Style.RESET_ALL)
    output = build_output_path("Subfinder", target)
    subprocess.run(f"subfinder -d {target} -silent > \"{output}\"", shell=True)
    if os.path.isfile(output):
        with open(output, "r") as f:
            lines = f.readlines()
            count = len(lines)
        print(Fore.LIGHTGREEN_EX + f"[✔] Subfinder completed. {count} subdomains found.\n" + Style.RESET_ALL)
    else:
        print(Fore.RED + "[!] Subfinder failed or returned no output.\n")

def run_httpx(target):
    print(Fore.GREEN + "\n[2] Running Httpx (status code 200 only)..." + Style.RESET_ALL)
    subfinder_output = build_output_path("Subfinder", target)
    if not os.path.isfile(subfinder_output):
        print(Fore.RED + "[!] Skipping Httpx — no subdomains found.\n" + Style.RESET_ALL)
        return
    output = build_output_path("Httpx", target)
    cmd = f"httpx -l \"{subfinder_output}\" -sc -status-code -mc 200 -o \"{output}\""
    subprocess.run(cmd, shell=True)

def run_paramspider(target):
    print(Fore.GREEN + "\n[3] Running Paramspider crawling..." + Style.RESET_ALL)
    os.makedirs("results", exist_ok=True)
    cmd = f"python ../paramspider/main.py -d {target}"
    subprocess.run(cmd, shell=True)

def run_ffuf(target):
    print(Fore.GREEN + "\n[4] FFUF fuzzing endpoints..." + Style.RESET_ALL)
    paramspider_output = os.path.join("results", f"{target}.txt")
    if not os.path.isfile(paramspider_output):
        print(Fore.RED + "[!] Skipping FFUF — no Paramspider result found.\n" + Style.RESET_ALL)
        return
    output = build_output_path("FFUF", target)
    wordlist = "\"C:\\Users\\USER\\Documents\\Penting\\BUG BOUNTY\\SecLists\\Discovery\\Web-Content\\common.txt\""
    cmd = f"ffuf -u https://{target}/FUZZ -w {wordlist} -mc all -o \"{output}\" -of json"
    subprocess.run(cmd, shell=True)

def run_dalfox(target):
    print(Fore.GREEN + "\n[5] Dalfox scanning for XSS..." + Style.RESET_ALL)
    paramspider_output = os.path.join("results", f"{target}.txt")
    if not os.path.isfile(paramspider_output):
        print(Fore.RED + "[!] Skipping Dalfox — no Paramspider result found.\n" + Style.RESET_ALL)
        return
    output = build_output_path("Dalfox", target)
    cmd = f"dalfox file \"{paramspider_output}\" --only-poc r --output \"{output}\""
    subprocess.run(cmd, shell=True)

def run_sqlmap_filter(target):
    print(Fore.GREEN + "\n[6] SQLMap filtering possible SQLi URLs..." + Style.RESET_ALL)
    paramspider_output = os.path.join("results", f"{target}.txt")
    output = build_output_path("Sqlmap", target)
    if not os.path.isfile(paramspider_output):
        print(Fore.RED + "[!] Skipping SQLMap — no Paramspider result found.\n" + Style.RESET_ALL)
        return
    with open(paramspider_output, "r") as f:
        urls = [line.strip() for line in f if "?" in line and "=" in line]
    filtered_urls = [url for url in urls if url.startswith("http")]
    with open(output, "w") as out:
        for url in filtered_urls:
            out.write(url + "\n")
    print(Fore.YELLOW + f"[✓] Filtered {len(filtered_urls)} potential SQLi URLs.\n" + Style.RESET_ALL)


def main():
    print_banner()
    print_menu()
    target = input().strip()
    print_options()
    choice = input(f"\n👉 Your choice: ").strip()

    if choice == "1":
        run_subfinder(target)
    elif choice == "2":
        run_httpx(target)
    elif choice == "3":
        run_paramspider(target)
    elif choice == "4":
        run_ffuf(target)
    elif choice == "5":
        run_dalfox(target)
    elif choice == "6":
        run_sqlmap_filter(target)
    elif choice == "7":
        run_subfinder(target)
        run_httpx(target)
        run_paramspider(target)
        run_ffuf(target)
        run_dalfox(target)
        run_sqlmap_filter(target)
                # Recon Summary Paths
        sub_out    = build_output_path("Subfinder", target)
        alive_out  = build_output_path("Httpx", target)
        params_out = os.path.join("results", f"{target}.txt")
        ffuf_out   = build_output_path("FFUF", target)
        xss_out    = build_output_path("Dalfox", target)
        sql_out    = build_output_path("Sqlmap", target)

        # Print final recon completion summary
        print(f"""\n\033[92m
🎯 RECON COMPLETE — {target}
------------------------------------------------
📂 Subdomains      → {sub_out}
✅ Alive hosts     → {alive_out}
🔎 Params (FUZZ)   → {params_out}
🧨 FFUF results    → {ffuf_out}
🧬 XSS scan        → {xss_out}
🧪 SQLi targets    → {sql_out}
------------------------------------------------
\033[0m""")

    else:
        print(Fore.RED + "Invalid option. Exiting." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
