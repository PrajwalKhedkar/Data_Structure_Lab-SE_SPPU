'''
Write a Python program to store marks scored in subject 
“Fundamental of Data Structure” by N students in the class. 
Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class 
c) Count of students who were absent for the test 
d) Display mark with highest frequency

'''

def average():
    add=0
    for i in range(len(marks)):
        if marks[i] !='AB':
            add=add+int(marks[i])
    print("Average of marks is :",add/num)

def highest_and_lowest():
    high=0
    for i in range(len(marks)):
        if marks[i]!= 'AB':
            if int(marks[i])>int(high):
                high=marks[i]
    print("Highest marks are :",high)
    low=100
    for i in range(len(marks)):
        if marks[i]!= 'AB':
            if int(marks[i])<int(low):
                low=marks[i]
    print("Lowest marks are :",low)
    
def absent():
    count=0
    for i in range(len(marks)):
        if marks[i]=='AB':
            count=count+1
    print("No of absent stuents are :",count)

def freqency():
    max=0
    res=marks[0]
    for i in marks:
        freq=marks.count(i)
        if freq>max:
            max=freq
            res=i
    print("Highest occuring marks are: ",res)
    print(max,"students got ",res,"marks")
    
marks=[]
num=int(input("Enter no. of students :"))
for i in range(0,num):
    print("Enter marks of student(For absent student enter '-1') ",i+1,":")
    stud=int(input())
    
    marks.append(stud)
print("List is:",marks)
flag=1
while flag==1:
    print("What do you want to do?\n1.The average score of class\n2.Highest score and lowest score of class \n3.Count of students who were absent for the test\n4.Display mark with highest frequency\n5.Exit\n")
    choice=int(input())
    if choice==1:
        average()
    elif choice==2:
        highest_and_lowest()
    elif choice==3:
        absent()
    elif choice==4:
        freqency()
    elif choice==5:
        flag=0
    else:print("Invalid choice.")
       