marks = []
for i in range(5):
    mark1=int(input("Enter marks first : "))
    marks.append(mark1)
    mark2=int(input("Enter marks second: "))
    marks.append(mark2)
    mark3=int(input("Enter marks three: "))
    marks.append(mark3)
    mark4=int(input("Enter marks four: "))
    marks.append(mark4)
    mark5=int(input("Enter marks five: "))
    marks.append(mark5)
    total=sum(marks)
    avg=total/5
    high=max(marks)
    low=min(marks)

    print("Total:",total)
    print("Average",avg)
    print("Highest",high)
    print("Lowest",low)


