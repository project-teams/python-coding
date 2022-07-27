'''
내가 생각했던 정답은 nCr로 해서 다 더하기 
'''
def choose(n,k):
        if k == 0: 
            return 1
        elif n < k:
            return 0
        else:
            return choose(n-1, k-1) + choose(n-1, k)

n = 4
two = n//2
one = 0
result = 0

if(n==2):
    print(2)

while two>=0:
    sum = 2 * two
    if(n == sum):
        result += 1
        two-=1
        continue
    
    a = two+(n-sum)
    result += choose(a, two)
    two-=1
    
print(result)


'''
진짜 정답은 피보나치 수열 휴..
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2: return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]