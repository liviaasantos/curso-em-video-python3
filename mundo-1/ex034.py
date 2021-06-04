# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:59:55 2021

@author: Livia Alves
"""

salario = float(input('Qual é o seu salário? R$'))
if salario <= 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, salario*1.15))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, salario*1.1))