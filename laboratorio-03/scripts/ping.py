# -*- coding: utf-8 -*-
'''
File: ping.py
Author: Marcelo Soares
Description: Desenvolvendo um script para executar um ping a partir de um arquivo 'host.txt'
'''

import platform
import subprocess
import time


def ping_hosts_from_file(filename):
    '''
    Ping IP addresses from a file.

    Args:
        filename (str): Name of the file containing a list of IP addresses.

    '''
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            host_list = file.read().splitlines()

        param = '-n' if platform.system() == 'Windows' else '-c'

        for ip in host_list:
            # Ignora linhas em branco no arquivo de hosts
            if not ip.strip():
                continue

            print(f'Verificando o IP: {ip}')
            print('-' * 60)

            try:
                subprocess.run(['ping', param, '2', ip], check=True)
            except subprocess.CalledProcessError:
                print(f'Falha ao responder o ping para o IP: {ip}')

            print('=' * 60)
            time.sleep(5)
    except FileNotFoundError:
        print(f'O arquivo {filename} não foi encontrado.')


if __name__ == "__main__":
    host_file = 'host.txt'
    ping_hosts_from_file(host_file)
