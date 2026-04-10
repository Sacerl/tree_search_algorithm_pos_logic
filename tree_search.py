from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)



def bfs(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.value)

        for child in node.children:
            queue.append(child)

    return result




def dfs(node, result=[]):
    if node is None:
        return result
 
    result.append(node.value)
 
    for child in node.children:
        dfs(child, result)
 
    return result



def build_example_tree():
    root = Node("A")
    b, c, d = Node("B"), Node("C"), Node("D")
    e, f, g = Node("E"), Node("F"), Node("G")

    root.add_child(b)
    root.add_child(c)
    root.add_child(d)
    b.add_child(e)
    b.add_child(f)
    d.add_child(g)

    return root




if __name__ == "__main__":
    tree = build_example_tree()

    print("── BFS (Breitensuche) ──")
    print(f"  Reihenfolge: {bfs(tree)}\n")

    print("── DFS (Tiefensuche) ──")
    print(f"  Reihenfolge: {dfs(tree)}\n")
