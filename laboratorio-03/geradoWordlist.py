# -*- coding: utf-8 -*-
'''
File: geradorWordlist.py
Author: Marcelo Soares
Description: Código para a geração de uma Wordlist
'''
import itertools
import string

# caracteres = string.ascii_letters + string.digits + string.punctuation # Letras + Números + caracters
# caracteres = string.ascii_letters + string.digits # Letras + Números
caracteres = string.ascii_letters # Letras
# No exemplo serão gerados listas de 5 posições fixas, mas pode alterar entre min e max
comprimento_min = 5
comprimento_max = 5

for comprimento in range(comprimento_min, comprimento_max + 1):
    resultado = itertools.product(caracteres, repeat=comprimento)
    for i in resultado:
        senha = ''.join(i)
        print(senha)