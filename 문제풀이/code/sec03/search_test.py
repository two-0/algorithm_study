
# 다양한 자료형인 시퀀스에서 검색하기


from seq_serch import seq_search

print('실수를 검색합니다.')
print('주의: End를 입력하면 종료 합니다.')

number = 0
x = []

while True:
    s = input(f'x[{number}]: ')
    if s == 'End':
        break
    x.append(float(s))
    number+=1

ky = float(input('검색할 값을 입력하세요.: '))

idx = seq_search(x, ky)
if idx == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 x[{idx}]에 잇습니다.')