# using Dictionary
def print_duplicates(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char, count in char_count.items():
        if count > 1:
            print(f"Character '{char}' occurs {count} times")

s = "hello world"
print_duplicates(s)
# time complexity O(n)
# space complexity O(n)
















# using collection of modules
import collections

def printduplicates(s):
    char_count = collections.Counter(s)
    for char, count in char_count.items():
        if count > 1:
            print(f"Character '{char}' occurs {count} times")

s = "hello world"
printduplicates(s)
# time complexity O(n)
# space complexity O(n)
















#using list
def prin_duplicates(s):
    char_count = [char for char in set(s) if s.count(char) > 1]
    for char in char_count:
        print(f"Character '{char}' occurs {s.count(char)} times")

s = "hello world"
prin_duplicates(s)
# time complexity O(n)
# space complexity O(n)








# using dictonary comprehension
def print_duplicate(s):
    char_count = {char: s.count(char) for char in set(s) if s.count(char) > 1}
    for char, count in char_count.items():
        print(f"Character '{char}' occurs {count} times")

s = "hello world"
print_duplicate(s)
# time complexity O(n)
# space complexity O(n)