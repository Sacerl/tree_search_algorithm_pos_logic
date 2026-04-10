from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


# ─────────────────────────────────────────
#  BFS – Breitensuche (ohne target)
# ─────────────────────────────────────────
def bfs(root):
    """Besucht alle Knoten ebenenweise und gibt sie als Liste zurück."""
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


# ─────────────────────────────────────────
#  DFS – Tiefensuche (ohne target)
# ─────────────────────────────────────────
def dfs(root):
    """Besucht alle Knoten in die Tiefe und gibt sie als Liste zurück."""
    if root is None:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.value)

        for child in reversed(node.children):
            stack.append(child)

    return result


# ─────────────────────────────────────────
#  Beispielbaum aufbauen
# ─────────────────────────────────────────
#
#          A
#        / | \
#       B  C  D
#      / \    |
#     E   F   G
#
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


# ─────────────────────────────────────────
#  Demo
# ─────────────────────────────────────────
if __name__ == "__main__":
    tree = build_example_tree()

    print("── BFS (Breitensuche) ──")
    print(f"  Reihenfolge: {bfs(tree)}\n")

    print("── DFS (Tiefensuche) ──")
    print(f"  Reihenfolge: {dfs(tree)}\n")
