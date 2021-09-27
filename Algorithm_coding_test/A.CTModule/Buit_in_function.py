sum()
min()
max()
eval()

data = sorted([5, 6, 9, 0, 3])
print(data)

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
result = sorted(student_tuples, key=lambda student: student[2], reverse=True)
print(result)

data = [["고구마", 25000], ["바나나", 123232], [
    "파인애플", 4500], ["감자", 3000], ["금귤", 6000]]
data.sort(key=lambda x: x[1])
print(data)
