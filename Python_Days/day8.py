limit_ = int(input('Enter a number: '))
for i in range(2, limit_ + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(f'{i} is prime')

word = 'python'
reversed_word = ''
for letter in word:
    reversed_word = letter + reversed_word
    print(reversed_word)

word = 'madam'
reversed_word = ''
for letter in word:
    reversed_word = letter + reversed_word
if reversed_word == word:
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')

num = int(input('Enter a number: '))
length = len(str(num))
armstrong_total = 0
for digit in str(num):
    armstrong_total += int(digit) ** length
if armstrong_total == num:
    print(f'{num} is an Armstrong number')
else:
    print(f'{num} is not an Armstrong number')

n = int(input('Enter a number: '))
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i
if total == n:
    print(f'{n} is a perfect number')
else:
    print(f'{n} is not a perfect number')
