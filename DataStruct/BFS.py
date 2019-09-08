class Node:
    def __init__(self, data):
        self.data = data
        self.childs = []


def bfs(A):
    q = []
    visited = set()

    while q:
        node = q.pop(0)
        if node in visited:
            continue
        print(node.data)
        q.extend(node.childs)
