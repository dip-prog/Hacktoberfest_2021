dp = [0]*(100000+2)
fibPow = [0]*(100000+2)
fibPow[0] = 2
fibPow[1] = 2
dp[1] = 1
m=1000000007

    
for i in range(2, 100000+2):
    # print(fib[i-1], fib[i-2], pow[fib[i-1]], pow[fib[i-2]])
    fibPow[i] = (fibPow[i-1]*fibPow[i-2])%m
    dp[i] = (((dp[i-1]*fibPow[i-2])%m)+((dp[i-2]*fibPow[i-1])%m))%m
    # print(i, dp[i])
    

for _ in range(int(input())):
    n = int(input())
    print(dp[n])
