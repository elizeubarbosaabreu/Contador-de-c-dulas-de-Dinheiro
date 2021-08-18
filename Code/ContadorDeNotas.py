#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ContadorDeNotas.py
#  
#  Copyright 2021  <pi@suelizeuadrian>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# CRIA UMA FUNÇÃO COM UM LOOP QUE SUBTRAI UMA NOTA DO VALOR DADO COMEÇANDO
# PELA MAIOR NOTA DAS NOTAS DEFINIDAS  NA LISTA 'NOTAS', ATÉ QUE O VALOR
# RESTANTE SEJA 0
def contarnotas(notas, x, count, valor):

    for n in notas:      

        if valor >= (notas[x]):          
            count += 1

            if valor >= 0:
                valor -= (notas[x])

            if valor < (notas[x]):
                print (f'{count} notas de R${(notas[x]):2.2f}')
                x += 1
                count = 0            
        else:
            x += 1
# LISTA DAS NOTAS DISPONIVEIS E DEFINIÇÕES DAS VARIÁVEIS
notas = [100, 50, 20, 10, 5, 2, 1]
x = count = valor = 0   

# ENTRADA DO VALOR PELO USUAŔIO
print('\033[7m{:^50}\033[m'.format('CONTADOR DE CÉDULAS'))
 
entrada = str(input('''
Este banco tem notas de:
-R$100.00
-R$50.00
-R$20.00
-R$10.00
-R$5.00
-R$2.00
-R$1.00
Quantos Reais você deseja sacar?
>>>>>>> R$'''))
if entrada.isnumeric():
	valor = int(entrada)			
else:
	print("Só vale usar números:")
	entravalor()
	

contarnotas(notas, x, count, valor)
print("Bye")        
