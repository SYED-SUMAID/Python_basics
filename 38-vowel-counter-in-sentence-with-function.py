def count_vowels(sentence):
    count = 0

    for char in sentence:
        if char.lower() in "aeiou":
            count += 1

    return count


sentence = input("Enter a sentence: ")

result = count_vowels(sentence)

print("Number of vowels:", result)
