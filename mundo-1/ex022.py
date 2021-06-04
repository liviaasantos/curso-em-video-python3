# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 18:37:55 2021

@author: livia Alves
"""

nome = input('Digite seu nome completo: ').strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome.split()[0], len(nome.split(' ')[0])))
