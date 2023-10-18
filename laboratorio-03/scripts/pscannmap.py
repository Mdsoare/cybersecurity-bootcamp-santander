# -*- coding: utf-8 -*-
'''
File: port_scanner.py
Author: Marcelo Soares
Description: Script para varredura de portas TCP/UDP com python-nmap
Requirement: sudo apt install -y nmap && pip install python-nmap
'''
import nmap

def realizar_varredura(ip, portas, tipo_varredura):
    scanner = nmap.PortScanner()

    if tipo_varredura == "1":
        scanner.scan(ip, portas, '-v -sT')  # TCP Connect Scan
    elif tipo_varredura == "2":
        scanner.scan(ip, portas, '-v -sU')  # UDP Scan
    elif tipo_varredura == "3":
        scanner.scan(ip, portas, '-v -sS')  # TCP SYN Scan
    else:
        print("Opção de varredura inválida.")
        return

    for host in scanner.all_hosts():
        print(f"Varredura para o host: {host}")
        for proto in scanner[host].all_protocols():
            print(f"Protocolo: {proto}")
            port_list = scanner[host][proto].keys()
            for port in port_list:
                state = scanner[host][proto][port]['state']
                print(f"Porta {port}: {state}")

if __name__ == '__main__':
    print("Bem-vindo ao Port Scanner com python-nmap!")
    print("<---------------------------------------->")

    ip = input("Digite o host ou ip: ")
    print(f'O host/ip digitado foi: {ip}')

    portas = input("Digite a faixa de portas (por exemplo, '1-1024'): ")
    tipo_varredura = input("""Tipos de varredura disponíveis:
        1 -> TCP Connect Scan
        2 -> UDP Scan
        3 -> TCP SYN Scan
        Selecione uma opção:  """)

    print(f'Sua escolha foi a opção {tipo_varredura}')

    realizar_varredura(ip, portas, tipo_varredura)
