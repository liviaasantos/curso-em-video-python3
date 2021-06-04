# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 12:33:45 2021

@author: Livia Alves
"""
from random import randint
alunos = []
p = input('Primeiro aluno: ')
alunos.append(p)
s = input('Segundo aluno: ')
alunos.append((s))
t = input('Terceiro aluno: ')
alunos.append(t)
q = input('Quarto aluno: ')
alunos.append(q)
print('O aluno escolhido foi {}'.format(alunos[randint(0,3)]))

