import random
import time
import os

print(""" 
- - - - - - - - Rules - - - - - - - - 

 No duplicates  
 if you do duplicate it will break
 20 tries 
 only enter 3 numbers

 - - - - - - - - - - - - - - - - - - - 
""")

a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
r = random
# nociwp = number of choice that are correct in wrong place
nociwp = 0

b = r.choice(a)
c = r.choice(a)
while c == b:
    c = r.choice(a)
d = r.choice(a)
while d == b or d == c:
    d = r.choice(a)
g = b + c + d
noc = 0
#print(g)

rd = open('log.txt', 'a')
rd.write(g + '''
''')
rd.close()

i = 0

while i < 20:
    x = str(input('Guess -- '))

    if x == g:
        i = i + 100

    if b == x[0]:
        noc = noc + 1

    if c == x[1]:
        noc = noc + 1

    if d == x[2]:
        noc = noc + 1

    if b == x[0]:
        nociwp = nociwp + 1

    if b == x[1]:
        nociwp = nociwp + 1

    if b == x[2]:
        nociwp = nociwp + 1

    if c == x[0]:
        nociwp = nociwp + 1

    if c == x[1]:
        nociwp = nociwp + 1

    if c == x[2]:
        nociwp = nociwp + 1

    if d == x[0]:
        nociwp = nociwp + 1

    if d == x[1]:
        nociwp = nociwp + 1

    if d == x[2]:
        nociwp = nociwp + 1

    #else:
    #print('Error input 3 numbers')
    #print('ending now')
    #quit()
    #exit()

    time.sleep(1)
    print('# of correct digits in correct place ---- ' + str(noc))
    print('# of correct digits in incorrect place -- ' + str(nociwp - noc))
    noc = 0
    nociwp = 0

    i = i + 1

win = str(i - 100)
win = 'Nice Job! You Got that in ' + win + ' tries'
print()
print(win)

rd = open('log.txt', 'a')
rd.write(win + '''
''')
rd.close()

#log attempts number and give a best score

#make a solver
