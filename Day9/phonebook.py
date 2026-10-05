phonebook={}
while True:
    ch=input("Add, Search , Update, Delete or Quit :")
    if ch=="add":
        name=input("Enter name :")
        number=input("Enter phone :")
        phonebook[name]=number
    elif ch=="search":
        name=input("Enter name :")
        print(phonebook.get(name,"Contact not found"))
    elif ch=="update":
            name=input("Enter name :")
            number=input("Enter phone :")
            phonebook[name]=number
    elif ch=="delete":
            name=input("Enter name :")
            phonebook.pop(name,None)
    elif ch=="quit":
          break           