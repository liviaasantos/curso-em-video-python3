# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:56:37 2021

@author: Livia Alves
"""

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

print('O total a pagar é de R${:.2f}'.format(dias*60+km*0.15))
