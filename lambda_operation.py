squre = lambda x: x*x
print(squre(5))

import math

# reverse string
reverse = lambda s:s[::-1]
print(reverse("Hello world"))

# convert to upper case
to_upper = lambda s: s.upper()
print(to_upper("misogi ai"))

# filter even number
filter_evens = lambda lst: list(filter(lambda x:x%2==0,lst))
print(filter_evens([1, 2, 3, 4, 5, 6]))

# sum
sum_list = lambda lst: sum(lst)
print(sum_list([1, 2, 3, 4]))