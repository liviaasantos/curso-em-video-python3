# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 12:43:58 2021

@author: Livia Alves
"""
import random
p = input('Primeiro aluno: ')
s = input('Segundo aluno: ')
t = input('Terceiro aluno: ')
q = input('Quarto aluno: ')
alunos = [p, s, t, q]
ordem = random.sample(alunos, k=4)
print('A ordem de apresentação é ')
print(ordem)
