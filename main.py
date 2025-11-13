print("Character Occurence")

word = input("Enter a word: ")
char = input("Enter a character to check: ")

count = 0

for i in range(len(word)):
    for j in range(i, i+1):
        if word[j] == char:
            count += 1

print(f"The character '{char}' is repeated {count} times in the word '{word}'.")

