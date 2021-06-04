# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:01:18 2021

@author: Livia Alves
"""

city = input('Em que cidade você nasceu: ')
city = city.upper().strip()
corte = city.split(' ')
print(corte[0] == 'SANTO')
