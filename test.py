from collections import deque

priorities = [1, 1, 9, 1, 1, 1]
d = deque([(v, i) for i, v in enumerate(priorities)])
print(d)
