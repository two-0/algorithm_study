

# 문제 1이 될 때 까지
#  일단 K = N인지
# 아니라 면 K % N == 0 인지
# 아니라면 K -1 % N  == 0 인지


n, k = map(int, input('n 과 k를 입력하세요: ').split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k) * k
    print(result, target, n)
    result += (n - target)
    print("target:", target, "result:", result)
    n = target

    if n < k:
        break
    result += 1
    n //= k
    print(result, n)


# N 이 1보다 크다면 1이 될 수 있도록 해주기 위해 빼준다.
print(result, n)
result += (n-1)
print(result)
