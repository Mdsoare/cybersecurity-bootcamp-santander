# -*- coding: utf-8 -*-
'''
File: clamav.py
Author: Marcelo Soares
Description: Código para uso do antivírus clamav
'''

import shutil
import subprocess  # nosec B404
import time
import schedule


def _get_bin_path(binary_name, default_path):
    '''Retorna o caminho absoluto do executável ou fallback padronizado.'''
    return shutil.which(binary_name) or default_path


def update_clamav():
    sudo_bin = _get_bin_path('sudo', '/usr/bin/sudo')
    freshclam_bin = _get_bin_path('freshclam', '/usr/bin/freshclam')
    try:
        subprocess.run([sudo_bin, freshclam_bin], check=True)  # nosec B603
        print("ClamAV foi atualizado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao atualizar o ClamAV: {e.stderr if e.stderr else e}")


def scan_directory(directory):
    directory_clean = directory.strip()
    if not directory_clean:
        print("Caminho do diretório inválido.")
        return

    clamscan_bin = _get_bin_path('clamscan', '/usr/bin/clamscan')
    try:
        result = subprocess.run(
            [clamscan_bin, '-r', directory_clean],
            capture_output=True,
            text=True,
            check=True
        )  # nosec B603
        output = result.stdout
        if "Infected files: 0" in output:
            print(f"Nenhum vírus encontrado no diretório '{directory_clean}'.")
        else:
            print(f"Vírus encontrados no diretório '{directory_clean}':")
            print(output)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar a verificação de antivírus: {e.stderr if e.stderr else e}")


def schedule_scan(directory, interval_minutes):
    schedule.every(interval_minutes).minutes.do(scan_directory, directory)


def generate_report(directory, report_file):
    directory_clean = directory.strip()
    report_file_clean = report_file.strip()
    if not directory_clean or not report_file_clean:
        print("Caminho do diretório ou do relatório inválido.")
        return

    clamscan_bin = _get_bin_path('clamscan', '/usr/bin/clamscan')
    try:
        result = subprocess.run(
            [clamscan_bin, '-r', directory_clean, '--log', report_file_clean],
            capture_output=True,
            text=True,
            check=True
        )  # nosec B603
        output = result.stdout
        if "Infected files: 0" in output:
            print(f"Nenhum vírus encontrado no diretório '{directory_clean}'.")
        else:
            print(f"Vírus encontrados no diretório '{directory_clean}':")
            print(output)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar a verificação de antivírus: {e.stderr if e.stderr else e}")


def main_menu():
    print("\nMenu ClamAV:")
    print("1. Atualizar o ClamAV")
    print("2. Verificar um diretório")
    print("3. Agendar verificação em um diretório")
    print("4. Gerar relatório de verificação")
    print("5. Sair")
    choice = input("Escolha uma opção (1/2/3/4/5): ").strip()

    if choice == "1":
        update_clamav()
    elif choice == "2":
        directory_to_scan = input("Digite o caminho do diretório a ser verificado: ")
        scan_directory(directory_to_scan)
    elif choice == "3":
        directory_to_scan = input("Digite o caminho do diretório a ser verificado: ")
        try:
            interval_minutes = int(input("Digite o intervalo em minutos para a verificação: "))
            schedule_scan(directory_to_scan, interval_minutes)
        except ValueError:
            print("Intervalo inválido. Digite um número inteiro.")
    elif choice == "4":
        directory_to_scan = input("Digite o caminho do diretório a ser verificado: ")
        report_file = input("Digite o caminho do arquivo de relatório: ")
        generate_report(directory_to_scan, report_file)
    elif choice == "5":
        return True
    else:
        print("Opção inválida. Tente novamente.")

    return False


if __name__ == "__main__":
    should_exit = False
    while not should_exit:
        should_exit = main_menu()

    while True:
        schedule.run_pending()
        time.sleep(1)
