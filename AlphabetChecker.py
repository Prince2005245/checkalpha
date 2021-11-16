def script():
    print("Whats up, its tyrones alphabet checker")
    character = input("Please enter in a single character: ")
    if((character >= "a" and character <= "z") or (character >= "A" and character <= "Z")):
        print(character, "is in the Alphabet")
    else:
        print(character, "is not in the Alphabet")
if __name__ == "__main__":
    script()
