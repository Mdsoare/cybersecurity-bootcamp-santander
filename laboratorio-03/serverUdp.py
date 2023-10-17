# -*- coding: utf-8 -*-
'''
File: clienteUcp.py
Author: Marcelo Soares
Description: Desenvolvendo um script para executar um servidor local UDP
'''

import socket


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Socket criado com sucesso")

        # hostAlvo = input("Digite o host ou IP a ser conectado: ")
        # portAlvo = int(input("Digite a porta a ser conectada: "))
        host = 'localhost'
        porta = 5432

        s.bind((host, porta))
        mensagem = 'Servidor: Olá cliente, e aí... blz?'

        while True:
            dados, endereco = s.recvfrom(4096)

            if dados:
                print("Servidor enviando mensagem...")
                s.sendto(dados + mensagem.encode(), endereco)
    except socket.error as e:
        print(f"Erro no socket: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        s.close()


if __name__ == "__main__":
    main()
