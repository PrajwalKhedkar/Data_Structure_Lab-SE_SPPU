''''
Write a python program to store first year percentage
of students in array.
Write function for sorting array 
of floating point numbers in ascending order using quick sort
and display top five scores.
'''

data=[]
num=int(input("Enter number of students = "))
for i in range(0,num):
    print("Enter pecentage of student",i+1,"=")
    perc=float(input())
    data.append(perc)
print("Unsorted list is :\n",data)

# data= [24,14,44,21,54] 
                          
def partition(data,start,end):
    pivot=data[start]  # pivot
    low=start+1   #i
    high=end        #j
    while True:
        while low<=high and data[low]<=pivot:   # i<=j and data[i] <= pivot 
            low=low+1                                    #  i++
        
        while low<=high and data[high]>=pivot:   # i<=j and data[j]>= pivot   
            high=high-1                              #   j--
            
        if low<=high:
            data[low],data[high]=data[high],data[low]  #swap elements
        else:
            break
    data[start],data[high]=data[high],data[start]        # swap pivot with j 
    
    return high
    
def quicksort(data,start,end):
    if start>=end:
        return
    else:
        part=partition(data,start,end) #[[],[]]
        quicksort(data,start,part-1)
        quicksort(data,part+1,end)

quicksort(data,0,num-1)
print("Sorted list is :\n",data)
print("Top 5 Scores are :")
i=num
top=[]
while i>num-5:
    t=data[i-1]
    top.append(t)
    i=i-1
print(top)