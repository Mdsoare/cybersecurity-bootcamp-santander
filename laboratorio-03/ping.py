# -*- coding: utf-8 -*-
'''
File: ping.py
Author: Marcelo Soares
Description: Desenvolvendo um script para executar um ping a partir de um arquivo 'host.txt'
'''

import os
import time
import platform


def ping_hosts_from_file(filename):
    '''
    Ping IP addresses from a file.

    Args:
        filename (str): Name of the file containing a list of IP addresses.

    '''
    try:
        with open(filename, 'r') as file:
            host_list = file.read().splitlines()

        for ip in host_list:
            print(f'Verificando o IP: {ip}')
            print('-' * 60)

            if platform.system() == 'Windows':
                os.system(f'ping -n 2 {ip}')
            else:
                os.system(f'ping -c 2 {ip}')

            print('=' * 60)
            time.sleep(5)
    except FileNotFoundError:
        print(f'O arquivo {filename} não foi encontrado.')


if __name__ == "__main__":
    host_file = 'host.txt'
    ping_hosts_from_file(host_file)
