import random

words = input()

#split string into a list of individual words
split = words.split(" ")

#shuffle list
random.shuffle(split)

#put together into a string
shuffled = " ".join(split)
print(shuffled)