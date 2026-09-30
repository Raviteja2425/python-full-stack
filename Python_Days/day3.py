num = 90
num_2 = 9
print(num + num_2)
print(num - num_2)
print(num * num_2)
print(num / num_2)
print(num // num_2)
print(num % num_2)

n = 9
n += 24
print(n)
n = 9
n -= 24
print(n)
n = 9
n *= 24
print(n)
n = 25
n /= 5
print(n)
n = 268.5
n //= 5
print(n)

a = 24
b = 25
print(a == b)
print(a != b)
print(a < b)
print(a > b)

a = [1, 2]
b = [1, 2]
print(a is b)
print(a is not b)

text = 'python is language'
print('y' in text)
print('i' not in text)

print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(5 >> 2)
print(5 << 1)

name = 'vamsi'
age = 22
print('my name is', name, 'age is', age)
print('hello!', name)
print(f'my name is {name} and i am {age} years old')
print('my name is %s and i am %d years old' % (name, age))

a = int(input('Enter an integer: '))
b = float(input('Enter any decimal: '))
print(b + 7)
value = input('Enter a string: ')
print(type(value))
nums = list(map(int, input('Enter some numbers: ').split()))
print(nums)
values = tuple(map(int, input('Enter some numbers: ').split()))
print(values)
