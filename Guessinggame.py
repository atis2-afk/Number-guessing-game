import random
from random import randint

x = randint(a=1, b=10)
y = int(input("guess a number"))
while y != x:
    print("try again!")
    x = int(input("next guess?"))
if y == x:
    print("yay")

