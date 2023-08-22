#Write a Python program to count the number 4 in a given list.

numbers = [int(x) for x in input().split()]
print(f"number 4 is counted {numbers.count(4)} times")
