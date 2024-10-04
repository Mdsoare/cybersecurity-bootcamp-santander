# -*- coding: utf-8 -*-
'''
File: bufferOverFlowSys.py
Author: Marcelo Soares
Description: Neste exemplo, o código lê 10 bytes de entrada do usuário usando 
sys.stdin.read(10). Se o usuário inserir mais de 10 bytes de dados, isso pode 
resultar em um buffer overflow, onde o programa tentará ler mais dados do que 
o buffer pode acomodar, potencialmente corrompendo a memória.
'''
import sys

def read_input():
    buffer = sys.stdin.read(10)
    return buffer

data = read_input()
print(f"Dados lidos: {data}")

'''
REMEDIAÇÃO: Para remediar essa vulnerabilidade, podemos utilizar a função sys.stdin.readline() em vez de sys.stdin.read(10). 
A função readline() lê uma única linha de entrada, até encontrar um caractere de nova linha. 
Dessa forma, evitamos o problema de ler um número fixo de bytes e garantimos que apenas uma linha de dados seja processada por vez.

import sys

def read_input():
    buffer = sys.stdin.readline()
    return buffer

data = read_input()
print(f"Dados lidos: {data}")
'''