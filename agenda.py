def userMenu():
    menu = True
    while menu:
        print ('1 - Create a new contact')
        print ('2 - Search')
        print ('3 - Help')
        print ('4 - Exit')
        menuOption = input ('Ingrese una opción: ')

        if menuOption == '1':
            saveContactFunction()
        elif menuOption == '2':
            searchFunction()
        elif menuOption == '3':
            helpFunction()
        elif menuOption == '4':
            menu = False;   

def helpFunction():
    print ("""\nHelp Menu

	Menu Navigation:
	Enter the number option followed by an enter, to select any option

	Creating a new contact:
	To create a new contact, select the first option of the menu with the number 1
	Now, type the data required in order: name, last name, email and phone numb

	Search for a contact:
	The user can search any previous contact saved, by entering the second option of the menu with the number 2
	Once inside the second option, just type the word/number you want to search followed by an enter
	""")

def saveContactFunction():
    with open("contacts.txt", "a") as f:
        f.write("new text" + '\n')
        # agregar inputs para meter los datos

def searchFunction():
    userWord = input ('Ingrese una palabra para buscar')
    with open('contacts.txt', 'r') as file:
        # arreglar la busqueda
        contacts = file.read()
        if userWord in contacts:
            print('string exist in a file')
        else:
            print('string does not exist in a file')

userMenu()