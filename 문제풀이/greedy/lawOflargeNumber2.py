# 문제:  큰 수의 법칙
# n: 배열의 크기
# m: 숫자가 더해지는 횟수
# k: 반복해서 더 할 수 있는 최대 횟수

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k
count = count + m % (k+1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)