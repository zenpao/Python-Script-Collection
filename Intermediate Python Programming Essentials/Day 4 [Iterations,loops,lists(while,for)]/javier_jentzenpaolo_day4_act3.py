wordBank = []

while True:
    word = str(input("\nEnter a word: "))
    wordBank.append(word)
    response = str(input("Do you want to try again? Y (yes) or N (no):")).upper()
    if response == 'Y':
        continue
    elif response == 'N':
        print("\nTotal Number of Words:", len(wordBank))
        print("Word Bank:", *wordBank)
        break

