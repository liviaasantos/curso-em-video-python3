# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:06:53 2021

@author: Livia
"""

name = input('Qual seu nome completo? ')
n = name.strip().upper().split(' ')
print('Seu nome tem Silva? {}'.format('SILVA' in n))
