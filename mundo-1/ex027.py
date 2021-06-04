# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 22:52:25 2021

@author: Livia Alves Santos
"""

name = input('Qual seu nome completo? ')
name = name.split(' ')

print('O seu primeiro nome é {}'.format(name[0]))
print('O seu último nome é {}'.format(name[len(name)-1]))