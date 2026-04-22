sentence = input("Enter sentence: ")

lookup = {
    "good": "excellent",
    "bad": "poor",
    "happy": "joyful"
}

words = sentence.split()

updated = []

for word in words:
    updated.append(lookup.get(word, word))

print("Updated Sentence:")
print(" ".join(updated))
