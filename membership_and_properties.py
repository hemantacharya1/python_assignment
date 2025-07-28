fruits_list = ["apple", "banana", "orange", "apple", "grape"]
fruits_tuple = ("apple", "banana", "orange")
fruits_set = {"apple", "banana", "orange", "grape"}
fruits_dict = {"apple": 5, "banana": 3, "orange": 8, "grape": 2}

def check(list):
    print("apple" in list)

def find_length(list):
    print(f"length of data structure is {len(list)}")

def print_element(list):
    for i in list:
        print(i)

check(fruits_list)
check(fruits_tuple)
check(fruits_set)
check(fruits_dict)
find_length(fruits_list)
find_length(fruits_tuple)
find_length(fruits_set)
find_length(fruits_dict)
print_element(fruits_dict)




# 🔢 1. List
# Time Complexity: O(n)

# Why: A list performs a linear search (checks each element one by one).

# Use Case: Fine for small collections, but slow for large ones.

# 🟣 2. Set
# Time Complexity: O(1) on average

# Why: Sets are implemented using hash tables, which allow constant-time lookups.

# Best for: Fast membership tests, e.g., checking if an item exists in a large collection.

# 🟩 3. Dict
# Time Complexity: O(1) on average (for keys)

# Why: Also uses a hash table internally, optimized for key lookup.

# Note: value in dict checks only keys, not values.

# Best for: Fast key presence checks.

# 🔷 4. Tuple
# Time Complexity: O(n)

# Why: Like lists, tuples are sequential containers, so it does a linear scan.

# Use Case: Use only if immutability is required and the size is small.