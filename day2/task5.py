# Capitalize the first letter of every word in a sentence.
def capitalize_sentence(sentence: str) -> str:
    return " ".join(word.capitalize() for word in sentence.split(" "))

print(capitalize_sentence("hello world from 100 days of coding"))
