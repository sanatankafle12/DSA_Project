import sys
from collections import deque
 
class Node:
    def __init__(self, x, y, dist=0):
        self.x = x
        self.y = y
        self.dist = dist

    def __hash__(self):
        return hash((self.x, self.y, self.dist))
 
    def __eq__(self, other):
        return (self.x, self.y, self.dist) == (other.x, other.y, other.dist)
 
 
row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]
 
 
def isValid(x, y, N):
    return not (x < 0 or y < 0 or x >= N or y >= N)
 

def findShortestDistance(src, dest, N):
 
    visited = set()
    q = deque()
    q.append(src)
    while q:
        node = q.popleft()
 
        x = node.x
        y = node.y
        dist = node.dist
        if x == dest.x and y == dest.y:
            return dist
 
        if node not in visited:
            visited.add(node)
            for i in range(len(row)):
                x1 = x + row[i]
                y1 = y + col[i]
 
                if isValid(x1, y1, N):
                    q.append(Node(x1, y1, dist + 1))
    

if __name__ == '__main__':
 
    N = 8                
    src = Node(0, 7)    
    dest = Node(7, 0)   
    print("The minimum number of steps required is",
          findShortestDistance(src, dest, N))