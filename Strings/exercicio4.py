# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

name = str(input('Digite seu nome:')).strip()
x = name.split()

list=[]
list.append(x)

print('Seu primeiro nome é', x[0])
print('Seu último nome é', x[-1])


