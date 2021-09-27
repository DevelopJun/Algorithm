# 정렬되어 있는 두 연결 리스트를 합쳐라
# 1-> 2-> 4, 1 -> 3 -> 4

def mergeTwoList(lista, listb: list[int]) -> list[int]:
    print(lista)
    print(listb)

    finallist = lista + listb
    finallist.sort()
    print(finallist)
    pass


lista = list(map(int, input().split()))
listb = list(map(int, input().split()))
mergeTwoList(lista, listb)
