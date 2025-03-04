print("Welcome to the Library Management System")

#Created a basic dictionary to store data.
lib = {1 : "Harry Potter.",
       2 : "Life of Pi.",
       3 : "Rich Dad Poor Dad.",
       4 : "Basics of Finance.",
       5 : "The complete Reference of C",
       6 : "The Laws of Human Nature."} 

#Function to create/add books.
def create() :
    key = int(input("Enter the ISBN number of the book: "))
    if(key not in lib) :
        lib[key] = input("Enter the title of the book: ")
        print("Book added successfully.\n")
    
    else :
        print("Key already Present.")
        choice = input("Whether you want to update the title(Y/N): ")
        if (choice == 'Y' or choice == 'y') :
            update()


#Function to read a book title.
def read() :
    key = int(input("Enter the ISBN of the book to read: "))
    if (key in lib) :
        print(lib[key])
        print()
    else :
        print("Given ISBN number is not present.\n")


#Function to update a book to given ISBN number.
def update() :
    key = int(input("Enter the ISBN number of the book: "))
    if(key in lib) :
        lib[key] = input("Enter the title of the book: ")
        print("Book updated successfully.\n")
    
    else :
        print("Key not Present.")
        choice = input("Whether you want to update the title(Y/N): ")
        if (choice == 'Y' or choice == 'y') :
            create()

#Function to delete a book title.
def delete() :
    if key in lib :
        key = int(input("Enter the ISBN number of the book to be deleted: "))
        del lib[key]
        print("Book Sucessfully deleted.\n")
    else :
        print("Key does not exist.")


#Main Menu
def main() :
    while True:
        print("1) Add/Create the book.\n2) To read a book.\n3) To Update a book.\n4) To Delete the title of the book.\n5) To Exit.")
        ch = int(input("Enter your choice: "))
        if ch == 1 :
            create() 
        elif ch == 2 :
            read()
        elif ch == 3 :
            update()
        elif ch == 4 :
            delete()
        elif ch == 5 :
            break 
        else :
            print("Invalid choice.\n")

main()