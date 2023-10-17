# -*- coding: utf-8 -*-
'''
File: verificarMeuIpExterno.py
Author: Marcelo Soares
Description: Script para identificar o IP externo
Requirement: pip install urlopen
'''
import json
from urllib.request import urlopen

def obter_dados_ip():
    try:
        url = 'https://ipinfo.io/json'
        resposta = urlopen(url)
        dados = json.load(resposta)
        return dados
    except Exception as e:
        print(f'Erro ao obter dados do IP externo: {e}')
        return None

def exibir_dados_ip(dados):
    if dados:
        ip = dados['ip']
        org = dados['org']
        cid = dados['city']
        pais = dados['country']
        regiao = dados['region']

        print('Detalhes do IP externo\n')
        print(f'IP: {ip}\nRegião: {regiao}\nPaís: {pais}\nCidade: {cid}\nOrg: {org}')
    else:
        print('Não foi possível obter os dados do IP externo.')

if __name__ == '__main__':
    dados_ip = obter_dados_ip()
    exibir_dados_ip(dados_ip)
