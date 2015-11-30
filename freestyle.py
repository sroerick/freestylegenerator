import random

lines = open('words.txt').read().splitlines()

for x in range(0, 3):
    myline =random.choice(lines)
    print(myline) 
