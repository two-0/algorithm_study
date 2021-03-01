## 1. 트리 (Tree) 구조

- 트리: Node 와 Branch를 이용해서, 사이클을 이루지 않도록 구성한 데이터 구조
- 실제로 어디에 많이 사용되나?
    - 트리 중 이진 트리 (Binary Tree) 형태의 구조로 **탐색(검색) 알고리즘 구현을 위해 많이 사용됨**

<br><br>

## 2. 알아둘 용어

`Node`

- 트리에서 데이터를 저장하는 기본 요소 (데이터와 다른 연결된 노드에 대한 Branch 정보 포함)

`Root  Node`

- 트리 맨 위에 있는 노드

`Level`

- 최상위 노드를 Level 0으로 하였을 때, 하위 Bracnh로 연결된 노드의 깊이를 나타냄

`Parent Node`

- 어떤 노드의 다음 리벨에 연결된 노드

`Child Node`

- 어떤 노드의 상위 레벨에 연결된 노드

`Leaf Node (Terminal Node)`

- Child Node가 하나도 없는 노드

`Sibling (Brother Node)`

- 동일한 Parent Node를 가진 노드

`Depth`

- 트레이서 Node가 가질 수 있는 최대 Level

![](https://images.velog.io/images/somday/post/95128d8f-a954-4e33-9fd9-f8ee0568de1d/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202021-02-24%20%EC%98%A4%ED%9B%84%203.19.31.png)

<br><br>

## 3. 이진 트리와 이진 탐색 트리 (Binary Search Tree)

이진 트리

- 노드의 최대 Branch가 2인 트리

이진 탐색 트리 (Binary Search Tree, BST)

- 이진 트리에 다음과 같은 추가적인 조건이 있는 트리
- 조건
    - 왼쪽 노드는 해당 노드보다 작은 값, 오른쪽 노드는 해당 노드보다 큰 값을 가지고 있다.

<br><br>

## 4. 자료 구조 이진 탐색 트리의 장점과 주요 용도

- 주요 용도: 데이터 검색(탐색)
- 장점: 탐색 속도를 개선할 수 있음

<br><br>

## 5. 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현하기

- Tree 자료구조는 이중 연결리스트로 구현한다.
- 따라서 먼제 연결 리스트 객체를 구현해보자

**노드 클래스 만들기**

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

<br>


이진 탐색 트리에 데이터 넣기

- 이진 탐색 트리 조건에 부합하게 데이터를 넣어야 한다.

```python
class NodeMgmt:
    def __init__(self, head):
        self.head = head
    
    def insert(self, value):
        # 순회를 하기위해사 현재의 노드를 알아야한다.
        self.current_node = self.head
        while True:
            # value는 새로 들어오는 노드의 값
            # 즉 현재의 노드보다 새로 들어오는 노드의 값이 더 작기 때문에
            # 왼쪽으로 가야 한다.
            if value < self.current_node.value:
           
            # 왼쪽으로 가는데 이제 왼쪽에 branch가 없다면 곧 바로 왼쪽으로 들어가면 되지만
            # 값이 있을 수도 있기 때문에 분기처리 한다.
            # 이 if 는 값이 있는 것에 대한 분기
                if self.current_node.left != None:
                    
                    # 이미 head 노드와 비교가 끝나고 왼쪽으로 이동했기에 
                    # 왼쪽에 이미 존재하는 node와 입력 value를 비교하기 위해 current_node를 변경한다.
                    # 그리고 다시 while로 돌어가 비교를 한다.
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break

            # 이제 현재 value가 current value 보다 큰 경우에 대한 분기처리이다.
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
       # insert와 마찬가지로 순회를 하기 위해 현재 노드를 알아야 한다.
       self.current_node = self.head
      
       # 순회를 하는데 current_node가 None이 아닐때 까지 순회를 함
    while self.current_node:
        
        # 이제 현재의 value가 입력값의 value와 동일한지 검사한다.
        # 동일하다면 검색 하는 값이 있기 때문에 True를 리턴   
        if self.current_node.value == value:
            return True
		 # 여기는 값이 일치 하지 않기 때문에 이진 탐색트리 조건에 맞게 입력 값과 현재 value의 크기를 보고
		 # 왼쪽으로 갈지 우측으로 갈지 분기처리 한다.
		 # 현재 조건은 입력값이 현재 value보다 작기 때문에 왼쪽으로 가서 현재 value를 갱신한다. 그리고 다시 while문을 탄다.
        elif value < self.current_node.value:
            self.current_node = self.current_node.left
        
        # 값이 크다면 우측으로 가서 현재 node를 우측의 node로 변경하고 while을 돈다
         else:
            self.current_node = self.current_node.right
      # while 과정을 다 거쳤는데도 True 반환이 없어 이곳으로 왔다면 찾는 값이 없기 때문에 false를 리턴하고 끝난다. 
        return False
```

<br> <br>

## **정리**

- 트리는 Node 와 Branch를 이용해서, 사이클을 이루지 않도록 구성한 데이터 구조 이다.
- 이진 트리는  트리에서 Branch가 최대 2개만 허용되는 트리이다.
- 이진 트리는 데이터 검색을 하는데 있어 매우 빠른 퍼포먼스를 보여준다.