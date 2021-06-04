# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 17:04:01 2021

@author: Livia Alves
"""
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < (b+c) and b < (a+c) and c < (a+b):
    print('Os segmentos formam um triângulo!')
else:
    print('Os segmentos não formam um triângulo!')