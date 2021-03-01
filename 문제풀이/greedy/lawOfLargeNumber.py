# 문제:  큰 수의 법칙
# n: 배열의 크기
# m: 숫자가 더해지는 횟수
# k: 반복해서 더 할 수 있는 최대 횟수

n, m, k = map(int,input().split())
data = list(map(int, input().split()))

# 오름차순 정렬
data.sort()
first = data[n - 1]
second = data[n - 2]
result = 0


while True:
    # 가장 큰 수를 k번 더한다.
    for i in range(k):
        # 만약 m(더 해지는 횟수가 0이면 반복문 종료)
        if m == 0:
            break
            # m이 0아니라면 k번 만큼 first(제일 큰 값을 더한다)
        result += first
            # m번 의 횟수가 끝나면 종료되어야 하기 때문에 m은 --
        m -= 1
        # m번이 모두 수행되었다면 종료
    if m == 0:
        break
        # 남은 홧수 만큼 두번 째 큰값을 더한다.
    result += second
    # m이 0이 되면 종료 되어야 하기 때문에 m --
    m -= 1

print(result)