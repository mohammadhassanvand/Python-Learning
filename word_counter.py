def count_words(text):
    return len(text.split())

sentence = input("Enter a sentence: ")
print("Word count:", count_words(sentence))
