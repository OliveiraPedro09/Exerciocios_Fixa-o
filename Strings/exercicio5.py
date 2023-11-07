# Faça um programa que leia o nome de quatro alunos e mostre a ordem sorteada.
import random

nome1= str(input('Primeiro nome: '))
nome2= str(input('Segundo nome: '))
nome3= str(input('Terceiro nome: '))
nome4= str(input('Quarto nome: '))

list= [nome1, nome2, nome3, nome4]

random.shuffle(list)

print(f'A ordem da lista será: ',list)
