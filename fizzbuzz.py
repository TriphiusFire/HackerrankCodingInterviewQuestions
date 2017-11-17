# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
for i in range(1,N+1):
    if i % 15 == 0: print 'FizzBuzz'
    elif i % 5 == 0: print 'Buzz'
    elif i % 3 == 0: print 'Fizz'
    else: print i
