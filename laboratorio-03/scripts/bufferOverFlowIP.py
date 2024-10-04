# -*- coding: utf-8 -*-
'''
File: bufferOverFlowIP.py
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

'''
# REMEDIAÇÃO: Para remediar essa vulnerabilidade, podemos adicionar uma verificação do comprimento da string antes de passá-la para a função 'ipaddress.ip_address'

import ipaddress

MAX_IP_LENGTH = 15  # Limite máximo para o comprimento de um endereço IPv4

def parse_ip(ip_input):
    if len(ip_input) > MAX_IP_LENGTH:
        return "Endereço IP muito longo"

    try:
        ip = ipaddress.ip_address(ip_input)
        return f"Endereço IP válido: {ip}"
    except ValueError:
        return "Endereço IP inválido"

ip_input = input("Digite um endereço IP: ")
result = parse_ip(ip_input)
print(result)

'''