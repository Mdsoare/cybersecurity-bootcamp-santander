# -*- coding: utf-8 -*-
'''
File: encryptDecrypt.py
Author: Marcelo Soares
Description: Código para uso de criptografia de arquivos
'''

from cryptography.fernet import Fernet
import base64

def gerar_chave():
    return Fernet.generate_key()

def criptografar_texto(texto, chave):
    fernet = Fernet(chave)
    texto_bytes = texto.encode('utf-8')
    texto_criptografado = fernet.encrypt(texto_bytes)
    return texto_criptografado

def descriptografar_texto(texto_criptografado, chave):
    fernet = Fernet(chave)
    texto_bytes = fernet.decrypt(texto_criptografado)
    texto = texto_bytes.decode('utf-8')
    return texto

def menu():
    print("===== MENU DE CRIPTOGRAFIA =====")
    print("1. Gerar chave")
    print("2. Criptografar texto")
    print("3. Descriptografar texto")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

while True:
    opcao = menu()

    if opcao == "1":
        chave = gerar_chave()
        print("Chave gerada:", chave.decode())
    elif opcao == "2":
        texto = input("Digite o texto a ser criptografado: ")
        chave = input("Digite a chave de criptografia: ").encode()
        texto_criptografado = criptografar_texto(texto, chave)
        print("Texto criptografado:", base64.urlsafe_b64encode(texto_criptografado).decode())
    elif opcao == "3":
        texto_criptografado = base64.urlsafe_b64decode(input("Digite o texto criptografado: ").encode())
        chave = input("Digite a chave de descriptografia: ").encode()
        texto_descriptografado = descriptografar_texto(texto_criptografado, chave)
        print("Texto descriptografado:", texto_descriptografado)
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")