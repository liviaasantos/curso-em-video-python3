# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:19:29 2021

@author: Livia Alves
"""

din = float(input('Quanto dinheiro você tem na carteira? R$'))

dol = din / 5.23

print('Com R${:.2f} você pode comprar US${:.2f}'.format(din, dol))
