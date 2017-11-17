n = int(raw_input())
if n < 0: 
    print 'NIL'
elif n == 0: 
    print 1
else:
    total = 1
    for i in range(n,0,-1):
        total*=i
    print total
    
