#Fibonacci: Crie um programa que imprima os primeiros n termos da sequência de Fibonacci.
first = 0
second = 1

number = int(input('size: '))
print(first)
print(second)
while number > 0:
    third = first + second
    print(third)
    first = second
    second = third
    number = number -1
