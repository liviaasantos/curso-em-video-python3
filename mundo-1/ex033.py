# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:50:58 2021

@author: 55349
"""

p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))
t = int(input('Terceiro valor: '))

if p > s and p > t:
    print('O maior valor digitado foi {}'.format(p))
if p < s and p < t: 
    print('O menor valor digitado foi {}'.format(p))
if s > p and s > t:
    print('O maior valor digitado foi {}'.format(s))
if s < p and s < t:
    print('O menor valor digitado foi {}'.format(s))
if t > p and t > s:
    print('O maior valor digitado foi {}'.format(t))
if t < p and t < s:
    print('O menor valor digitado foi {}'.format(t))