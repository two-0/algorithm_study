
# 9는 소수인가

data = int(input("원소를 입력하세요: "))

def is_prime_number(data):
    for i in range(2, data):
      if data % i == 0:
          return False
      return True

print(is_prime_number(data))