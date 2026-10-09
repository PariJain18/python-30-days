name=["Aman","Riya","Siya"]
marks=[75,90,85]
student=list(zip(name,marks))
student.sort(key=lambda X:X[1],reverse=True)
for name,marks in student:
    print(name,marks)
    
