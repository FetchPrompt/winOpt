import subprocess
from clear import clear

def network_reset():
    clear()
    subprocess.run(["netsh", "winsock", "reset"], check=True)
    subprocess.run(["netsh", "int", "ip", "reset"], check=True)
    subprocess.run(["ipconfig", "/release"], check=True)
    subprocess.run(["ipconfig", "/renew"], check=True)
    subprocess.run(["ipconfig", "/flushdns"], check=True)
