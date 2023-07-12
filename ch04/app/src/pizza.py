# TRY IT YOURSELF 4 - 1

pizzas = ['cheese', 'pepperoni', 'supreme']

for pizza in pizzas:
    print(f"I like {pizza} pizza.\n")
print("I like pizza!")

# TRY IT YOURSELF 4-11
friends_pizzas = pizzas

pizzas.append('white')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

friends_pizzas.append('sausage')
print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)
