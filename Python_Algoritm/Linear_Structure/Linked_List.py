# 파이썬으로 링크드 리스트
# 자료구조에서 가장 중요한 개념 중 하나임.
# 입력을 어떻게 받을 것인가?

# https://wayhome25.github.io/cs/2017/04/17/cs-19/
# LinkedList Class 정의

# Node 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# LinkedList 클래스(자료구조) 정의


# Node 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList 클래스 (자료구조) 정의
class LinkedList:
    # 초기화 메소드
    def __init__(self):
        dummy = Node("dummy")
        # 제일 앞 머리
        self.head = dummy
        # 뒤에 부터 순서대로
        self.tail = dummy
        self.current = None
        self.before = None

        self.num_of_data = 0

    # append 메소드 (insert - 맨 뒤에 노드 추가, tail과 node의 next, 데이터 개수 변경)
    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

        self.num_of_data += 1

    # delete 메소드 (delete - current 노드 삭제, 인접 노드의 current, next 변경, 데이터 개수 변경)
    def delete(self):
        pop_data = self.current.data

        if self.current is self.tail:
            self.tail = self.before

        self.before.next = self.current.next
        self.current = self.before  # 중요 : current가 next가 아닌 before로 변경된다.
        #

        self.num_of_data -= 1

        return pop_data

    # first 메소드 (search1 - 맨 앞의 노드 검색, before, current 변경)
    def first(self):
        if self.num_of_data == 0:  # 데이터가 없는 경우 첫번째 노드도 없기 때문에 None 리턴
            return None

        self.before = self.head
        self.current = self.head.next

        return self.current.data

    # next 메소드 (search2 - current 노드의 다음 노드 검색, 이전에 first 메소드가 한번은 실행되어야 함)
    def next(self):
        if self.current.next == None:
            return None

        self.before = self.current
        self.current = self.current.next

        return self.current.data

    def size(self):
        return self.num_of_data


# 파이썬은 그냥 self를 전해주는 것 같음. 클래스 메소드 함수에 self를 써주는게
# 클래스의 메소드들은 self를 첫번 째 인자로 받도록 해주어야 한다. Python이 자동으로 self를 전달하기 때문이다.


l_list = LinkedList()
print(l_list.first())
l_list.append(5)
print(l_list.first())


# 수학이 안들어가서, 국립대
# 미대를 본다고 해도, 성적이 안되니까,

# 86 + 60 => 150
