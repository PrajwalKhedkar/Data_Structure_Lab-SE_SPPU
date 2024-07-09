''' 
Write a python program to store first year percentage of students in array. 
Write function for sorting array of floating point numbers in ascending order using 
a) Selection Sort 
b) Bubble sort 
and display top five scores.

'''


list=[]
num=int(input("Enter the no. of students :"))
for i in range(0,num):
    print("Enter Precentage of Student ",i+1,":")
    percent=float(input())
    list.append(percent)
print("Your list is :",list)
                                    
def selection_sort():           
    for i  in range(0,num):
        min_num=i
        for j in range(i+1,num):
            if list[j]<list[min_num]:
                min_num=j
                list[i],list[min_num]=list[min_num],list[i]
    print("Sorted list is :",list)
    top=[]
    for i in range(0,num):
        if i<=4:
            t=list[i]
            top.append(t)
    print("Top 5 are :",top)
        

def bubble_sort():
    for i  in range(1,num-1):
        for j in range(0,num-i-1):    #[4,3,2,1,7,5,6]
            if list[j]>list[j+1]:      #j i       j i
                list[j],list[j+1]=list[j+1],list[j]
    print("Your list is :",list)
    top=[]
    for i in range(0,num):
        if i<=4:
            t=list[i]
            top.append(t)
    print("Top 5 are :",top)
        


flag=1
while flag==1:
    c=int(input("What do you want?\n1.Selection sort\n2.Bubble sort\n3.Exit\n"))
    if c==1:
        selection_sort()
    elif c==2:
        bubble_sort()
    elif c==3:
        flag=0
    else:
        print("Invalid Input")

print("******************** THANK YOU *********************")