# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 22:42:56 2021

@author: Livia Alves
"""

frase = input('Digite uma frase: ')
frase = frase.strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))

