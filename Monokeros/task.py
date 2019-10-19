class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

def insert_value(current_node, new_value, depth):
    if new_value <= current_node.value:
        if current_node.left:
            insert_value(current_node.left, new_value, depth + 1)
        else:
            depth += 1
            print(depth)
            current_node.left = Node(new_value)
        
    else:
        if current_node.right:
            insert_value(current_node.right, new_value, depth + 1)
        else:
            depth += 1
            print(depth)
            current_node.right = Node(new_value)
       

n = int(input())
nodes = list(map(int, input().split()))
root = Node(nodes[0])

print(1)
for node in nodes[1:]:
    insert_value(root, node, 1)

    