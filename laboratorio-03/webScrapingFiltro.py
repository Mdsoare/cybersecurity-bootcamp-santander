# -*- coding: utf-8 -*-
'''
File: webScrapingFiltro.py
Author: Marcelo Soares
Description: Script para Web Scraping usando BeautifulSoup
Requirement: pip install requests BeautifulSoup4
'''
import requests
from bs4 import BeautifulSoup

# url = input("Digite a URL: ")
url = "https://www.climatempo.com.br/"
site = requests.get(url).content
soup = BeautifulSoup(site, 'html.parser')

# Use uma lista de classes CSS para acessar o elemento
# temperatura = soup.find("span", class_=["_block", "_margin-b-5", "-gray"])
# temperatura = soup.find("h2", class_=["-bold", "-font-18", "-gray-dark-2", "_center", "_margin-b-10" ])
temperatura = soup.find("b", class_=["title"])

if temperatura is not None:
    print("Título: ", soup.title.string)
    print("Adminstrador: ", soup.find('admin'))
    print("1ª Tag 'a': ", soup.a.string)
    print("1ª Tag 'p': ", soup.p.string)
    print("1ª Tag 'span': ", soup.span)
    print("String: ", temperatura.string)
else:
    print("Elemento de temperatura não encontrado.")