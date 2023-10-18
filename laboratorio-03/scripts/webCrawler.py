# -*- coding: utf-8 -*-
'''
File: webCrawler.py
Author: Marcelo Soares
Description: Script para Web Crawler
'''

import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def start(url):

    wordlist = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser')

    for each_text in soup.findAll('div', {'class': 'article'}):  # Escolha uma classe CSS mais específica
        content = each_text.text

        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
    
    # Melhorar a limpeza de palavras
    clean_list = [re.sub(r'[!@#$%^&*()_\-+={[}\]|;:"<>?/., ]', '', word) for word in wordlist if word]

    create_dictionary(clean_list)

def create_dictionary(clean_list):

    c = Counter(clean_list)

    # Print das 10 palavras mais comuns
    top = c.most_common(10)
    for word, count in top:
        print(f"{word}: {count}")

if __name__ == '__main__':
    url = input('Digite a URL: ')
    start(url)