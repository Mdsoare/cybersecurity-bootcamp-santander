# -*- coding: utf-8 -*-
'''
File: hideFile.py
Author: Marcelo Soares
Description: Script para ocultar/desocultar arquivos/diretórios
'''
import ctypes
import platform
import os

def hide_file(file_path, hide=True):
    if platform.system() == 'Windows':
        # Ocultar ou desocultar arquivo/diretório no Windows
        atributo_ocultar = 0x02 if hide else 0x00
        retorno = ctypes.windll.kernel32.SetFileAttributesW(file_path, atributo_ocultar)
        return retorno
    elif platform.system() == 'Linux':
        # Adicionar ou remover o ponto no início do nome para ocultar ou desocultar no Linux
        new_path = f".{file_path}" if hide else file_path[1:]
        try:
            os.rename(file_path, new_path)
            return True
        except Exception as e:
            print(f'Erro ao ocultar/desocultar: {e}')
    else:
        print('Sistema operacional não suportado.')
    return False

if __name__ == '__main__':
    file_path = input('Digite o caminho do arquivo/diretório a ser ocultado/desocultado: ')
    
    choice = input('Deseja ocultar (O) ou desocultar (D)? ').strip().lower()
    if choice == 'o':
        if hide_file(file_path):
            print('Arquivo/diretório foi ocultado!')
        else:
            print('Falha ao ocultar o arquivo/diretório.')
    elif choice == 'd':
        if hide_file(file_path, hide=False):
            print('Arquivo/diretório foi desocultado!')
        else:
            print('Falha ao desocultar o arquivo/diretório.')
    else:
        print('Escolha inválida. Use "O" para ocultar ou "D" para desocultar.')
