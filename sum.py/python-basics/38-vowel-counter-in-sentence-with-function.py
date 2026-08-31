def vowel_counter(sentence):
    count = 0

    for char in sentence.lower():
        if char in "aeiou":
            count += 1

    return count


sentence = input("Enter a sentence: ")
print("Number of vowels:", vowel_counter(sentence))