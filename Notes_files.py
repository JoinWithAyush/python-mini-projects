
NOTES_FILES = "notes.txt"

def add_notes():
    note = input("Enter your notes: ")
    with open(NOTES_FILES, "a") as file:
        file.write(note + "\n")
    print("Notes added successsfully!\n")    

#View all notes

def view_notes():
    try:
        with open(NOTES_FILES, "r") as files:
            notes = files.readlines()
            if not notes:
                print("No notes found.\n")
                return
            print("\nYour Notes: ")
            for index, note in enumerate(notes,start=1):
               print(f"{index}. {note.strip()}")

               print()

    except FileNotFoundError:
        print("No notes file found yet.\n")

#Search for a notes
def search_notes():
    keyword = input("Enter a ley word to search: ").lower()
    try:
        with open(NOTES_FILES, "r") as file:
            notes = file.readlines()

            found = False
            for index, note in enumerate(notes, start=1):
                if keyword in note.lower():
                    print(f"{index}. {note.strip()}")
                    found = True
            if not found:
                print("No matching notes found.")

                print()

    except FileNotFoundError:
        print("No notes file found yet.\n")

#Delete a note
def delete_note():
    try:
        with open(NOTES_FILES, "r") as file:
            notes = file.readlines()
        
        if not notes:
            print("No notes avaliable to delete.\n")
            return
        
        print("\nYour Notes:")

        for index, note in enumerate(notes, start=1):
            print(f"{index}. {note.strip()}")

        note_number = int(input("Enter note number ot delete: "))

        if 1 <= note_number <= len(notes):
            removed_note = notes.pop(note_number -1)

            with open(NOTES_FILES, "w") as file:
                file.writelines(notes)

            print(f"Deleted note: {removed_note.strip()}\n")
        else:
            print("Invalid note number.\n")

    except FileNotFoundError:
        print("No notes file found yet.\n")
    
def main():
    while True:
        print("1. Add Notes")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Delete Notes")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_notes()

        elif choice == "2":
            view_notes()

        elif choice == "3":
            search_notes()

        elif choice == "4":
            delete_note()

        elif choice == "5":
            print("GoodBye!")
            break

        else:
            print("Invalid choice.\n")

main()            