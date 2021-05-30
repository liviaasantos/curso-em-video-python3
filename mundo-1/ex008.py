# -*- coding: utf-8 -*-
"""
Created on Sun May 30 15:50:10 2021

@author: Livia Alves
"""

n1 = float(input('Digite um valor em metros: '))

print('A medida de {}m corresponde a:'.format(n1))
print('{}km'.format(n1/1000))
print('{}hm'.format(n1/100))
print('{}dam'.format(n1/10))
print('{}dm'.format(n1*10))
print('{}cm'.format(n1*100))
print('{}mm'.format(n1*1000))