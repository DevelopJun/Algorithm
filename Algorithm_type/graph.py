# 그래프 이론
# DFS, BFS 와 9장 최단 경로에서 다룬 내용은 모두 그래프 알고리즘의 한 유형으로 볼 수 있다.
# 크루스칼 알고리즘은 그리디 알고리즘으로 분류되며, 위상 정렬 알고리즘은 앞서 배운 큐 자료구조 혹은 스택 자료구조를
# 활용해야 구현할 수 있다.
# ' 여러 개의 도시가 연결되어 있다.' 는 무조건 그래프 알고리즘임.

# 트리 자료구조는 다양한 알고리즘에서 사용되므로 꼭 기억해야함,

# 인접행렬(Adjaacency Matrix) : 2차원 배열을 사용하는 방식
# 인접 리스트(Adjacency List) : 리스트를 사용하는 방식

# 서로소 집합 Disjoint Sets
# 서로소 집합 자료구조는 union-find * 합치기 찾기 /  자료구조라고 불리기도 한다.
# 연산의 이름 자체가 합치기와 찾기이기도 하고, 두 집합이 서로소 관계인지를 확인할 수 있다는 말은 각 집합이
# 어떤 원소를 공통으로 가지고 있는지를  확인할 수 있다는 말과 같기 때문임.

# 특정 원소가 속한 집합을 찾기

def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때 까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합 :', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블:', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
