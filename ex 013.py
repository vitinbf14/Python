from random import randint
pc = randint(0,5) #Faz o pc pensar
print('---' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('---' * 20)
jogador = int(input('Em que número eu pensei?')) #Jogador tenta adivinhar
if jogador == pc:
    print('Parabéns!! Você ganhou!!')
else:
    print('Você errou!! Tente novamente!!')
