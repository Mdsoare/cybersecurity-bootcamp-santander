# -*- coding: utf-8 -*-
'''
File: clamav.py
Author: Marcelo Soares
Description: Código para uso do antivírus clamav
'''

import subprocess
import schedule
import time

def update_clamav():
    try:
        subprocess.run(['sudo', 'freshclam'], check=True)
        print("ClamAV foi atualizado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao atualizar o ClamAV: {e.stderr}")

def scan_directory(directory):
    try:
        result = subprocess.run(['clamscan', '-r', directory], capture_output=True, text=True, check=True)
        output = result.stdout
        if "Infected files: 0" in output:
            print(f"Nenhum vírus encontrado no diretório '{directory}'.")
        else:
            print(f"Vírus encontrados no diretório '{directory}':")
            print(output)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar a verificação de antivírus: {e.stderr}")

def schedule_scan(directory, interval_minutes):
    schedule.every(interval_minutes).minutes.do(scan_directory, directory)

def generate_report(directory, report_file):
    try:
        result = subprocess.run(['clamscan', '-r', directory, '--log', report_file], capture_output=True, text=True, check=True)
        output = result.stdout
        if "Infected files: 0" in output:
            print(f"Nenhum vírus encontrado no diretório '{directory}'.")
        else:
            print(f"Vírus encontrados no diretório '{directory}':")
            print(output)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar a verificação de antivírus: {e.stderr}")

def main_menu():
    while True:
        print("\nMenu ClamAV:")
        print("1. Atualizar o ClamAV")
        print("2. Verificar um diretório")
        print("3. Agendar verificação em um diretório")
        print("4. Gerar relatório de verificação")
        print("5. Sair")
        choice = input("Escolha uma opção (1/2/3/4/5): ")

        if choice == "1":
            update_clamav()
        elif choice == "2":
            directory_to_scan = input("Digite o caminho do diretório a ser verificado: ")
            scan_directory(directory_to_scan)
        elif choice == "3":
            directory_to_scan = input("Digite o caminho do diretório a ser verificado: ")
            interval_minutes = int(input("Digite o intervalo em minutos para a verificação: "))
            schedule_scan(directory_to_scan, interval_minutes)
        elif choice == "4":
            directory_to_scan = input("Digite o caminho do diretório a ser verificado: ")
            report_file = input("Digite o caminho do arquivo de relatório: ")
            generate_report(directory_to_scan, report_file)
        elif choice == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_menu()

    while True:
        schedule.run_pending()
        time.sleep(1)
