# 1000까지의 수중 소수인 수 찾기

for i in range(2, 1001):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)