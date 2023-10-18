# -*- coding: utf-8 -*-
'''
File: decript.py
Author: Marcelo Soares
Description: Script para simular o resgate de um arquivo encriptado por um Ransomware
Requirement: pip install pyaes
'''
import os
import pyaes

# Função principal para descriptografar o arquivo de teste.txt
# Inclui no laboratório um tratamento de erro try-except, mas em um cenário real não estariam

def decrypt_file(input_filename, output_filename, key):
    try:
        with open(input_filename, "rb") as encrypted_file:
            aes = pyaes.AESModeOfOperationCTR(key)
            with open(output_filename, "wb") as decrypted_file:
                while True:
                    chunk = encrypted_file.read(1024)  # Lê o arquivo criptografado em blocos de 1 KB
                    if not chunk:
                        break
                    decrypted_chunk = aes.decrypt(chunk)
                    decrypted_file.write(decrypted_chunk)
        
        # Remover o arquivo criptografado após a descriptografia bem-sucedida
        os.remove(input_filename)
        
        print(f"Arquivo '{input_filename}' descriptografado com sucesso em '{output_filename}'")
    
    except Exception as e:
        print(f"Erro ao descriptografar o arquivo: {str(e)}")

# Como é um laboratório, inclui a estrutura if __name__=="__main__"
# Dessa forma o código só será executado diretamente.

if __name__ == "__main__":
    encrypted_file_name = "teste.txt.ransomwaretroll"
    decrypted_file_name = "teste.txt"
    decryption_key = b"testeransomwares"

    decrypt_file(encrypted_file_name, decrypted_file_name, decryption_key) # chamada da função aqui

