import random

names = ["Joe", "Bob", "Ron", "Ali"]
print("Let Joe, Bob and Ron Brawl!")

number = random.randint(1, len(names))

print(f"{names[number - 1]} won the brawl!")
