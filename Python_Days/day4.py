text = 'python is a programming language'
print(len(text))
print(text[12:23])
print(text[12:])
print(text[:23])
print(text[::-2])
print(text.upper())
print(text.lower())
print(text.index('l'))
print(text.replace('python', 'java'))
print(text.split(' '))
print(text.count('p'))

txt = 'madam'
print(txt[::-1])

items = [1, 2, 3, 4, 'python']
print(items[-1][5])
all_ = [12, [1, 'python', [1, 4], (78, [6, 7])], ['java', 78]]
print(all_[1][3][1])
data = ['python', [1, 2, (90, 'details', [67, 0]), (78, 'student')]]
print(data[1][2][1][2])
print(len(data))

data = [1, 2, 3, 4, 5, 6, 7]
print(data[2:6])
a = [1, 2]
b = [3, 4]
print(a + b)

go = [1, 2]
print(go)
go.append(4)
print(go)

a = [1, 2]
a.extend('python')
print(a)

a = [1, 2, 3]
a.pop(2)
print(a)
a.remove(2)
print(a)
