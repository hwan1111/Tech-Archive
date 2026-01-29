# 4134 
# 다음 소수
import sys

def is_prime(n):
    if x < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

n = int(sys.stdin.readline())
for _ in range(n):
    x = int(sys.stdin.readline().strip())
    while True:
        if is_prime(x):
            print(x)
            break
        x += 1