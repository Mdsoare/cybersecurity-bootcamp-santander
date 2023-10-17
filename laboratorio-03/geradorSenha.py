# -*- coding: utf-8 -*-
'''
File: geradorSenha.py
Author: Marcelo Soares
Description: Script para gerar senhas aleatórias
'''

import string
import secrets


def generate_password(length=16, characters=None):
    if characters is None:
        characters = string.ascii_letters + \
            string.digits + 'ç!@#$%&*()-_=+,.;:/?[]\{\}'

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def main():
    password = generate_password()
    print("Senha gerada: ", password)


if __name__ == "__main__":
    main()
