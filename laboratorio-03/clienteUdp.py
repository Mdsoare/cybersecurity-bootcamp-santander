# -*- coding: utf-8 -*-
'''
File: clienteUcp.py
Author: Marcelo Soares
Description: Desenvolvendo um script para executar um cliente local UDP
'''

import socket


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Socket criado com sucesso")

        # input("Digite o host ou IP a ser conectado: ")
        hostAlvo = 'localhost'
        portAlvo = 5432  # int(input("Digite a porta a ser conectada: "))
        # input("Digite a mensagem a ser enviada: ")
        mensagem = 'Cliente: Olá servidor! E aí... Tudo blz?\n'

        print(f'Cliente: {hostAlvo}')
        s.sendto(mensagem.encode(), (hostAlvo, portAlvo))

        dados, server = s.recvfrom(4096)
        dados = dados.decode()
        print(f'Cliente: {dados}')
    except socket.error as e:
        print(f"Erro no socket: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        print("Cliente: Fechando a conexão")
        s.close()


if __name__ == "__main__":
    main()
