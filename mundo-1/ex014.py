# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:50:54 2021

@author: Livia Alves
"""

tempc = float(input('Informe a temperatura em °C: '))

tempf = 32 + tempc*9/5

print('A temperatura de {:.2f}°C corresponde a {:.2f}°F'.format(tempc, tempf))