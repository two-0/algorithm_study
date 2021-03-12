

# for 문을 이용한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search_use_for (a: Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

### 생략 