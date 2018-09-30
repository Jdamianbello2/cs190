b = False

while b == False:
    stack = input("Enter a long string of continuous text with or without the word 'needle' in it.")
    if "needle" in stack:
        print("found it")
        b = True
    else:
        print("No heroine found :(")
