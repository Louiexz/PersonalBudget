import subprocess
import sys
import os


def run_command(command, env=None):
    """Executa um comando shell e retorna o status e a saída."""
    result = subprocess.run(
        command, shell=True, env=env, text=True, capture_output=True
    )
    return result.returncode, result.stdout, result.stderr


def main():
    # Caminho para o ambiente virtual e o comando Python a ser executado
    venv_path = "/home/luxz/Documentos/Codes/Python/Django/myproject/.venv"
    command = "python3 manage.py runserver"

    # Define o ambiente virtual
    env = os.environ.copy()
    env["PATH"] = f"{venv_path}/bin:" + env["PATH"]
    env["VIRTUAL_ENV"] = venv_path

    # Ativa o ambiente virtual e executa o comando
    print("Ativando o ambiente virtual e executando o comando...")
    returncode, stdout, stderr = run_command(command, env)

    # Exibe a saída do comando
    print(stdout)
    if returncode != 0:
        print(f"Erro ao executar o comando: {stderr}", file=sys.stderr)

    print("Desativando o ambiente virtual...")


if __name__ == "__main__":
    main()
