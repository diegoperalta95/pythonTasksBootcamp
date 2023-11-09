def userMenu():
    menu = True
    while menu:
        print ('1 - Create a new contact')
        print ('2 - Search')
        print ('3 - Help')
        print ('4 - Exit')
        menuOption = input ('Insert an option: ')

        if menuOption == '1':
            saveContactFunction()
        elif menuOption == '2':
            searchFunction()
        elif menuOption == '3':
            helpFunction()
        elif menuOption == '4':
            menu = False;   
        else: 
            print ('\n Insert a valid option \n')

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
    # Create a contact asking info from the user, and then saves it to a contacts.txt file
    userName = input ('Insert name: ')
    userLastName = input ('Insert last name: ')
    userEmail = input ('Insert email: ')
    userPhone = input ('Insert phone: ')

    print ('\n Used added! \n')
    with open("contacts.txt", "a") as f:
        f.write(userName + ' ' + userLastName + ' ' + userEmail + ' ' + userPhone + '\n')

def searchFunction():
    # Search function, ask for a word an then searchs for it in contacts.txt
    userWord = input ('Insert a word for searching: ')
    matchingContacts = []
    with open('contacts.txt', 'r') as file:
        for line in file:
            if userWord.lower() in line.lower():
                matchingContacts.append(line.strip())
    
    matchingContactsString = [str(contact) for contact in matchingContacts]
    print('\n' + '\n'.join(matchingContactsString) + '\n')

userMenu()