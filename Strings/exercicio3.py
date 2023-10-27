# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase= str(input('Digite uma frase:' )).lower().strip()

contador= 0

if 'a' in frase:
    print('A letra "a" aparece {} na frase'.format(frase.count('a')))
    print('A letra "a" aparece na posição {}  '.format(frase.find('a')+1))
    print('A letra "a" aparece na posição {} pela ultima vez '.format(frase.rfind('a')+1))
else : 
    print("Sua frase não possui a letra 'a' ")




