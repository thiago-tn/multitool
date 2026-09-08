from modules.portscan import port_scan
from modules.hash import verify_hash
from modules.passgen import password_generator
from modules.sysinfo import export_system_info, get_system_info

def menu():

    while True:

        print("""
==============================
  ..eeeee..
 e8"   8   "8e
d8     8     8b
8!   .dWb.   !8
Y8 .e* 8 *e. 8P
 *8*   8   *8*
   **ee8ee**
Multitool by Th
==============================

1 - Port Scanner
2 - Hash Checker
3 - Gerador de Senhas
4 - Informações do Sistema
0 - Sair
""")

        opcao = input("Escolha: ")

        if opcao == "1":

            host = input("Host: ")

            inicio = int(input("Porta inicial: "))

            fim = int(input("Porta final: "))

            abertas = port_scan(host, inicio, fim)

            print()

            print("Portas abertas:", abertas)

        elif opcao == "0":

            print("exit program")

            break

        elif opcao == "2":

            caminho = input("Caminho do arquivo: ")

            esperado = input("Hash SHA-256 esperado: ")

            try:
                resultado = verify_hash(caminho, esperado)
                print("Hash verificado com sucesso." if resultado else "Hash inválido ou arquivo alterado.")
            except FileNotFoundError:
                print("Arquivo não encontrado.")

        elif opcao == "3":

            try:
                print("Senha gerada:", password_generator())
            except ValueError as erro:
                print(erro)

        elif opcao == "4":

            informacoes = get_system_info()
            print("\nInformações do sistema:")
            for nome, valor in informacoes.items():
                print(f"{nome}: {valor}")

            try:
                arquivo = export_system_info(info=informacoes)
                print(f"\nArquivo criado: {arquivo}")
            except PermissionError:
                print("Não foi possível criar o arquivo sysinfo.xlsx.")

        else:

            print("Opção inválida")
if __name__ == "__main__":
    menu()
    