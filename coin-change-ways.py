def getWays(n, c):
    coins = sorted(c)
    t = [1]
    for i in range(0,n): t.append(0)
    for i in range(0,len(coins)):
        
        for j in range(coins[i],n+1):
            t[j] += t[j-coins[i]]
    return t[n]

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
c = map(long, raw_input().strip().split(' '))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print ways
