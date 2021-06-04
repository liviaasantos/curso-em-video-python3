# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:39:16 2021

@author: Livia Alves
"""

num = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(num))
if num <= 200:
    preco = 0.5*num
    print('E o preço da sua passagem será de R${:.2f}'.format(preco))
else:
    preco = 0.45*num
    print('É o preço da sua viagem será de R${:.2f}'.format(preco))