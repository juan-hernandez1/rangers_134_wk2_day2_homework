# Exercise 1
# Using the given list, print out a filtered version of the list with only the numbers 
# that are less than ten

alist = [1,11,14,5,8,9]
filtered_list = [x for x in alist if x < 10]

for number in filtered_list:
    print(number)

# Exercise 2
# Merge and sort the two lists below
# Hint: You can use the .sort() method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

merged_list = l_1 + l_2
merged_list.sort()

print(merged_list)

# Exercise 3
# Square every number from 1 to 15
# include 15

squared_numbers = [x ** 2 for x in range(1, 16)]

for number in squared_numbers:
    print(number)

# Exercise 4
# Using List Comprehension and the given list, print out a filtered list with only the names # that start with the letter 'a'. The names in the outputted list should be title cased and # have no whitespace.

names_list = ['   amy', 'Briant', 'Ryan ', ' Alex', 'steve', '  ']
list_comp = [name.strip().title() for name in names_list if len(name.strip())> 0 and name.strip().lower()[0] == "a" ]
list_comp

# Exercise 5
# Print all Prime numbers from 1 to 100


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    x = 5
    while x * x <= number:
        if number % x == 0 or number % (x + 2) == 0:
            return False
        x += 6
    return True


for num in range(1, 101):
    if is_prime(num):
        print(num)
