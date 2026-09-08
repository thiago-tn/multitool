import socket

def port_scan(alvo, inicio, fim):
    portas_abertas = []

    print(f"\nEscaneando {alvo}\n")

    for porta in range(inicio, fim + 1):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            sock.settimeout(1)

            if sock.connect_ex((alvo, porta)) == 0:

                portas_abertas.append(porta)
                print(f"[+] {porta} aberta")

    return portas_abertas
   
        