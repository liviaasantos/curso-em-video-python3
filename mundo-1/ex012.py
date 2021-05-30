# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:31:03 2021

@author: Livia Alves
"""
preço = float(input('Qual é o preço do produto? R$'))

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, preço*0.95))
