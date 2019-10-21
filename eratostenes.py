n = int(input())
# エラトステネスの篩実装, indexと数が一致している
is_prime = [True for _ in range(n + 1)]
# 0と1は素数でないので省く
is_prime[0] = is_prime[1] = False

prime_count = 0

for i in range(n):
    if is_prime[i] is True:
        prime_count += 1
        for c in range(i, n + 1, i):
            is_prime[c] = False

print(prime_count)
