def split(n, k):
    sum_splits = 0
    while n >= k:
        x = n // k
        y = n % k
        sum_splits += x  
        n = x + y  
    if n>1:
        sum_splits += 1
    return sum_splits

def solve():
    x, y = map(int, input().split())
    if x == 1:
        print(0)
    else:
        print(split(x, y))

t = int(input())
for _ in range(t):
    solve()
