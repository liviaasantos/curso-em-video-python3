# -*- coding: utf-8 -*-
"""
Created on Sun May 30 11:26:56 2021

@author: Livia Alves
"""

var = input('Digite algo: ')

print('O tipo primitivo do que você digitou é {}'.format(type(var)))
print('Só tem espaço? {}'.format(var.isspace()))
print('É um número? {}'.format(var.isnumeric()))
print('É alfabético? {}'.format(var.isalpha()))
print('É alfanumérico? {}'.format(var.isalnum()))
print('Está em maiúsculas? {}'.format(var.isupper()))
print('Está em minúsculas? {}'.format(var.islower()))
print('Está capitalizada? {}'.format(var.istitle()))

