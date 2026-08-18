# -*- coding: utf-8 -*-
'''
File: geradorSenha.py
Author: Marcelo Soares
Description: Script para gerar senhas aleatórias
'''

import string
import secrets


def generate_secret(length=16, characters=None):
    if characters is None:
        characters = string.ascii_letters + \
            string.digits + 'ç!@#$%&*()-_=+,.;:/?[]{}'

    result = ''.join(secrets.choice(characters) for _ in range(length))
    return result


def main():
    generated_secret = generate_secret()
    print("Senha gerada:", generated_secret)


if __name__ == "__main__":
    main()