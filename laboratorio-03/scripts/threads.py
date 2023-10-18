# -*- coding: utf-8 -*-
'''
File: threads.py
Author: Marcelo Soares
Description: Desenvolvendo um script para executar threads usando POO
'''
from threading import Thread
import time

class Carro(Thread):
    def __init__(self, velocidade, piloto):
        super().__init__()
        self.velocidade = velocidade
        self.piloto = piloto

    def run(self):
        trajeto = 0
        while trajeto < 100:
            trajeto += self.velocidade
            time.sleep(0.5)
            print(f'Piloto: {self.piloto} - Trajeto: {trajeto} Km\n')

t_carro1 = Carro(1, 'Bruno')
t_carro2 = Carro(1.5, 'Thiago')

t_carro1.start()
t_carro2.start()

