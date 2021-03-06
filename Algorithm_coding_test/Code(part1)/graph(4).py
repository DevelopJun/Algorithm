# 팀 결성(준호 개인 코딩)
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


result = []

n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

for i in range(m):
    identify, a, b = map(int, input().split())
    if identify == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            result.append(1)
        else:
            result.append(2)

for i in result:
    if i == 1:
        print("Yes")
    else:
        print("NO")
