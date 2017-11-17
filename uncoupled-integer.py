import sys
line = sys.stdin.readline()
line = line.replace(' ','')
line = str.split(line,',')

notwo = []

for e in line:
    if e in notwo: notwo.remove(e)
    else: notwo.append(e)
        
for e in notwo:
    sys.stdout.write(e)
