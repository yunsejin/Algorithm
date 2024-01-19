N = int(input())
tree = dict()

for i in range(N):
    root, left, right = input().split()
    tree[root] = (left, right)
    
def preorder(v):
    result = []
    if v != '.':
        result.append(v)
        result.extend(preorder(tree[v][0]))
        result.extend(preorder(tree[v][1]))
    return result

def inorder(v):
    result = []
    if v != '.':
        result.extend(inorder(tree[v][0]))
        result.append(v)
        result.extend(inorder(tree[v][1]))
    return result

def postorder(v):
    result = []
    if v != '.':
        result.extend(postorder(tree[v][0]))
        result.extend(postorder(tree[v][1]))
        result.append(v)
    return result

print("".join(preorder('A')))
print("".join(inorder('A')))
print("".join(postorder('A')))