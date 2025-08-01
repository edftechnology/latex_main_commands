import subprocess

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Command executed successfully: {command}")
    except subprocess.CalledProcessError:
        print(f"Failed to execute command: {command}")

def main():
    # Lista de comandos para instalar e configurar Tex Live e fazer a limpeza do sistema
    commands = [
        "sudo apt clean",
        "sudo apt autoclean",
        "sudo apt autoremove -y",
        "sudo apt update",
        "sudo apt --fix-broken install",
        "sudo apt clean",
        "sudo apt list --upgradable",
        "sudo apt full-upgrade -y",
        "sudo apt install texstudio -y",
        "texstudio --version"
    ]

    for command in commands:
        run_command(command)

    print("Installation and system maintenance are complete.")

if __name__ == "__main__":
    main()

# [1] OPEN AI.
# ***Instalar o tex live no linux ubuntu.***
# Disponível em: <https://chat.openai.com/c/5341e112-5d65-410b-bec5-00b9a61a6650> (texto adaptado).
# ChatGPT.
# Acessado em: 29/09/2023 18:56.
