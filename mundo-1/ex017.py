# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 11:51:25 2021

@author: 55349
"""
from math import hypot
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))