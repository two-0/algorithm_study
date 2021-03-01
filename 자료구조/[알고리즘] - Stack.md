## **꼭 알아둬야 할 자료 구조: 스택 (Stack)**

- 데이터를 제한적으로 접근할 수 있는 구조
  - 한쪽 끝에서만 자료를 넣거나 뺄 수 있는 구조
- 가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조
  - 큐: FIFO
  - 스택: LIFO

<br>

### **1. 스택 구조**

- 스택은 LIFO (Last In First Out)
- 대표적인 스택의 활용
  - 컴퓨터 내부의 프로세스 구조의 함수 동작 방식
- 주요 기능
  - push(): 데이터를 스택에 넣기
  - pop(): 데이터를 스택에서 꺼내기

<br>

### **2. 스택 구조와 프로세스 스택**

- 스택 구조는 프로세스 실행 구조의 가장 기본
- 함수 호출시 프로세스 실행 구조를 스택과 비교해서 이해가 필요

**프로세스 함수의 스택 구조의 예시**

```python
def recursive(data):
	if data < 0:
			print("ended")
	else
			print(data)
			recursive(data - 1)
		  print("returned", data)
```

**결과**

![](https://images.velog.io/images/somday/post/0fb0fed6-643c-4e56-b384-685b68d8ccac/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202021-02-16%20%EC%98%A4%ED%9B%84%209.32.10.png)

<br>

### **자료 구조 스택의 장단점**

- 장점
  - 구조가 단순해서 구현이 쉽다.
  - 데이터 저장, 읽기 속도가 빠르다
- 단점 (일반적인 스택 구현시)
  - 데이터 최대 갯수를 미리 정해야 한다.
    - 파이썬의 경우 재귀는 1000번까지 호출 가능
  - 저장 공간의 낭비가 발생할 수 있다.
    - 미리 최대 갯수만큼 저장공간을 확보해야 한다.

> 스택은 단순하고 빠른 성능을 위해 사용되므로, 보통 배열 구조를 활용해서 구현하는 것이 일반적임 이 경우 위에서 열거한 단점이 존재할 수 있다.

<br>

### **4. 파이선 리스트 기능에서 제공하는 메서드로 스택 사용해보기**

- append(push) , pop 메서드 제공

```python
data_stack = list()

data_stack.append(2)
data_stack.append(3)

data_stack
data_stack.pop()
```

<br>

**결과**

![](https://images.velog.io/images/somday/post/ea453178-890f-4914-a3fb-b8b54451b553/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202021-02-16%20%EC%98%A4%ED%9B%84%209.47.53.png)

<br>

### **5. 프로그래밍 연습**

**연습1: 리스트 변수로 스택을 다루는 POP, PUSH 기능 구현해보기 (pop, push 사용하지 않고 직접 구현)**

```python
stack_list = list()

def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data

def push(data):
    stack_list.append(data)

for index in range(10):
    push(index)

pop()
```

<br>

**결과**

![](https://images.velog.io/images/somday/post/5829d965-669c-4cef-9815-b90d9fc88683/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202021-02-16%20%EC%98%A4%ED%9B%84%209.54.39.png)
