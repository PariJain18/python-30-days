shopping_list=[]
while True:
    choice=input("Enter choice add,remove,view and quit:")
    if choice == "add":
        item=input("Enter Item")
        shopping_list.append(item)
    elif choice == "remove":
        item=input("Enter item to remove:")
        shopping_list.remove(item)
    elif choice == "view":
        print("Shopping list:",shopping_list)
    elif choice == "quit":
        print("Good Day") 
        break        
