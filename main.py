#Notes app by @rafaelborri

def main():
    while True:
        operation = input("Reade = r\nWrite = w\nEnd = e\n").lower()
        if operation == "r":
            nameinput = input("What is the name of the note\n")
            name = nameinput + ".txt"
            note = open(name, "r")
            print(note.read())
        elif operation == "w":
            nameinput = input("Name of the note you want to create\n")
            name = nameinput + ".txt"
            note = open(name, "w")
            data_for_note = input()
            note.write(data_for_note)
        elif operation == "e":
            exit()
        else:
            print("Mistake, you havent select a good note probably because you are stupid or you can't read.")

if __name__ == "__main__":
    main()