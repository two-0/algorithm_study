## **대표적인 데이터 구조: 해쉬 테이블 (Hash Table)**

## **1. 해쉬 구조**

- Hash Table: 키 (key)에 데이터 (Value)를 저장하는 구조
  - Key를 통해 바로 데이터를 받아올 수 있으므로, 속도가 획기적으로 빨라짐
  - 파이썬 딕셔너리(Dictonary) 타입이 해쉬 테이블의 예
  - 보통 배열로 미리 Hash Table 사이즈만큼 생성 후에 사용 (공간과 탐색 시간을 맞바꾸는 기법)
  - 단, 파이썬에서는 해쉬를 별도로 구현할 이유가 없다 - 딕셔너리 타입을 사용하면 됨

<br><br>

## **2. 알아둘 용어**

- 해쉬(Hash): 임의 값을 고정 길이로 변환하는 것
- 해쉬 테이블(Hash Table): 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
- 해싱 함수(Hashing Function): Key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
- 해쉬 값(Hash Value) 또는 해쉬 주소(Hash Address) Key를 해싱 함수로 연산해서, 해쉬 값을 알아내고, 이를 기반으로 해쉬 테이블에서 해당 Key에 대한 데이터 위치를 일관성있게 찾을 수 있다.
- 슬롯(Slot): 한 개의 데이터를 저장할 수 있는 공간
- 저장할 데이터에 대해 Key를 추출할 수 있는 별도 함수도 존재할 수 있음

![](https://images.velog.io/images/somday/post/1baf4df1-4369-459c-8b38-5687a4ba0837/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202021-02-20%20%EC%98%A4%ED%9B%84%203.08.18.png)

<br><br>

## **3. 간단한 해쉬 예**

**Hash Table 만들기**

```python
hash_table = list([i for in range(10)])
hash_table
```

**간단한 해쉬 함수를 만들어보기**

- 해쉬 함수는 다양한 함수가 있으며, 가장 간단한 방식은 Division 방식이다.

```python
def hash_func(key):
		return key % 5
```

**해쉬 테이블에 저장하기**

- 데이터에 따라 필요시 key 생성 방법 정의가 필요하다.

```python
data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'
data4 = 'Anthor'

# ord(): 문자의 ASCII 코드를 리턴한다.
print (ord(data1[0]), ord(data2[0]), ord(data3[0])
print (ord(data1[0]), hash_func(ord(data1[0])))
```

out

- 65, 68, 84
- 65, 0

**해쉬 테이블에 값 저장 예**

- data: value와 같이 data와 value를 넣으면 해당 data에 대한 key를 찾아서 해당 key에 대응하는 해쉬주소에 value를 저장하는 방식

```python
def storage_data(data, value):
		key = ord(data[0])
		hash_address = hash_func(key)
		hash_table[hash_address] = value
```

**해쉬 테이블에서 특정 주소의 데이터를 가져오는 함수도 만들어보자**

데이터 입력

```python
storage_data('Andy', '01023049383')
storage_data('Dave', '01023948472')
storage_data('Trump', '01043226823')

```

**이제 실제 데이터를 저장하고, 읽어보자**

```python
def get_data(data):
		key = ord(data[0])
		hash_address = hash_func(key)
		return hash_table[hash_address]
```

```python
get_data('Andy')
```

<br>

### 자료 구조 해쉬 테이블의 장단점과 주요 용도

**장점**

- 데이터 저장/읽기 속도가 빠르다 (검색 속도가 빠름)
- 해쉬는 키에 대한 데이터가 있는지 (중복) 확인이 쉬움

**단점**

- 일반적으로 저장공간이 좀더 많이 필요하다.
- 여러 키에 해당하는 주소가 동일한 경우 충동을 해결하기 위한 별도 자료구조가 필요함
- (여러 키에 대한 충돌을 피하는 가장 기본적인 방법은 해쉬 테이블의 공간을 크게 잡으면 충돌을 피할 수 있는 가장 기본적인 방법이 된다.)
- (키 값을 generation 하는 방식도 물론 변경되어야 한다.)

**주요 용도**

- 검색이 많이 필요한 경우
- 저장, 삭제, 읽기가 빈번한 경우
- **캐시 구현시 (중복 확인이 쉽기 때문에)**

<br>

## 다시 이해하기

" **보통 배열로 미리 Hash Table 사이즈만큼 생성 후에 사용(공간과 탐색 시간을 맞바꾸는 기법) "**

이말은 즉, 해쉬 테이블의 내부적 구조는 배열로 생성할 수 있는데 공간과 탐색 시간을 맞바꾼다는 것은 해쉬 테이블의 공간을 크게 할당해서 내부적 충돌을 최대한 배제한다.

이렇게 되면 내부적 충돌을 해결하기 위한 추가적 자원이 들지 않기 때문에 검색 기능의 성능에 영향을 미치지 않고 해쉬 테이블의 장점인 "데이터 저장/읽기의 속도가 빠르다" 를 최적화로 사용이 가능해진다는 의미이다.

<br><br>

## **4. 프로그래밍 연습**

연습1: 리스트 변수를 활용해서 해쉬 테이블 구현해보기

- 해쉬 함수: key % 8
- 해쉬 키 생성: hash(data)

```python
hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value

def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]
```

<br>

```python
save_data('Dave', '01020302002')
save_data('Andy', '01034939485')

read_data('Dave')

결과: '01020302002'
```

<br>

### **분석하기**

`def get_key`

- 먼저 해시 구조는 key, value 이기 때문에 key 값을 얻어야 한다 따라서 get_key 함수를 이용해서 데이터에 값을 key로 변경해야 한다.
- 이때 사용된 방법은 파이썬이 기본적으로 제공하는 hash() 함수를 이용한다.

`def hash_function`

- key % 8을 통해 해쉬 테이블에 저장될 위치를 구하는 함수 이다
- 추후 데이터를 받고 데이터가 해싱 된 후 이 값을 8로 나눈 나머지 값을 최종 저장 위치로 설정 한 것 이다.

`def save_data(data, value)`

- 저장을 하기 위해서 저장될 위치 (data) 값 (value)이 필요 하다. 따라서 인자는 data, value를 받고 들어온 data를 해싱 해주는 get_key 를 타게 하고 그 다음 해당 해싱 값을 % 8의 나머지 값을 저장위치로 지정해주는 hash_function을 타게 된다.
- 그러고 나면 hash_address 라는 주소가 할당되는데 이 주소에 value를 저장하면 된다.

`def read_data(data)`

- 저장된 값을 읽을 때에 먼저 저장된 위치을 알아야 하니 저장 로직이랑 똑같이 먼저 hash_address 값을 알아낸다.
- 그리고 이미 hash 테이블에 값이 저장되어 있기 때문에 저장된 위치를 알기만 하면 바로 return 값으로 저장된 값을 출력할 수 있다.

<br><br>

## 5. 충돌 해결 알고리즘

- 해쉬 테이블의 가장 큰 문제는 충돌(Collision)의 경우입니다. 이 문제를 충돌 또는 해쉬 충돌이라고 부른다.

  **01. Chaining 기법**

- 개방 해싱 또는 Open Hasing 기법 중 하나, 해쉬 테이블 저장공간 외의 공간을 활용하는 기법이다.
- 충돌이 일어나면 링크드 리스트라는 자료 구조를 이용해서, 링크드 리스트로 데이터를 추가로 뒤에 연결시켜서 저장하는 기법이다.

<br>

### 연습2: 연습 1의 해쉬 테이블 코드에 Chaining 기법으로 충돌해결 코드를 추가해보기

1. 해쉬 함수: key % 8
2. 해쉬 키 생성: hash(data)

**코드**

```python
hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None
```

**해쉬 키를 별도의 저장 공간에 할당하는 이유** `index_key = get_key(data)`

- 해쉬 테이블의 저장 위치를 정할 때 key % 5로 했을 경우 동일한 위치가 될 수 있다.
- 예를 들어 해쉬 값이 11과 21 일 경우 % 5를 할 경우 1 이라는 동일한 위치가 된다.
- 동일한 위치에 Linked List - Chaining 기법을 이용해 저장을 했다고 가정하면 아래의 그림과 같이 된다.

**예시**
![](https://images.velog.io/images/somday/post/60c69370-5a9f-4bd1-b55e-fa9927389be2/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202021-02-20%20%EC%98%A4%ED%9B%84%202.37.14.png)

- 이 때 첫번째 값이 내가 원하는 데이터인지 두 번째 값이 내가 원하는 값이 알 수가 없게 되는데 (실제 저장은 Andy's phone 와 같은 방식으로 저장되는게 아니라 임의의 길이의 int 값으로 저장되기 때문에)
- 이를 식별 하기 위해 우리는 index 값을 사용해서 식별할 수 있도록 한다.

<br>

**해쉬 값을 통한 address 위치가 겹치는 경우, 리스트 형식으로 값을 저장하기 위해 해쉬 테이블의 저장 위치의 index 값과 index_key의 값이 동일한 경우 다음 칸에는 value로 덮어 쓰운다 >>> 리스트로 관리하기 위해서**

**코드**

```python
for index in range(len(hash_table[hash_address])):
         if hash_table[hash_address][index][0] == index_key:
             hash_table[hash_address][index][1] = value
             return
```

- 해쉬 테이블의 저장 위치에 이미 값이 있을 경우 우리는 연결리스트로 chaining을 제공하는데 연결리스트를 직접 구현하는 것은 비효율적이기 때문에 이와 유사한 파이썬의 리스트를 사용할 것이다.
- 그리고 리스트를 사용할 것이기 때문에 index0, index1을 하나의 list로 사용할 것이다. [index1, index2] 와 같은 형태
- index1에는 key가 들어가고 index2에는 value가 들어가는 것으로 덮어 쓰게 한다.

**최종 메모리 모형**

![](https://images.velog.io/images/somday/post/20d28242-27e8-489e-805e-bfce22d92125/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202021-02-20%20%EC%98%A4%ED%9B%84%202.54.06.png)

<br>

만약 hash_adrress 값이 0일 경우 (즉, 하나도 겹치지 않은 경우) 위에서 언급한 것처럼 리스트로 관리하기 때문에 `[[index_key, value]]` 형태로 hash_address 에 저장한다.
<br>

**코드**

```python
for index in range(len(hash_table[hash_address])):
         if hash_table[hash_address][index][0] == index_key:
             hash_table[hash_address][index][1] = value
             return
		hash_table[hash_address].append([index_key, value])
else:
		hash_table[hash_address] = [[index_key, value]]
```

<br>

`read_data(data)`

- 데이터를 읽어오는 것은 체이닝으로 저장하는 것보단 간편하다.
- 우선 로직은 hash_table[hash_address] 의 위치에 0이 아닌 값이 있어야 한다.
- 0 이 아닌 값이 존재한다면 이제 체이닝이 되어 있는 만큼 for 문을 통해 루프를 돌게되고
- 리스트 형식으로 저장된 해쉬 테이블의 index 가 index_key와 동일한지 찾는다. → 즉 우리가 찾는 index_key인지를 검사하느 것이다.
- 맞다면 그 리스트의[1] 값을 리턴 하면 value가 나오게 된다.
