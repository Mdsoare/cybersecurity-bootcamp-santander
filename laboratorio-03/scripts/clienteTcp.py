# -*- coding: utf-8 -*-
'''
File: clienteTcp.py
Author: Marcelo Soares
Description: Desenvolvendo um script para executar um cliente TCP
'''

import socket


def create_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return s
    except socket.error as e:
        print("Falha ao criar o socket")
        print("Erro: {}".format(e))
        raise


def connect_to_server(s, host, port):
    try:
        s.connect((host, port))
        print("Cliente TCP conectado com sucesso!")
        s.shutdown(socket.SHUT_RDWR)
    except (ConnectionRefusedError, TimeoutError) as e:
        print(f"Não foi possível conectar ao host {host}:{port}")
        print("Erro: {}".format(e))
        raise


def main():
    try:
        s = create_socket()

        print("Socket criado com sucesso")

        hostAlvo = input("Digite o host ou IP a ser conectado: ")
        portAlvo = int(input("Digite a porta a ser conectada: "))

        connect_to_server(s, hostAlvo, portAlvo)
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        s.close()


if __name__ == "__main__":
    main()
