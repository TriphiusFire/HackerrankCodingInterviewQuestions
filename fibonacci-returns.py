import sys
lines = sys.stdin.readlines()
inputs = []
for e in lines: inputs.append(int(e))
fibos = [0,1]
for i in range(2,100):
    fibos.append(fibos[i-1]+fibos[i-2])
for e in inputs: 
    sys.stdout.write(str(fibos[e])+'\n')
