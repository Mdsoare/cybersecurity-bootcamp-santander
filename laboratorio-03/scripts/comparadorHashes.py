# -*- coding: utf-8 -*-
'''
File: comparadorHashes.py
Author: Marcelo Soares
Description: Script para comparar hashes
'''

import hashlib


def calcular_hash(arquivo, hash_algorithm=hashlib.sha256):
    try:
        with open(arquivo, 'rb') as file:
            hash_obj = hash_algorithm()
            while True:
                data = file.read(8192)
                if not data:
                    break
                hash_obj.update(data)
            return hash_obj.hexdigest()
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {arquivo}")
        return None
    except Exception as e:
        print(f"Erro inesperado ao calcular o hash: {e}")
        return None


def main():
    arquivo1 = 'a.txt'
    arquivo2 = 'b.txt'

    hash1 = calcular_hash(arquivo1)
    hash2 = calcular_hash(arquivo2)

    if hash1 is not None and hash2 is not None:
        if hash1 != hash2:
            print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
            print(f'O hash do arquivo {arquivo1}: {hash1}')
            print(f'O hash do arquivo {arquivo2}: {hash2}')
        else:
            print(f'O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')
            print(f'O hash do arquivo {arquivo1}: {hash1}')
            print(f'O hash do arquivo {arquivo2}: {hash2}')


if __name__ == "__main__":
    main()
