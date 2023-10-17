# -*- coding: utf-8 -*-
'''
File: encryptDecrypt.py
Author: Marcelo Soares
Description: Código para uso de criptografia GPG
Requirement: pip install python-gnupg
'''
import gnupg

def gerar_chave(gpg, nome, email, senha):
    chave = gpg.gen_key(gpg.gen_key_input(
        name_real=nome,
        name_email=email,
        passphrase=senha
    ))
    return chave

def criptografar_texto(gpg, texto, destinatario):
    texto_criptografado = gpg.encrypt(texto, destinatario)
    return texto_criptografado.data.decode()

def descriptografar_texto(gpg, texto_criptografado, senha):
    texto_descriptografado = gpg.decrypt(texto_criptografado, passphrase=senha)
    return texto_descriptografado.data.decode()

def menu():
    print("===== MENU DE CRIPTOGRAFIA =====")
    print("1. Gerar chave")
    print("2. Criptografar texto")
    print("3. Descriptografar texto")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

gpg = gnupg.GPG()

while True:
    opcao = menu()

    if opcao == "1":
        nome = input("Nome do usuário: ")
        email = input("Endereço de e-mail: ")
        senha = input("Senha para a chave: ")
        chave = gerar_chave(gpg, nome, email, senha)
        print("Chave gerada ID:", chave.fingerprint)
    elif opcao == "2":
        destinatario = input("ID do destinatário (fingerprint): ")
        texto = input("Digite o texto a ser criptografado: ")
        texto_criptografado = criptografar_texto(gpg, texto, destinatario)
        print("Texto criptografado:\n", texto_criptografado)
    elif opcao == "3":
        texto_criptografado = input("Cole o texto criptografado: ")
        senha = input("Senha da chave: ")
        texto_descriptografado = descriptografar_texto(gpg, texto_criptografado, senha)
        print("Texto descriptografado:\n", texto_descriptografado)
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")
