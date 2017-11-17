
import sys
def match(f,s):
    if f == '(' and s == ')' or f == ')' and s == '(': return True
    elif f == '[' and s == ']' or f == ']' and s == '[': return True
    elif f == '{' and s == '}' or f == '}' and s == '{': return True
    else: return False
line = sys.stdin.readline()

chars = [line[0]]

for i in range(1,len(line)):
    if len(chars) > 0:
        if match(line[i],chars[len(chars)-1]): chars.pop()
        else: chars.append(line[i])
    else: chars.append(line[i])
             
if len(chars) == 0:
    sys.stdout.write('True')
else: sys.stdout.write('False')
