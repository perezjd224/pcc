# TRY IT YOUR 4 - 3
for x in range(1,21):
    print(x)


# TRY IT YOUR 4 - 4
numbers = []

for number in range(1, 1000001):
    numbers.append(number)

print(numbers)

# TRY IT YOUR 4 - 5
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# TRY IT YOUR 4 - 6
numbers = []

for number in range(1, 20, 2):
    numbers.append(number)

print(numbers)

# TRY IT YOUR 4 - 7
numbers = []

for number in range(1, 30, 3):
    numbers.append(number)

print(numbers)

# TRY IT YOUR 4 - 8, 4-9
cubes = [value**3 for value in range(1, 11)]
  
print(cubes) 