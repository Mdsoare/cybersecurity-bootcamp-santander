# -*- coding: utf-8 -*-
'''
File: bufferOverFloeIP.py
Author: Marcelo Soares
Description: Neste exemplo, o usuário insere um endereço IP. 
No entanto, o código não verifica o comprimento do endereço IP antes de tentar analisá-lo. 
Se o usuário inserir uma string muito longa, isso poderia levar a um buffer overflow e um 
erro de exceção não tratada.
'''

import ipaddress

def parse_ip(ip_input):
    try:
        ip = ipaddress.ip_address(ip_input)
        return f"Endereço IP válido: {ip}"
    except ValueError:
        return "Endereço IP inválido"

ip_input = input("Digite um endereço IP: ")
result = parse_ip(ip_input)
print(result)