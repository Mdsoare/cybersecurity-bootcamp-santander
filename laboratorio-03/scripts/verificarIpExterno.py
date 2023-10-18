# -*- coding: utf-8 -*-
'''
File: verificarIpExterno.py
Author: Marcelo Soares
Description: Script para obter informações do IP externo ou de um IP específico
Requirement: pip install requests
'''
import json
import requests

def obter_dados_ip(ip=None):
    if ip:
        url = f'https://ipinfo.io/{ip}/json'
    else:
        url = 'https://ipinfo.io/json'

    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            return dados
        else:
            print(f'Erro ao obter dados do IP: Status Code {resposta.status_code}')
            return None
    except Exception as e:
        print(f'Erro ao obter dados do IP: {e}')
        return None

def exibir_dados_ip(dados):
    if dados:
        ip = dados['ip']
        org = dados['org']
        cid = dados['city']
        pais = dados['country']
        regiao = dados['region']

        print('Detalhes do IP\n')
        print(f'IP: {ip}\nRegião: {regiao}\nPaís: {pais}\nCidade: {cid}\nOrg: {org}')
    else:
        print('Não foi possível obter os dados do IP.')

if __name__ == '__main__':
    ip = input('Digite um IP (ou deixe em branco para usar o IP externo): ')
    dados_ip = obter_dados_ip(ip)
    exibir_dados_ip(dados_ip)
