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
def contarnotas(notas, count, valor):
	
	print('\n\033[7m{:^50}\033[m'.format('Pegue as notas: '))
	print(f'\nR${valor:2.2f} => ', end='')
	
	if valor >= 1: 
		
		for valor_da_nota in notas:
			
			while valor >= valor_da_nota:          
				count += 1
				valor -= valor_da_nota
	  
				if valor < valor_da_nota:
					print('[', end='')
					print(f'{count:0>2} notas de R${valor_da_nota:2.2f}', end='')
					print(']', end=' ')	
					count = 0 
					
				if valor == 0:
					break

            
# LISTA DAS NOTAS DISPONIVEIS E DEFINIÇÕES DAS VARIÁVEIS
notas = [100, 50, 20, 10, 5, 2, 1]
count = valor = 0   

# ENTRADA DO VALOR PELO USUAŔIO
print('\033[7m{:^50}\033[m'.format('CONTADOR DE CÉDULAS'))


print('''Este banco tem notas de:

	-R$100.00
	-R$50.00
	-R$20.00
	-R$10.00
	-R$5.00
	-R$2.00
	-R$1.00
''')

while True:
	
	entrada = str(input('\nQuantos Reais você deseja sacar? >>>>>>> R$'))
	
	if entrada.isnumeric() and entrada != '0':
		valor = int(entrada)	
		break				
	else:
		print('\nFavor digitar valor numérico, inteiro e maior ou igual a R$1,00')
		
	
contarnotas(notas, count, valor) 
