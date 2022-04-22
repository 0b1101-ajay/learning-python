import random


words = ['father', 'enterprise', 'science', 'programming', 'resistance', 'fiction', 'condition', 'reverse', 'computer', 'python']
word = random.choice(words)

jumble = ''.join(random.sample(word, len(word)))

print(f"The jumbled word is {jumble}")

guess = input("Write your guess: ")

if guess == word:
    print("Correct")
else:
    print(f"Incorrect: The word is {word}")