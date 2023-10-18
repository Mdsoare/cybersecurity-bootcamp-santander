# -*- coding: utf-8 -*-
'''
File: pscan.py
Author: Marcelo Soares
Description: Script para varredura de portas TCP
'''

import socket

def scan_port(host, port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(1)
        code = client.connect_ex((host, port))
        if code == 0:
            print(f'Porta {port} -> Aberta')
        else:
            print(f'Porta {port} -> Fechada')
        client.close()
    except Exception as e:
        print(f'Erro ao verificar porta {port}: {e}')

if __name__ == '__main__':
    host = input('Digite a URL: ')
    
    ports = []
    count = 0
    while count < 10:
        try:
            port = int(input('Digite a porta: '))
            if 1 <= port <= 65535:
                ports.append(port)
                count += 1
            else:
                print('A porta deve estar entre 1 e 65535.')
        except ValueError:
            print('Porta inválida. Digite um número válido.')

    print('Iniciando varredura...')
    for port in ports:
        scan_port(host, port)

    print('Fim da varredura!')