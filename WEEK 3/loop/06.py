vowels="aeiou"
word="python"
count=0

for char in word:
    if char in vowels:
        count += 1

print(f'Number of vowels in {word} is {count}   ')

# Output: Number of vowels in python is 1