def my_map(func, iterable):
    return [func(item) for item in iterable]

result = my_map(lambda x: x * x, [1, 2, 3, 4])
print(result)