# -*- coding: utf-8 -*-
'''
File: webScraping.py
Author: Marcelo Soares
Description: Script para Web Scraping usando BeautifulSoup
Requirement: pip install requests BeautifulSoup4
'''

import requests
from bs4 import BeautifulSoup

def realizar_web_scraping(url, parser='lxml'):
    try:
        # Faz a solicitação HTTP e verifica se a resposta é bem-sucedida
        response = requests.get(url)
        response.raise_for_status()

        # Verifique o tipo de conteúdo da resposta para evitar parsing incorreto
        content_type = response.headers.get('Content-Type', '').lower()
        if 'html' not in content_type:
            print('A URL não contém conteúdo HTML.')
            return

        # 'soup' recebe o conteúdo HTML da URL
        soup = BeautifulSoup(response.content, parser)

        # Estruture os dados conforme necessário (exemplo: extrair links)
        links = [link['href'] for link in soup.find_all('a', href=True)]

        return links
    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação HTTP: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    url = input('Digite a URL: ')
    links = realizar_web_scraping(url)

    if links:
        print("Links encontrados:")
        for link in links:
            print(link)