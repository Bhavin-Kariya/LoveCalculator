import string
import sys
from array import *

from termcolor import cprint, colored

a = input("Enter your name : ")
b = input("Enter your crush name :")

a = a.replace(" ", '')
b = b.replace(" ", '')

c = a.lower() + "loves" + b.lower()

d = "0"
e = "0"

if a == '' or b == '':
    print("You Must Enter Name of Both the Persons...")
else:
    while len(c) != 0:
        cn = 0
        cn = c.count(c[0], 0, len(c))
        if cn != 0:
            d = d + str(cn)
            c = c.replace(c[0], '', cn)
    n = len(d)

    while n > 3:

        for i in range(1, n):
            if d[i] != '0':
                if n % 2 == 0 and i == n / 2:
                    e = e + d[i]
                else:
                    e = e + str(int(d[i]) + int(d[-i]))
                d = d[:-i]
                for j in range(i):
                    d = d + '0'
        d = e[:]
        n = len(d)
        e = "0"

    al = "\033[91m {}\033[00m".format(d[1:] + " %")
    print("\033[1m", a.capitalize(), "has", al, "\033[1m", "Love for", b.capitalize())
