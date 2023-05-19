def reverseWords(words):
    reverseTheWords = words[::-1].upper()
    stringCount = len(reverseTheWords)
    print(f"OUTPUT: {reverseTheWords} ({stringCount} characters)")


words = str(input("INPUT: "))

reverseWords(words)