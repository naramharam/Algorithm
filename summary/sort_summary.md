# 정렬

### 선택 정렬

- 가장 작은 것을 선택해서 제일 앞으로 보내는 알고리즘

![img](https://t1.daumcdn.net/cfile/tistory/256B9C34545081D835)



`다음의 숫자들을 오름차순으로 정렬하는 프로그램을 작성하세요.`

`1 10 5 8 7 6 4 3 2 9`

```python
def selection_sort(array):

    for i in range(0, len(array)-1):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
        print(array)


array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
selection_sort(array)
```

`result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

- **선택 정렬의 시간 복잡도는 O(N^2) 이다.**

- 선택 정렬은 비효율적인 알고리즘 중 하나이다.



---

### 버블정렬

- 옆에 있는 값과 비교해서 더 작은 값을 반복적으로 앞으로 보내는 알고리즘 
- 선택 정렬과 같이 몸시 직관적인 해결 방법
-  뒤에서 부터 집합의 크기를 하나 씩 줄여 나가야 된다.

![img](https://t1.daumcdn.net/cfile/tistory/275F9A4A545095BD01)

`다음의 숫자들을 오름차순으로 정렬하는 프로그램을 작성하세요.`

`1 10 5 8 7 6 4 3 2 9`

```python
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print(array)

bubble_sort([1, 10, 5, 8, 7, 6, 4, 3, 2, 9])
```

`result =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] `

- **버블 정렬의 시간 복잡도는 선택정렬의 시간 복잡도와 동일한 O(n^2) 이다.**
- 일반적으로 정렬 알고리즘 중 가장 느리다.

---

### 삽입 정렬

- 각 숫자를 적절한 위치에 삽입하는 방법
- 다른 정렬 방식들은 무조건 위치를 바꾸는 방식이었다면 삽입 정렬은 **필요할 때만** 위치를 바꾸게 된다.

![img](https://t1.daumcdn.net/cfile/tistory/2569FD3854508BE811)

`다음의 숫자들을 오름차순으로 정렬하는 프로그램을 작성하세요.`

`1 10 5 8 7 6 4 3 2 9`

```python
def insert_sort(array):
    for i in range(len(array)-1):
        j = i
        while array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            j = j - 1

    print(array)

insert_sort([1, 10, 5, 8, 7, 6, 4, 3, 2, 9])
```

`result =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

- **선택 정렬의 시간 복잡도는 O(N^2) 이다.**
- 위 3가지 정렬 중 가장 효과적인 정렬 방법이다.

---

### 퀵 정렬

- 대표적인 '분할 정복' 알고리즘이다.
- 퀵 정렬은 하나의 큰 문제를 두 개의 작은 문제로 분할하는 식으로 빠르게 정렬 한다. **즉, 특정한 값을 기준으로 큰 숫자와 작은 숫자를 서로 교환한 뒤에 배열을 반으로 나눈다.**
- 퀵 정렬에서는 **기준 값**이 있다. 이를 **피벗(Pivot)** 이라고 한다.

##### 알고리즘

1. 리스트 가운데서 하나의 원소를 고른다. 이렇게 고른 원소를 **피벗**이라고 한다.
2. 피벗 앞에는 피벗보다 값이 작은 원소들이 오고, 피벗 뒤에는 피벗보다 값이 큰 모든 원소들이 오도록 피벗을 기준으로 리스트를 둘로 나눈다. 이렇게 리스트를 둘로 나누는 것을 **분할** 이라고 한다. 분할을 마친 뒤에 피벗은 더 이상 움직이지 않는다.
3. 분할된 두 개의 작은 리스트에 대해 **재귀(Recursion)** 적으로 이 과정을 반복한다. 재귀는 리스트의 크기가 0이나 1일 될 때 까지 반복 된다.

- 재귀 호출이 한번 진행될 때마다 최소한 하나의 원소는 최종적으로 위치가 정해지므로, 이 알고리즘은 반드시 끝난다는 것을 보장할 수 있다.

![íµ ì ë ¬ì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://t1.daumcdn.net/cfile/tistory/221EE74E57D0478118)

`다음의 숫자들을 오름차순으로 정렬하는 프로그램을 작성하세요.`

`3 7 8 1 5 9 6 10 2 4`

```python
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    small = []
    big = []
    equal = []
    for value in array:
        if value < pivot:
            small.append(value)
        elif value > pivot:
            big.append(value)
        else:
            equal.append(value)

    return quick_sort(small) + equal + quick_sort(big)


print(quick_sort([3, 7, 8, 1, 5, 9, 6, 10, 2, 4]))
```

`result =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`



- **퀵 정렬의 평균 시간 복잡도는 O(N*logN) 이다.**
- **퀵 정렬의 최악 시간 복잡도는 O(N^2) 이다.**



위와 같이 이미 정렬이 되어 있는 경우 퀵 정렬의 시간 복잡도는 O(N^2)에 가깝다. 위의 경우 삽입 정렬을 사용할 경우 매우 빠르게 풀수 있다.

---

### 병합 정렬

- 일단 정확히 반으로 나누고 나중에 합친 후 정렬하는 알고리즘
- 분할 정복 알고리즘의 하나이다.
- 합병 정렬은 다음과 같이 작동한다.
  1. 리스트의 길이가 0 또는 1이면 이미 정렬 된것으로 본다. 
  2. 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
  3. 각 부분 리스틀르 재귀적으로 합병 정렬을 이용해 정렬한다.
  4. 두 부분 리스트를 다시 하나의 정렬된 리스트로 **합병** 한다.

![img](https://ka-perseus-images.s3.amazonaws.com/ace963383bea8d154f6abd1322a06a73b56b4628.png)

- 퀵 정렬과 다르게 피벗 값이 없고 항상 반으로 나눈다는 특징이 있다.
- **병합 정렬의 시간 복잡도 O(N * logN)을 보장하는 것 이다.**

`3, 5, 1, 2, 9, 6, 4, 5, 7`

```python
def merge_sorted(new_array):
    if len(new_array) > 1:
        mid = len(new_array) // 2
        left = new_array[:mid]
        right = new_array[mid:]
        new_left = merge_sorted(left)
        new_right = merge_sorted(right)
        return merge(new_left, new_right)
    else:
        return new_array


def merge(left, right):
    i = 0
    j = 0
    result = []

    while (i < len(left)) & (j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while (i < len(left)):
        result.append(left[i])
        i += 1

    while (j < len(right)):
        result.append(right[j])
        j += 1

    return result


array = [3, 5, 1, 2, 9, 6, 4, 5, 7]
print(merge_sorted(array))
```

`result = [1 2 3 4 5 6 7 8 9 10]`

## 코드 수정해서 추가하기

---

### 힙 정렬

- 병합 정렬과 퀵 정렬만큼 빠른 정렬 알고리즘 이다.
- 힙 정렬은 **힙 트리 구조를 이용하는 정렬 방법**이다.
- 힙을 이용해 데이터를 정렬하면 어떨까 ?



![ì´ì§í¸ë¦¬ì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://madplay.github.io/img/post/2018-04-30-binary-search-tree-1.jpg)

- 이진 트리: 모든 노드의 자식 노드가 2개 이하인 트리 구조

- **트리** 라는 것은 말 그대로 가지를 뻗어 나가는 것처럼 데이터가 서로 연결 되어 있다는 것이다.

![ìì ì´ì§í¸ë¦¬ì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://t1.daumcdn.net/cfile/tistory/23108B4156716F691E)

- **완전 이진트리는** 데이터가 루트 노드부터 시작해서 자식 노드가 왼쪽 자식 노드, 오른쪽 자식 노드로 차근차근 들어가는 구조의 이진 트리이다.
- 즉, 완전 이진 트리는 이진 트리의 노드가 중간에 비어있지 않고 뺵빽히 가득 찬 구조이다.

##### 힙은 최솟값이나 최댓값을 빠르게 찾아내기 위해 완전 이진 트리를 기반으로 하는 트리이다.

- 힙 정렬을 하기 위해서는 정해진 데이터를 힙 구조를 가지도록 만들어야 한다.

![í êµ¬ì¡°ì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](http://3.bp.blogspot.com/-QGbIGtOsknY/VYxNnlUiIoI/AAAAAAAACCc/a06lp5qTcGo/s1600/Heap_Concept.png)

##### 힙 정렬을 수행하기 위해서는 힙 생성 알고리즘(Heapify Algorithm)을 사용 한다.

![í ìì± ìê³ ë¦¬ì¦ì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](http://mblogthumb2.phinf.naver.net/MjAxODAzMTNfMTIz/MDAxNTIwOTI2NjUxNzY5.MniqPG6mA1ryADxjlEeV_pAlyeRO53yrs1-dBaiEWTUg.jTOzp4KyJODckaccHEw2f-UfmHW3Q2kufurvKvdckS8g.PNG.ndb796/image.png?type=w800)



- 힙 생성 알고리즘은 특정 한' 하나의 노드'에 대해서 수행하는 것이다.
- 하나의 노드를 제외하고는 최대 힙이 구성되어 있는 상태
- 위 트리에서 5만 최대 힙 정렬을 수행해주면 전체 트리가 최대 힙 구조로 형성되는 상태이다.

##### 특정한 노드의 두 자식 중에서 더 큰 자식과 자신의 위치를 바꾸는 알고리즘 이다.

위의 예시에서는 5의 두 작식인 7과 4중에서 더큰 자식인 7과 5의 위치를 바꾸어 주면된다.

![image-20190109161302641](/Users/eunyeob/Library/Application Support/typora-user-images/image-20190109161302641.png)

- **힙 생성 알고리즘의 시간 복잡도는 O(log N) 이다.**

`다음의 데이터를 오름차순 정렬하세요`

`7 6 5 8 3 5 9 1 6`

위 배열을 완전 이진 트리 형태로 출력하면 다음과 같다.

![image-20190109170633840](/Users/eunyeob/Library/Application Support/typora-user-images/image-20190109170633840.png)

- 모든 원소를 기준으로 힙 생성 알고리즘을 적용하여 전체 트리를 힙 구조로 만들어 주어야 한다.

![image-20190110145903990](/Users/eunyeob/Library/Application Support/typora-user-images/image-20190110145903990.png)

- 그래서 결과적으로 위와 같이 최대 힙이 구성된다. 이제부터 루트에 있는 값을 가장 뒤쪽으로 보내면서 힙 트리의 크기를 1씩 빼주면 된다.



![image-20190110150043654](/Users/eunyeob/Library/Application Support/typora-user-images/image-20190110150043654.png)

- 즉 위와 같이 9와 6을 바꾼 뒤에는 9는 정렬이 완련된 것이므로 빨간색으로 처리합니다. 이제 9를 제외하고 나미저 8개 원소를 기준으로 또 힙 생성 알고리즘을 수행한다. 결과는 다음과 같다.

![image-20190110150232296](/Users/eunyeob/Library/Application Support/typora-user-images/image-20190110150232296.png)

- 이제 다시 가장 큰 숫자인 8이 루트에 존재한다. 이것을 가장 뒤 쪽의 원소와 서로 바꿉니다.



![image-20190110150448935](/Users/eunyeob/Library/Application Support/typora-user-images/image-20190110150448935.png)

- 그럼 위와 같이 8과 9가 가장 뒤에 배열되어 정렬이 이루어졌다. 이제 이 과정을 반복하면된다
- **힙 정렬의 전체 시간 복잡도는 O(N * logN)이다.**



```
import heapq as hq
import random


def heap_sort():
    heapify = []
    for _ in range(10):
        num = random.randint(1, 11)
        hq.heappush(heapify, num)
        print(num)

    print(heapify)


heap_sort()
```

`result1 = [2, 3, 3, 4, 7, 11, 10, 11, 7, 9] `

`result2 = [2, 2, 7, 7, 3, 10, 10, 11, 8, 11]`

`result3 = [1, 2, 3, 3, 2, 7, 4, 9, 6, 7]`



- 위 코드는 파이썬의 모듈인 **heapq 와 random** 을 사용하였다. 리스트 값을 랜덤 값으로 받아오고 그 값을 차례대로 넣으면서 힙 정렬을 실행하였다.

---

### 계수 정렬

- 현재 까지 공부한 선택 정렬, 버블 정렬, 삽입 정렬, 퀵 정렬, 병합 정렬, 힙 정렬 중 가장빠른 알고리즘은 어떤것일까? 아마 속도가 O(N * log N)이 나오는 퀵 정렬, 병합 정렬, 힙 정렬, 중 하나 일 것이다. 하지만 이것보다 더욱 빠르게 정렬을 해야한다면 어떻게 해야 될까 ?



`다음의 5이하 자연수 데이터들을 오름차순 정렬하세요`

`1 3 2 4 3 2 5 3 1 2 3 4 4 3 5 1 2 3 5 2 3 1 4 3 5 1 2 1 1 1`

이번 예시의 데이터는 총 30개이다. 위 예시들을 보면 모든 숫자가 1~5사이의 숫자들이다. 이처럼 '**범위 조건**'이 있는 경우에 한해서 굉장히 빠른 알고리즘이 있다.

- 계수 정렬(Counting Sort)은 단순하게 '**크기를 기준으로**' 세는 알고리즘이다.

- **계수 정렬의 시간 복잡도는 O(N) 이다.**



지금 까지는 모든 데이터를 그 자체로 위치를 바꾸어 가면서 정렬하는 알고리즘에 대해서 공부를 했다. 이번에 다룰 계수 정렬은 '크기를 기준'으로 갯수만 세주면 되기 때문에 위치를 바꿀 필요가 없다. 또한 모든 데이터에 한 번씩만 접근하면 된다는 점에서 무척이나 효율적인 방법이다.



![image-20190110205341978](/Users/eunyeob/Library/Application Support/typora-user-images/image-20190110205341978.png)

![image-20190110205430842](/Users/eunyeob/Library/Application Support/typora-user-images/image-20190110205430842.png)

![image-20190110205504568](/Users/eunyeob/Library/Application Support/typora-user-images/image-20190110205504568.png)

위와 같이 해당 크기의 원소를 만나는 경우 숫자를 1씩 더해가면 된다. 위와 같은 방식을 반복하면 결과적으로 다음과 같이 된다.

![image-20190110205527481](/Users/eunyeob/Library/Application Support/typora-user-images/image-20190110205527481.png)

출력 결과는 다음과 같이 나온다.

`1 1 1 1 1 1 1 1 2 2 2 2 2 2 3 3 3 3 3 3 3 3 4 4 4 4 5 5 5 5 `

