# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 11:57:31 2021

@author: Livia Alves
"""

from math import sin, cos, tan, radians
a = radians(float(input('Digite o ângulo desejado: ')))
print('O ângulo de {} tem o seno de {:.2f}'.format(a, sin(a)))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(a, cos(a)))
print('O ângulo de {} tem a tangente de {:.2f}'.format(a, tan(a)))