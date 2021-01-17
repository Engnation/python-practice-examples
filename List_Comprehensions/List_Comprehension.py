#Examples are originally from SOLOLEARN:

#List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule.

#Note: Python list comprehensions are inspired by set-builder notation in mathematics.

#This is a basic example of a list comprehension that creates a list of cubed numbers up to 64:
cubes = [i**3 for i in range(5)]

print('cubes: ',cubes)

#A list comprehension can also contain an if statement to enforce a condition on values in the list.

evens=[i**2 for i in range(10) if i**2 % 2 == 0]

print('evens: ',evens)