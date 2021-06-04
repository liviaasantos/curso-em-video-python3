# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:20:59 2021

@author: Livia Alves
"""
import random
num = random.randint(0, 5)

print('-'*45)
print('Vou pensar em um número entre 0 e 5. Consegue adivinhar?')
print('-'*45)
ver = int(input('Em que número eu pensei? '))

if num == ver:
    print('PARABÉNS! Você conseguiu me vencer')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(num, ver))