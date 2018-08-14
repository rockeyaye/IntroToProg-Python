#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   Rockey Aye
# Date:  Aug 13, 2018
# Change Log: New
# Change Description:  Rockey Aye, 8/9/2016, Create code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# task = Key of dictionary for the row of data from the file
# priority = Value of dictionary for the row of data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# dicNewRow = A New Dictionary row based on New Entry of Task and Priority
# delRow = Task and Priority to be deleted

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display current task ToDo list to the user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
#-------------------------------

# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.
File = "C:\_PythonClass\Todo.txt"
strData = ""
dicRow = {}
lstTable = []

# Extract / Open File using open, append, and close
objFile = open(File, "r")
for line in objFile:
    strData = line.split(",")
    dicRow = {"task":strData[0].strip(), "priority":strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# Step 2
# Display a menu of choices to the user
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()#adding a new line

    # Step 3
    # Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Current ToDo List:")
        for row in lstTable:
            #reading each dictionary row of data from the file
            print(row["task"] + " : " + row["priority"])

    # Step 4
    # Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        #User input on the task and its priority
        strTask = ()
        while not strTask:
            strTask = str(input("Please Enter Task: ")).strip().title()
        strPriority = ()
        while not strPriority:
            strPriority = str(input("Please Enter Priority (High, Medium, Low): ")).strip().title()
        dicRow = {"task":strTask,"priority":strPriority}
        lstTable.append(dicRow)
        #print out the updated list
        print("\nUpdated ToDo List:")
        for row in lstTable:
            print(row["task"] + " : " + row["priority"])
        continue

    # Step 5
    # Remove a new item to the list/Table
    elif(strChoice == '3'):
        #5a-Allow user to indicate which row to delete
        strDelete = ()
        while not strDelete:
            strDelete = input("Please Enter Task to be Deleted: ").strip().title()
        # if entry is in the list - using a boolean function
        BlankRemoved = False
        intRow = 0
        while(intRow < len(lstTable)):
            if(strDelete == str(list(dict(lstTable[intRow]).values())[0])):
                del lstTable[intRow]
                BlankRemoved = True
            intRow += 1
        #end for loop
        #5b-Update user on the status
        if(BlankRemoved == True):
            print("Remove:", strDelete)
        else:
            print("Item", strDelete, "is not found.")
        # print out the updated list
        print("\nUpdated ToDo List AFTER Removed Task:")
        for row in lstTable:
            print(row["task"] + " : " + row["priority"])
        continue

    # Step 6
    # Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        strSave = input("Do you want to save data into ToDo.txt (Save = Y or Not Save = N)? ".strip().lower())
        if (strSave.lower() == 'y'):
            objFile = open(File, "w")
            for dicRow in lstTable:
                objFile.write(dicRow["task"] + "," + dicRow["priority"] + "\n")
            objFile.close()
            input("You've saved the updated data.")
        else:
            input("Updated Data is not saved.  Original Data is available.")
        continue

    elif (strChoice == '5'):
        break #and Exit the program