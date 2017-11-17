# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

l = sys.stdin.readlines()
f = int(l[0])

F0 = 0
F1 = 1
F2 = None

if f == 0: sys.stdout.write(str(F0))
elif f == 1: sys.stdout.write(str(F1))
else:
    for i in range(0,f-1):
        F2 = F0+F1
        F0 = F1
        F1 = F2
    sys.stdout.write(str(F2))
