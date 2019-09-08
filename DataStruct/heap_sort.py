import heapq as hq
import random


def heap_sort():
    heapify = []
    for _ in range(10):
        num = random.randint(1, 11)
        hq.heappush(heapify, num)

    print(heapify)


heap_sort()

