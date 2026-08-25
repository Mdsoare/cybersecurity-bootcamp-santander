# -*- coding: utf-8 -*-
'''
File: verificarMeuIpExterno.py
Author: Marcelo Soares
Description: Script para identificar o IP externo
Requirement: pip install requests
'''
import requests


def obter_dados_ip():
    try:
        url = 'https://ipinfo.io/json'
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()
        return dados
    except Exception as e:
        print(f'Erro ao obter dados do IP externo: {e}')
        return None


def exibir_dados_ip(dados):
    if dados:
        ip = dados.get('ip', 'N/A')
        org = dados.get('org', 'N/A')
        cid = dados.get('city', 'N/A')
        pais = dados.get('country', 'N/A')
        regiao = dados.get('region', 'N/A')

        print('Detalhes do IP externo\n')
        print(f'IP: {ip}\nRegião: {regiao}\nPaís: {pais}\nCidade: {cid}\nOrg: {org}')
    else:
        print('Não foi possível obter os dados do IP externo.')


if __name__ == '__main__':
    dados_ip = obter_dados_ip()
    exibir_dados_ip(dados_ip)
    