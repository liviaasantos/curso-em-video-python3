# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:45:35 2021

@author: Livia Alves
"""

salário = float(input('Qual é o seu salário? R$'))

print('O funcionário que recebia R${:.2f}, com aumento de 15%, passará a receber R${:.2f}'.format(salário, salário*1.15))
