# -*- coding: utf-8 -*-
'''
File: ping.py
Author: Marcelo Soares
Description: Desenvolvendo um script para executar um ping a partir de um arquivo 'host.txt'
'''

import platform
import shutil
import subprocess  # nosec B404
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

        # Determina o executável com caminho absoluto para mitigar PATH hijacking
        ping_bin = shutil.which('ping') or ('ping' if platform.system() == 'Windows' else '/bin/ping')
        param = '-n' if platform.system() == 'Windows' else '-c'

        for ip in host_list:
            ip_clean = ip.strip()
            # Ignora linhas em branco no arquivo de hosts
            if not ip_clean:
                continue

            print(f'Verificando o IP: {ip_clean}')
            print('-' * 60)

            try:
                # Execução segura passando lista de argumentos explicitamente
                subprocess.run([ping_bin, param, '2', ip_clean], check=True)  # nosec B603
            except subprocess.CalledProcessError:
                print(f'Falha ao responder o ping para o IP: {ip_clean}')

            print('=' * 60)
            time.sleep(5)
    except FileNotFoundError:
        print(f'O arquivo {filename} não foi encontrado.')


if __name__ == "__main__":
    host_file = 'host.txt'
    ping_hosts_from_file(host_file)
