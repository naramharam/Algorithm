## 스택(Stack)

#### 스택은 택배 상하차를 생각하면 되고 큐는 은행 창구를 생각하면 된다.



![ì¤íì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Data_stack.svg/300px-Data_stack.svg.png)

- 스택은 한 쪽 끝에서만 자료를 넣거나 뺄 수 있는 **선형구조(LIFO - Last In First Out)** 으로 되어 있다.
- 자료를 넣는 것을 **푸시(push)** 라고 하고 반대로 넣어둔 자료를 꺼내는 것을 **팝(pop)** 이라고 한다.
- 이때 꺼내지는 자료는 가장 최근에 보관한 자료부터 나오게 된다. 이를 LIFO 구조라고 한다.



```python
def stack():
    stack = []
    for i in range(0, 7):
        stack.append(i)
    print(stack)

    while stack:
       print("POP->", stack.pop())


stack()
```

`[0, 1, 2, 3, 4, 5, 6]
POP-> 6
POP-> 5
POP-> 4
POP-> 3
POP-> 2
POP-> 1
POP-> 0`

#### 파이썬에서는 append() 와 pop() 을 사용하면 아주 간단하게 스택을 구현 할 수 있다.

---

## 큐(Queue)

- 먼저 집어 넣은 데이터가 먼저 나오는 **FIFO(First In First Out)** 구조로 저장하는 형식을 말한다.
- 먼저 줄을 선 사람이 먼저 나갈 수 있는 상황을 연상하면 된다.

![views](https://wayhome25.github.io/assets/post-img/cs/queue1.jpg)

![views](https://wayhome25.github.io/assets/post-img/cs/queue2.jpg)



##### 입력 동작은 Enqueue, 출력 동작은 Dequeue 라고 한다.

```python
class Queue(list):
    enqueue = list.append

    def dequeue(self):
        return self.pop(0)

    def is_empty(self):
        if not self:
            return True
        else:
            return False

    def peek(self):
        return self[0]


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    while not q.is_empty():
        print(q.dequeue(), end= ' ') 
```





