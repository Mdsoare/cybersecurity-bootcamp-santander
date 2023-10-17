# -*- coding: utf-8 -*-
'''
File: geradorDeHashes.py
Author: Marcelo Soares
Description: Script para gerar hashes a partir de uma entrada de texto ou arquivo
Example:
python3 geradorDeHashes.py --texto "Seu texto" md5
python3 geradorDeHashes.py --arquivo caminho_do_arquivo sha256
python3 geradorDeHashes.py -h # Para exibir o help
'''

import argparse
import hashlib

def gerar_hash(texto, tipo):
    if tipo == 'md5':
        return hashlib.md5(texto.encode('utf-8')).hexdigest()
    elif tipo == 'sha1':
        return hashlib.sha1(texto.encode('utf-8')).hexdigest()
    elif tipo == 'sha256':
        return hashlib.sha256(texto.encode('utf-8')).hexdigest()
    elif tipo == 'sha512':
        return hashlib.sha512(texto.encode('utf-8')).hexdigest()
    else:
        raise ValueError('Tipo de hash inválido')

def main():
    parser = argparse.ArgumentParser(description='Gera hashes a partir de uma entrada de texto ou arquivo')
    parser.add_argument('--texto', help='Texto a ser hasheado')
    parser.add_argument('--arquivo', help='Caminho para um arquivo a ser hasheado')
    parser.add_argument('tipo', choices=['md5', 'sha1', 'sha256', 'sha512'], help='Tipo de hash')

    args = parser.parse_args()

    if args.texto:
        resultado = gerar_hash(args.texto, args.tipo)
        print(f'O hash gerado da string é: {resultado}')
    elif args.arquivo:
        try:
            with open(args.arquivo, 'r') as file:
                texto = file.read()
                resultado = gerar_hash(texto, args.tipo)
                print(f'O hash gerado do arquivo é: {resultado}')
        except FileNotFoundError:
            print('Arquivo não encontrado.')
    else:
        print('Você deve especificar --texto ou --arquivo.')

if __name__ == "__main__":
    main()