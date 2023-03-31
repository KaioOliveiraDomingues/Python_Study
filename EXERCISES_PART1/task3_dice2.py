import random
import time

print('DICE ROLL!!')
time.sleep(1)
size = int(input('Max Roll: '))
dice = random.randint(1,size)
print('Rolling!!')
time.sleep(1)
print('.', end="\r")
time.sleep(1)
print('..', end="\r")
time.sleep(1)
print('...', end="\r")
time.sleep(1)
print('DICE ROLLED: ', dice)
