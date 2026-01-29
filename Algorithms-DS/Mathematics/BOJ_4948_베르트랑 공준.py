# 4948
# 베르트랑 공준

import sys

# 1. 최대 범위까지 소수 리스트를 미리 만들기 (에라토스테네스의 체)
MAX = 123456 * 2
is_prime_list = [True] * (MAX + 1)
is_prime_list[0] = is_prime_list[1] = False

for i in range(2, int(MAX**0.5) + 1):
    if is_prime_list[i]:
        for j in range(i*i, MAX + 1, i):
            is_prime_list[j] = False

# 2. 입력 처리
def solve():
    line = sys.stdin.readline()
    if not line: return False
    n = int(line)
    
    if n == 0:
        return False
    
    # 미리 구해놓은 리스트에서 n < x <= 2n 범위의 소수 개수만 세기
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if is_prime_list[i]:
            count += 1
    print(count)
    return True

while solve():
    pass