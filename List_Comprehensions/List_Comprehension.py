#List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule.

#Note: Python list comprehensions are inspired by set-builder notation in mathematics.

#This is a basic example of a list comprehension that creates a list of cubed numbers up to 64:
cubes = [i**3 for i in range(5)]

print(cubes)

