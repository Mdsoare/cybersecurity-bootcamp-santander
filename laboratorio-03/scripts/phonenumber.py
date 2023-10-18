# -*- coding: utf-8 -*-
'''
File: phonenumber.py
Author: Marcelo Soares
Description: Script para valildar e informal local de telefone 
Requirement: pip install phonenumbers
'''

import phonenumbers
from phonenumbers import geocoder

def validar_numero_telefone(numero):
    try:
        phone_number = phonenumbers.parse(numero)
        if phonenumbers.is_valid_number(phone_number):
            return phone_number
        else:
            return None
    except phonenumbers.phonenumberutil.NumberFormatException:
        return None

def obter_local_telefone(numero):
    phone_number = validar_numero_telefone(numero)
    if phone_number:
        return geocoder.description_for_number(phone_number, 'pt')
    else:
        return "Número de telefone inválido."

if __name__ == "__main__":
    phone = input('Digite o telefone no formato +551140028922: ')
    local = obter_local_telefone(phone)
    print(local)
