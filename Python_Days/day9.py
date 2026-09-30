def add_(a, b):
    print(a + b)

add_(5, 6)

num = 0
num_1 = 1
print(num, num_1, end=' ')
for _ in range(1, 10):
    num_2 = num + num_1
    num = num_1
    num_1 = num_2
    print(num_2, end=' ')
print()

def combine_lists(first, second):
    print(first + second)

combine_lists([1, 3], [5, 6])

def data_(a=8, b=9):
    print(a + b)

data_(1, 5)

def prime(limit):
    for number in range(2, limit + 1):
        count = 0
        for divisor in range(1, number + 1):
            if number % divisor == 0:
                count += 1
        if count == 2:
            print(f'{number} is prime')

prime(int(input('Enter a number: ')))

def details(age, name, batch, location):
    print(name)
    print(age)
    print(batch)
    print(location)

details(name='teja', age=45, location='vizag', batch=6)

def all_(*name):
    print(name)

all_('teja', '45', 'vizag', '6')

def student_details(**data_):
    print(data_.keys())

student_details(name='teja', age=45, location='vizag', batch=6)

def multiply(a, b):
    return a * b

print(multiply(4, 5))
