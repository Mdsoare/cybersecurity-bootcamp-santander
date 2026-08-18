# -*- coding: utf-8 -*-
'''
File: geradorSenha.py
Author: Marcelo Soares
Description: Script para gerar strings aleatórias
'''

import string
import secrets


def generate_string(length=16, characters=None):
    if characters is None:
        characters = string.ascii_letters + \
            string.digits + 'ç!@#$%&*()-_=+,.;:/?[]{}'

    data = ''.join(secrets.choice(characters) for _ in range(length))
    return data


def main():
    output = generate_string()
    print("Resultado:", output)


if __name__ == "__main__":
    main()