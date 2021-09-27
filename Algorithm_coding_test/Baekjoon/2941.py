'''
크로아티아 알파벳
'''
import re
text = str(input())

finds = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

result = 0


for x in range(len(finds)):
    text = text.replace(finds[x], "a")

listtext = list(text)
print(listtext)
print(len(listtext))
print(len(text))
# change1 = re.sub(r'[^\w]', '', string)
# change = [word for word in re.sub(r'[^\w]', '', string)]

# print(change)
# result = []
# print(result)
