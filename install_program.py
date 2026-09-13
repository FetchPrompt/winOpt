import subprocess
from clear import clear

apps = {
    "1": ("Google Chrome", "Google.Chrome"),
    "2": ("Steam", "Valve.Steam"),
    "3": ("OBS Studio", "OBSProject.OBSStudio"),
    "4": ("Discord", "Discord.Discord"),
    "5": ("Tor Browser", "TorProject.TorBrowser"),
    "6": ("Firefox", "Mozilla.Firefox"),
    "7": ("Brave", "Brave.Brave"),
    "8": ("Visual Studio Code", "Microsoft.VisualStudioCode"),
    "9": ("Vim", "vim.vim"),
    "10": ("Neovim", "Neovim.Neovim"),
    "11": ("Spotify", "Spotify.Spotify"),
    "12": ("VLC Player", "VideoLAN.VLC"),
    "13": ("InkScape", "Inkscape.Inkscape"),
    "14": ("Audacity", "Audacity.Audacity"),
    "15": ("uTorrent", "BitTorrent.uTorrent"),
    "16": ("Git", "Git.Git"),
    "17": ("GIMP", "GIMP.GIMP"),
    "18": ("Krita", "Krita.Krita"),
    "19": ("WhatsApp", "WhatsApp.WhatsApp"),
    "20": ("7Zip", "7zip.7zip")
}

def install_program(package_id):
    print(f"Starting installation for {package_id}...")
    
    command = ["winget", "install", "-e", "--id", package_id, "--silent", "--accept-source-agreements", "--accept-package-agreements"]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"Successfully installed {package_id}!")
        if result.stdout:
            print(f"\nOutput: \n{result.stdout}")
        if result.stderr:
            print(f"\nWarnings: \n{result.stderr}")

        input("Press ENTER to get back...")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_id}.")
        print(f"\nReturn Code: \n{e.returncode}")
        if e.stdout:
            print(f"\nOutput: \n{e.stdout}")
        if e.stderr:
            print(f"\nError Output: \n{e.stderr}")

        input("Press ENTER to get back...")

def app_selection():
    app_selector = """
Choose an app to install:
[1] Google Chrome
[2] Steam
[3] OBS Studio
[4] Discord
[5] Tor Browser
[6] Firefox
[7] Brave
[8] Visual Studio Code
[9] Vim
[10] NeoVim
[11] Spotify
[12] VLC Player
[13] InkScape
[14] Audacity
[15] uTorrent
[16] Git
[17] GIMP
[18] Krita
[19] WhatsApp
[20] 7Zip
[0] Exit
"""
    clear()
    print(app_selector)
    app_selected = input("Enter an option: ").strip().lower()
    if app_selected == "0":
        input("Press ENTER to go back...")

    if app_selected in apps:
        app_name, package_id = apps[app_selected]
        print(f"Selected {app_name}")
        install_program(package_id)
    else:
        print("Invalid option.")
        print("Press ENTER to return...")