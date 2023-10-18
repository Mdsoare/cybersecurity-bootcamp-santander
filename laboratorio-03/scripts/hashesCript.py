# -*- coding: utf-8 -*-
'''
File: codificar.py
Author: Marcelo Soares
Description: Desenvolvendo um gerador de hash e criptografia de arquivos / textos
Example:
Gerar hash MD5 de um texto: 
    python3 geradorDeHashes.py --texto "Seu texto" --tipo md5
Criptografar um texto em base64: 
    python3 geradorDeHashes.py --texto "Texto a ser criptografado" --tipo base64
Gerar hash SHA256 de um arquivo: 
    python3 geradorDeHashes.py --arquivo caminho_do_arquivo --tipo sha256
Descriptografar um texto em base64: 
    python3 geradorDeHashes.py --texto "Texto criptografado" --tipo base64 --descriptografar
Descriptografar um arquivo em base64: 
    python3 geradorDeHashes.py --arquivo caminho_do_arquivo --tipo base64 --descriptografar
'''

import argparse
import hashlib
import base64

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

def criptografar_texto(texto, tipo):
    if tipo == 'base64':
        return base64.b64encode(texto.encode('utf-8')).decode()
    else:
        raise ValueError('Tipo de criptografia inválido')

def descriptografar_texto(texto, tipo):
    if tipo == 'base64':
        return base64.b64decode(texto.encode('utf-8')).decode()
    else:
        raise ValueError('Tipo de descriptografia inválido')

def main():
    parser = argparse.ArgumentParser(description='Gera hashes a partir de uma entrada de texto ou arquivo e opcionalmente descriptografa')
    parser.add_argument('--texto', help='Texto a ser hasheado ou criptografado')
    parser.add_argument('--arquivo', help='Caminho para um arquivo a ser hasheado ou criptografado')
    parser.add_argument('--tipo', choices=['md5', 'sha1', 'sha256', 'sha512', 'base64'], help='Tipo de hash ou criptografia')
    parser.add_argument('--descriptografar', action='store_true', help='Descriptografar o texto ou arquivo')
    
    args = parser.parse_args()

    if args.texto:
        if args.descriptografar:
            resultado = descriptografar_texto(args.texto, args.tipo)
        else:
            if args.tipo in ['md5', 'sha1', 'sha256', 'sha512']:
                resultado = gerar_hash(args.texto, args.tipo)
            elif args.tipo == 'base64':
                resultado = criptografar_texto(args.texto, args.tipo)
            else:
                print('Tipo de hash ou criptografia inválido.')
                return
        print(f'Resultado: {resultado}')
    elif args.arquivo:
        try:
            with open(args.arquivo, 'r') as file:
                texto = file.read()
                if args.descriptografar:
                    resultado = descriptografar_texto(texto, args.tipo)
                else:
                    if args.tipo in ['md5', 'sha1', 'sha256', 'sha512']:
                        resultado = gerar_hash(texto, args.tipo)
                    elif args.tipo == 'base64':
                        resultado = criptografar_texto(texto, args.tipo)
                    else:
                        print('Tipo de hash ou criptografia inválido.')
                        return
                print(f'Resultado: {resultado}')
        except FileNotFoundError:
            print('Arquivo não encontrado.')
    else:
        print('Você deve especificar --texto ou --arquivo.')

if __name__ == "__main__":
    main()
