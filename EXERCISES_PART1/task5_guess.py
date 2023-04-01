#Adivinhação: Crie um programa que escolha um número aleatório entre 1 e 100 e permita que o usuário adivinhe qual é esse número.
import random

number = random.randint(1,100)
guess = 0

while number != guess:

    guess = int(input('your guess:'))
    if guess == number:
        print('CORRECT, you guessed: ', guess, 'and it was: ', number)
        break
    elif guess > number:
        print('wrong! the number is lower')
    elif guess < number:
        print('wrong! the number is higher')
