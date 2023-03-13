def CreateANewFile():

    #this code will attempt to create a file with the specified name, however will return an error with file already exists (this can be useful)
    myfile = open("ThisFileDoesNotExist.txt", "x")

    myfile.write("This a new file!")
    myfile.close()

    fileName = input("Type in the name of a file you would like to create:\n")
    newFile = open(fileName + ".txt", "x")

    newFile.write("This is another new file")
    newFile.close()

def AppendToAFile():

    appendFile = open("ThisFileDoesNotExist.txt", "a")
    appendFile.write("\nThis text has been appended to the end of the a file")
    appendFile.close()

def ReadFile():

    readFile = open("ListFile.txt", "r")
    myList = list()

    for line in readFile:
        list.append(int(line))

def WriteListToFile(names):

    listFile = open("ListFile.txt", "w")
    #You can use the "w" parameter to overwrite the contents of a file

    for x in range(0, len(names)):
        listFile.write(names[x] + "\n")

    listFile.close()

def Main():

    # List of random names
    names = ["John", "Sarah", "Michael", "Jessica", "Kevin", "Emily", "David", "Olivia", "William", "Sophia"]

    bLoop = True

    while bLoop == True:

        # Display menu options
        print("Welcome to the file management system!")
        print("1. Start Creating a new file - Will throw an error")
        print("2. Start writing to a file - by appending to the end, regardless if the file already exists")
        print("3. Write a list to a file")
        print("4. Start Reading from a file")
        print("5. Close this program")

        # Get user input
        choice = input("Enter your choice (1-4): ")

        # Perform action based on user choice
        if choice == "1":
            print("You chose to start creating a file, but this will potentiall throw an error if the file you try to create already exists.")
            CreateANewFile()
        elif choice == "2":
            print("This will add some text to the end of a file, or create one if it does not alreayd exist...")
            AppendToAFile()
        elif choice == "3":
            WriteListToFile(names)
            print("This will write a list of names to a file...")
        elif choice == "4":
            print("Lets read the lines from the file...\n\n")
            ReadFile()
        elif choice == "5":
            print("Closing the program.")
        else:
            print("Invalid choice.")

Main()

