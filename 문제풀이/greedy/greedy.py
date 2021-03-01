money = int(input("거스름돈은 얼마인가요: "))

count = 0

coin_types = [500, 100, 50 ,10]

for coin in coin_types:
    count += money // coin
    money %= coin

print(count)