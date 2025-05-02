# import heapq
| 함수                          | 설명 |
|-------------------------------|------|
| `heapq.heappush(heap, item)` | `item`을 힙에 추가 |
| `heapq.heappop(heap)`        | 가장 작은 원소 제거 후 반환 |
| `heapq.heappushpop(heap, item)` | `item`을 넣고 가장 작은 원소를 pop (더 빠름) |
| `heapq.heapreplace(heap, item)` | 가장 작은 원소 제거 후 `item` 추가 |
| `heapq.heapify(list)`        | 일반 리스트를 힙 구조로 변환 |
| `heapq.nlargest(n, iterable)` | 가장 큰 n개 요소 리턴 |
| `heapq.nsmallest(n, iterable)` | 가장 작은 n개 요소 리턴 |
---
# from itertools import collections, permutations, product
| 구분 | 개념 설명 | 중복 허용 | 순서 고려 | 예시 (A, B, C 중 2개 뽑기)|
|---------------|----------------------------------------------|------------|-------------|----------------------------------|
| 순열 (Permutation)  | 순서를 **고려**하여 **r개를 선택**               | ❌        | ✅         | AB, AC, BA, BC, CA, CB           |
| 조합 (Combination)  | 순서를 **고려하지 않고** **r개를 선택**         | ❌        | ❌         | AB, AC, BC                        |
| 곱 (Product, 중복순열) | 중복을 **허용**하면서 모든 **자리 수 조합** 생성 | ✅        | ✅         | AA, AB, AC, BA, BB, BC, CA, CB... |

``` python
a = [1, 2]
b = ['A', 'B']
# 중복 조합
print(list(product(a, b)))
# [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]

# 자기 자신과 곱 (repeat)
print(list(product([0, 1], repeat=2)))
# [(0, 0), (0, 1), (1, 0), (1, 1)]


a = [1, 2, 3]
# 조합
print(list(combinations(a, 2)))
# [(1, 2), (1, 3), (2, 3)]

# 순열
print(list(permutations(a, 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
```
---
# DFS, BFS
``` python
# DFS - 재귀 기반
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# DFS - 스택 사용
def DFS(graph, root): # stack
    visited = []
    stack = [root]
 
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack+= graph[n] - set(visited)
    return visited

# BFS - 큐 사용
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
```
---
# lambda 사용 - 정렬
``` python
array.sort(key = lambda data : data[1]) #1번 인덱스 기준 정렬
print(array)

# 평소 -> 0번 인덱스 기준 , 아래 예시 -> 0,1번 인덱스 기준
print(sorted(array,key = lambda x:  (x[0],x[1])))

# 비교 기준을 x*3으로 두고 정렬
numbers.sort(reverse=True, key = lambda x:x*3)
```
---
# set 연산
``` python
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

# 교집합
print(list(set(a) & set(b)))  # [3, 4]

# 합집합
print(list(set(a) | set(b)))  # [1, 2, 3, 4, 5, 6]

# 차집합
print(list(set(a) - set(b)))  # [1, 2]

# 대칭차집합
print(list(set(a) ^ set(b)))  # [1, 2, 5, 6]
```
---
# 형변환
| 함수 | 설명 | 예제 |
|------|------|------|
| `int(x)` | 정수로 변환 | `int("10")` → `10` |
| `float(x)` | 실수로 변환 | `float("3.14")` → `3.14` |
| `str(x)` | 문자열로 변환 | `str(123)` → `"123"` |
| `bool(x)` | 불리언으로 변환 | `bool(0)` → `False`, `bool("hi")` → `True` |
| `list(x)` | 리스트로 변환 | `list("abc")` → `['a', 'b', 'c']` |
| `tuple(x)` | 튜플로 변환 | `tuple([1,2,3])` → `(1, 2, 3)` |
| `set(x)` | 집합(set)으로 변환 | `set([1,2,2,3])` → `{1, 2, 3}` |
| `dict(x)` | 딕셔너리로 변환 | `dict([("a",1),("b",2)])` → `{'a':1,'b':2}` |
---
# from collections import deque
| 메서드 | 설명 |
|------|------|
| append(x) |	오른쪽 끝에 x 추가|
| appendleft(x) |	왼쪽 끝에 x 추가|
| pop() | 오른쪽 끝 요소 제거 및 반환|
| popleft() | 왼쪽 끝 요소 제거 및 반환|
| extend(iterable) | iterable의 모든 요소를 오른쪽에 추가|
| extendleft(iterable) | iterable의 모든 요소를 왼쪽에 추가 (역순으로 들어감)|
| remove(x)	| 첫 번째로 나오는 x 제거
| clear()	| 모든 요소 제거
| reverse()	| 요소 순서 뒤집기
| rotate(n)	| n만큼 회전 (양수: 오른쪽, 음수: 왼쪽)
| count(x)	| x의 개수 반환
| index(x, start, stop)	| x의 인덱스 반환 (start~stop 범위)|
---
# zip, enumerate
``` python
temp1 = [1, 3, 5]
temp2 = [2, 4, 6]

for n1, n2 in zip(temp1, temp2):
	print(n1, n2)
    
temp = ['k', 'o', 'r', 'e', 'a']

for idx, value in enumerate(temp):
	print(idx, value)
```
--- 
# dict
### 기본 사용
| 함수/메서드                | 설명                                               | 예시 코드                                | 반환값/효과         |
|----------------------------|----------------------------------------------------|------------------------------------------|---------------------|
| `d.get(key, default)`      | 키의 값을 반환, 없으면 default 반환                | `d.get('a', 0)`                          | 값 또는 default     |
| `d.keys()`                 | 모든 키 반환(뷰 객체)                             | `d.keys()`                               | dict_keys 객체      |
| `d.values()`               | 모든 값 반환(뷰 객체)                             | `d.values()`                             | dict_values 객체    |
| `d.items()`                | (키, 값) 쌍 반환(뷰 객체)                        | `d.items()`                              | dict_items 객체     |
| `d.pop(key[, default])`    | 키의 값을 반환하고, 해당 항목 삭제                 | `d.pop('a', 0)`                          | 값 또는 default     |
| `d.popitem()`              | 임의의 (키, 값) 쌍 삭제 및 반환 (3.7+는 마지막)   | `d.popitem()`                            | (키, 값) 튜플       |
| `d.clear()`                | 모든 항목 삭제                                    | `d.clear()`                              | None                |
| `d.update([other])`        | 다른 dict나 (키, 값)쌍으로 여러 항목 추가/수정    | `d.update({'a': 10, 'b': 20})`           | None                |
| `d.setdefault(key, default)`| 키가 없으면 추가 후 값 반환, 있으면 기존 값 반환 | `d.setdefault('a', 100)`                 | 값                  |
| `d.copy()`                 | 얕은 복사본 반환                                  | `d2 = d.copy()`                          | dict                |
| `dict.fromkeys(keys, value)`| keys로 새 dict 생성, 모든 값은 value             | `dict.fromkeys(['x','y'], 0)`            | dict                |
---
### 예시
``` python
d = {'a': 1, 'b': 2}

d.get('a')           # 1
d.get('c', 0)        # 0

list(d.keys())       # ['a', 'b']
list(d.values())     # [1, 2]
list(d.items())      # [('a', 1), ('b', 2)]

d.pop('a')           # 1, d는 {'b': 2}
d.update({'c': 3})   # d는 {'b': 2, 'c': 3}
d.setdefault('d', 4) # 4, d는 {'b': 2, 'c': 3, 'd': 4}
d.clear()            # d는 {}
```
### 정렬
``` python
dic = {'apple': 3, 'banana': 1, 'pear': 5}
sorted(dic.item(), key = lambda x: x[1])
```
---
# 리스트 관련 함수
``` python
a.append(2) 					# a의 마지막 원소로 삽입
a.sort()						# 오름차순 정렬
a.sort(reverse = True)			# 내림차순 정렬
a.reverse()						# 원소의 순서를 뒤집음
a.insert(2, 3)					# 인덱스 2에 원소 3을 삽입
a.remove(1)						# 값이 1인 원소를 제거. 원소가 여러 개면 하나만 제거
```
---
# 문자열
| 함수 | 설명 | 예시 |
|------|------|------|
| `len()` | 문자열 길이 반환 | `len("Hello")` → `5` |
| `lower()` | 모든 문자 소문자화 | `"Hello".lower()` → `"hello"` |
| `upper()` | 모든 문자 대문자화 | `"hello".upper()` → `"HELLO"` |
| `capitalize()` | 첫 문자만 대문자화 | `"hello".capitalize()` → `"Hello"` |
| `title()` | 각 단어의 첫 문자만 대문자화 | `"hello world".title()` → `"Hello World"` |
| `strip()` | 양쪽 공백 제거 | `"  hello  ".strip()` → `"hello"` |
| `replace(old, new)` | 특정 문자 치환 | `"hello".replace("e", "a")` → `"hallo"` |
| `split(sep)` | 구분자로 분리하여 리스트 반환 | `"apple,banana,grape".split(",")` → `['apple', 'banana', 'grape']` |
| `join(iterable)` | 구분자 문자열로 iterable의 요소 합침 | `",".join(["apple", "banana", "grape"])` → `"apple,banana,grape"` |
| `find(sub)` | 부분 문자열 찾기 (없으면 -1 반환) | `"hello".find("e")` → `1` |
| `index(sub)` | 부분 문자열 찾기 (없으면 예외 발생) | `"hello".index("e")` → `1` |
| `count(sub)` | 부분 문자열의 개수 세기 | `"hello".count("l")` → `2` |
| `startswith(prefix)` | 문자열이 특정 접두사로 시작하는지 확인 | `"hello".startswith("he")` → `True` |
| `endswith(suffix)` | 문자열이 특정 접미사로 끝나는지 확인 | `"hello".endswith("lo")` → `True` |
| `isalpha()` | 알파벳만 있는지 확인 | `"abc".isalpha()` → `True` |
| `isdigit()` | 숫자만 있는지 확인 | `"123".isdigit()` → `True` |
| `isspace()` | 공백만 있는지 확인 | `"   ".isspace()` → `True` |
---
### 활용
``` python
a = "Hello"
b = "World"
result = a+b		# HelloWorld
result = a+" "+b	# Hello World
result = a[2:]		# 마찬가지로 슬라이싱이 가능하다. llo
```
### 뒤집기
``` python
string = 'Welcome SJKOding!'
print(string[::-1])
# !gnidOKJS emocleW
```
---
# 숫자
### 내장함수
| 함수명               | 설명                                               | 예시 코드              | 반환값/결과         |
|----------------------|----------------------------------------------------|------------------------|---------------------|
| abs(x)               | x의 절댓값 반환                                    | abs(-5)                | 5                   |
| round(x, n)          | x를 소수점 n자리까지 반올림 (n 생략 시 정수)        | round(3.1415, 2)       | 3.14                |
| pow(x, y[, z])       | x의 y제곱 (z 지정 시, (x**y) % z)                  | pow(2, 3), pow(2, 3, 3)| 8, 2                |
| divmod(x, y)         | (x를 y로 나눈 몫, 나머지) 튜플 반환                | divmod(7, 3)           | (2, 1)              |
| sum(iterable[, start])| iterable의 합계 (start부터 시작)                   | sum([1,2,3], 10)       | 16                  |
| min(iterable, ...)   | 최소값 반환                                        | min(1, 2, 3)           | 1                   |
| max(iterable, ...)   | 최대값 반환                                        | max([1, 5, 3])         | 5                   |
| int(x)               | x를 정수로 변환                                    | int(3.7)               | 3                   |
| float(x)             | x를 실수로 변환                                    | float(5)               | 5.0                 |
| complex(a, b)        | 복소수 생성                                        | complex(2, 3)          | (2+3j)              |
| bin(x)               | x의 2진수 문자열 반환                              | bin(10)                | '0b1010'            |
| oct(x)               | x의 8진수 문자열 반환                              | oct(10)                | '0o12'              |
| hex(x)               | x의 16진수 문자열 반환                             | hex(10)                | '0xa'               |
| type(x)              | x의 자료형 반환                                    | type(3.14)             | <class 'float'>     |
---
### math
``` python
import math

print(math.ceil(3.14))   # 4   (올림)
print(math.floor(3.14))  # 3   (내림)
print(round(3.14))       # 3   (반올림, 내장 함수)
```