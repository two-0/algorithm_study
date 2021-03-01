## **해쉬 테이블 충돌 해결 하기**

## Linear Probling 기법

- 폐쇄 해싱 또는 Close Hashing 기법 중 하나이다.
- 테이블 저장공간 안에서 충돌 문제를 해결하는 기법
- 충돌이 일어나면 해당 hash address의 다음 address 부터 맨 처음 나오는 빈공간에 저장하는 기법
  - 저장공간 활용도를 높이기 위한 기법

### 연습3:연습 1의 해쉬 테이블 코드에 Linear Probling 기법으로 충돌해결 코드를 추가해보기

1. 해쉬 함수: key % 8
2. 해쉬 키 생성: hash(data)

```python
hash_table = list([0 for index in range(8)])

def get_key(data):
    return hash(data)

# 해쉬 테이블의 저장될 위치를 결정한다.
def hash_func(key):
    return key % 8:

def save_data(data, value):
    # 내부적으로 해쉬 데이터를 구분하기 위해서 index를 부여한다.
    index_key = get_key(data)
    hash_address = hash_func(index_key)

    # hash_address != 0이라는 것은 현재 key에 이미 값이 있다는 의미
    if (hash_table[hash_adrress]) != 0:
        # 현재 위치가 빈공간이 아니기 때문에 빈공간을 찾기 위해 현재 위치부터
        # hash_table의 길이만큼 순회 하며 빈공간을 찾는다.
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            # 만약 저장될 위치의 key가 충돌했는데 현재 받은 데이터의 key의 index가 동일하게 되면
            # value 만 업데이트 한다.
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    # key에 Data가 없다면 해당 위치에 바로 저장한다.
    else:
        hash_table[hash_address] = [index_key, value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_func(index_key)

    # hash_table의 hash_address 0이 아니란 것은 데이터가 있다는 것
    if hash_table[hash_address] != 0:
        # 데이터가 존재하기 때문에 데이터를 찾기 위해 현재 위치에서 부터 쭉 순회하며 데이터를 찾는다.
        for index in range(hash_address, len(hash_table)):
            # 해쉬 테이블의 index가 0 이라는 것은 한 번도 해당 데이터가 해싱 된 적이 없다는 의미
            # index는 hash(data) 를 해서 나온 key이기 때문인데
            # 이 key가 없다는 것은 해당 데이터는 저장된 적이 없다는 것을 의미한다.
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None
```

<br><br>

## **빈번한 충돌을 개선하는 기법**

- 해쉬 테이블들 사용할 때 충돌이 빈번하게 일어난다는 것은 해쉬 테이블 성능에 많은 영향을 미친다.
- 그 이유는 충돌을 해결하기 위해 for 문 을 타게 되는데 for문은 성능 저하를 일으키는 주요 원인이 되기 때문이다.
- 따라서 우리는 현재 Hash Table이 충돌이 빈번하게 일어난다면 빈번하게 발생하지 않도록 기법을 개선할 필요가 있다.

### 방법

- 해쉬 함수를 재정의 및 해쉬 테이블 저장공간을 확대 한다.
- Ex:

```python
hash_table = list([None for in range(16)])

def hash_function(key);
		return key % 16
```

<br>

### 참고: 해쉬 함수와 키 생성 함수

- 파이썬의 `hash()` 함수는 실행할 때마다, 값이 달라질 수 있다.
- 유명한 해쉬 함수들이 존재한다. (SHA: Secure Hash Algorithm, 안전한 해시 알고리즘)
  - 어떤 데이터도 유일한 고정된 크기의 고정값을 리턴해주므로, 해쉬 함수로 유용하게 활용 가능하다.

**SHA -1**

```python
import hashlib

data = 'test'.encode()
hash_object = hashlib.sha1()
hash_object.update(data)
hex_dig = hash_object.hexdigest()

print (hex_dig)
```

<br> <br>

**SHA - 256**

```python
import hashlib

data = 'test'.encode()
hash_object = hashlib.sha256()
hash_object.update(data)
hex_dig = hash_object.hexdigest()

print(hex_dig)
```

<br>

### 연습4. 연습2의 Chaining 기법을 적용한 해쉬 테이블 코드에 키 생성 함수들 sha256 해쉬 알고리즘을 사용하도록 변경하기

1. 해쉬 함수: key % 8
2. 해쉬 키 생성: hash(data)

```python
import hashlib

hash_table = list([0 for i in range(8)])

def get_key(data):
        hash_object = hashlib.sha256()
        hash_object.update(data.encode())
        hex_dig = hash_object.hexdigest()
        return int(hex_dig, 16)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key, value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None
```

<br>

### **get_key(data): 를 변경하자**

- 연습4 번을 해결하는 방법을 저는 get_key(data)를 변경하는 것으로 했습니다.
- 먼저 파이썬의 라이브러리인 hashlib을 사용해 sha256을 사용합니다.
- 그리고 data는 문자열로 들어올 것이기 때문에 **encode를 통해 byte 값으로 변경합니다**
- 그리고 byte 된 값을 다시 16진수 값으로 바꾼 뒤 리턴 합니다.
- 다만 여기서 get_key는 정수를 리턴해야 hash_function에서 % 8을 할 수 있기 때문에 16진수 값을 int로 parsing을 해준 뒤 리턴 합니다.

## 시간 복잡도

- 일반적인 경우 (충돌이 없는 경우): O(1)
- 최악의 경우 (충돌이 모두 발생하는 경우): O(n)

> 해쉬 테이블의 경우, 일반적인 경우를 기대하고 만들기 때문에 시간 복잡도는 O(1) 이라고 말할 수 있다.

### 검색에서 해쉬 테이블의 사용 예

- 16개의 배열에 데이터를 저장하고 검색할 때 O(n)
- 16개의 데이터 저장공간을 가진 위의 해쉬 테이블에 데이터를 저장하고 검색할 때 O(1)
