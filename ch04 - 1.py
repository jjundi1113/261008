# Node 클래스 정의
class Node:
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end=' ')
    while current.link is not None: # is not None > != None
        current = current.link
        print(current.data, end=' ')
    print(current.data)

# 노드 생성. 첫 번째 노드라서 link는 None으로 설정
node1 = Node()
node1.data = "다현"

node2 = Node()
node2.data = "정연"
node1.link = node2

node3 = Node()
node3.data = "쯔위"
node2.link = node3

node4 = Node()