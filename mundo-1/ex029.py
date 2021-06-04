# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:31:16 2021

@author: Livia Alves
"""

vel = float(input('Qual a velocidade atual do seu carro? '))

if vel > 80:
    multa = (vel - 80)*7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')