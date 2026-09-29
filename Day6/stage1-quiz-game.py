while True:
    score=0
    print("PYTHON QUIZ GAME")
    print("***Welcome to the python Quiz***")
    print("Q1. What is Python")
    print("a.  Programming Language")
    print("b.  Browser")
    print("c.  Database")
    print("d.  Operating System")
    ch=input("Enter your Chioce")
    if(ch=="a"):
        score+=1

    print("Q2. What is the extension of a Python file")
    print("a.  .html")
    print("b.  .py")
    print("c.  .css")
    print("d.  .java")
    ch=input("Enter your Chioce")
    if(ch=="b"):
            score+=1   

    print("Q3. Which function is used to display output?")
    print("a.  input()")
    print("b.  show()")
    print("c.  print()")
    print("d.  display")
    ch=input("Enter your Chioce")
    if(ch=="c"):
        score+=1

    print("Q4.  Which function is used to take input?")
    print("a.  input()")
    print("b.  print()")
    print("c.  read()")
    print("d.  get()")
    ch=input("Enter your Chioce")
    if(ch=="a"):
            score+=1

    print("Q5.  Which symbol is used for comments in python?")
    print("a.  //")
    print("b.  #")
    print("c.  --")
    print("d.  **")
    ch=input("Enter your Chioce")
    if(ch=="b"):
             score+=1


    print("Q6.  Which keyword is used to check a condition?")
    print("a.  for")
    print("b.  while")
    print("c.  if")
    print("d.  print")
    ch=input("Enter your Chioce")
    if(ch=="c"):
                score+=1

    print("Q7.  Which loop is commonly used with range()?")
    print("a.  if")
    print("b.  for")
    print("c.  print")
    print("d.  input")
    ch=input("Enter your Chioce")
    if(ch=="b"):
                score+=1

    print("Q8.  Which symbol is used to assign a value to a variable?")
    print("a.  ==")
    print("b.  =")
    print("c.  +")
    print("d.  *")
    ch=input("Enter your Chioce")
    if(ch=="b"):
                score+=1

    print("Q4.  Which data type is used for whole numbers?")
    print("a.  String")
    print("b.  Float")
    print("c.  Integer")
    print("d.  Boolean")
    ch=input("Enter your Chioce")
    if(ch=="c"):
               score+=1

    print("Q4.  Which keyword is used to repeat a block of code?")
    print("a.  for")
    print("b.  if")
    print("c.  print")
    print("d.  input")
    ch=input("Enter your Chioce")
    if(ch=="a"):
                score+=1

    print("**** QUIX RESULT ****")
    print("Your Score",score)
    per=(score/10)*100
    print("Percentage is:",per,"%")
    if per>=80:
            print("Excellent!")
    else:
            print("Keep practising!") 

    play_again=input("\nPlay again ? (y/n):")   
    if play_again!="y":
            print("thank you for playing!:") 
    break               

                                 
                                 
                     
                                  


