# -*- coding: utf-8 -*-
"""
File: verificarIpExterno.py
Author: Marcelo Soares
Description: Script para obter informações do IP externo ou de um IP específico
Requirement: pip install requests
"""

import requests


def obter_dados_ip(ip=None):
    if ip:
        url = f"https://ipinfo.io/{ip}/json"
    else:
        url = "https://ipinfo.io/json"

    try:
        resposta = requests.get(url, timeout=10)
        if resposta.status_code == 200:
            return resposta.json()

        print(f"Erro ao obter dados do IP: Status Code {resposta.status_code}")
        return None
    except Exception as e:
        print(f"Erro ao obter dados do IP: {e}")
        return None


def exibir_dados_ip(dados):
    if dados:
        ip = dados.get("ip", "N/A")
        org = dados.get("org", "N/A")
        cid = dados.get("city", "N/A")
        pais = dados.get("country", "N/A")
        regiao = dados.get("region", "N/A")

        print("Detalhes do IP\n")
        print(f"IP: {ip}\nRegião: {regiao}\nPaís: {pais}\nCidade: {cid}\nOrg: {org}")
    else:
        print("Não foi possível obter os dados do IP.")


if __name__ == "__main__":
    ip_alvo = input(
        "Digite um IP (ou deixe em branco para usar o IP externo): "
    ).strip()
    dados_ip = obter_dados_ip(ip_alvo if ip_alvo else None)
    exibir_dados_ip(dados_ip)
