from functools import reduce

# IIFE (immediately invoked function expression)
number = 1
(lambda number: print(number * 200))(number)


# filter
array = [1, 3, 5, 7, 9, 11]
result1 = filter(lambda element: element > 7, array)
print(list(result1))


# map
result2 = map(lambda element: element * 20, array)
print(list(result2))


# reduce
result3 = reduce(lambda a, b: a + b, array)
print(result3)


# sorted
books = [('JavaScript', 650), ('Python', 600), ('C++', 950)]
result4 = sorted(books, key=lambda book: book[1])
print(result4)
