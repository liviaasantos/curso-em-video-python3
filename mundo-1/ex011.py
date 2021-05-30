# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:24:54 2021

@author: Livia Alves
"""

lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m²'.format(lar, alt, lar*alt))
print('Para pintar essa parede você precisará de {:.4f}L de tinta'.format((alt*lar)/2))