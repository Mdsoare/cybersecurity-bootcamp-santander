# -*- coding: utf-8 -*-
'''
File: ips.py
Author: Marcelo Soares
Description: Desenvolvendo um script para listar endereços IP em uma rede
'''
import ipaddress

def listar_enderecos_ip(rede):
    for endereco in rede:
        yield endereco # Para retornar valores parciais em vez de um único valor

def main():
    ip = "192.168.0.0/24"
    rede = ipaddress.ip_network(ip)

    print(f"Listando endereços IP na rede {rede}:")
    for endereco in listar_enderecos_ip(rede):
        print(endereco)

if __name__ == "__main__":
    main()