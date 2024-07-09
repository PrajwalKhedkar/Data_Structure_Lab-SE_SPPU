'''a) Write a python program to store names and mobile numbers of your friends in sorted
order on names. Search your friend from list using binary search (recursive and nonrecursive). Insert friend if not present in phonebook '''
'''
def binary_search(arr,key):
    low=0
    high=len(arr)-1
  
    while low<=high:             #[1,2,3,   4    ,5,6,7]
        mid=(low+high)//2      #   low     mid         high
                                    #         4  ,5,6,7]
        if data[mid][0]== key:#  [1,2,3]                low   high
            return mid
        elif data[mid][0]<key:
            low=mid+1
        elif data[mid][0]>key:
            high=mid-1
            
    return-1
    
def sort():
    for j in range(0,len(data)):
        #swapped=False
       # i=0
        for i in range(len(data)-1):
            if data[i][0]>data[i+1][0]:
                data[i],data[i+1]=data[i+1],data[i]
                #swapped=True
        #if swapped==False:
          #  break
    print(data)

def insert():
    c=[name]
    num=(input("Enter mobile number :"))
    c.append(num)
    data.append (c)
    print('Unsorted list is:\n',data)
    
def call():
    if index==-1:
        print("Search Not Found")
        choice=input(("Do you want to insert number?(Y/N)\n"))
        if choice=='Y':
            insert()
            print('Sorted list is:')
            sort()
        elif choice=='N':
            print('Sorted list is:')
            sort()
        else:print("Invalid Input!!!\nEXITTING........")
    else:
        print("Search Found")
        print('Sorted list is:')
        sort()

data=[['A',984563210],['B',976543210],['C',96674523190],['D',8978675634]]
print("Unsorted list is:\n",data)       
name=input("Enter name you want to search:")
index=binary_search (data,name)
call()

'''

data=[['A',984563210],['B',976543210],['C',96674523190],['D',8978675634]]
def bin_srch(data,key):
    low=0
    high=len(data)-1
    
    while True:
        mid=(low+high)//2
        if data[mid][0]==key:
            return mid
        elif data[mid][0]<key:
            low=mid+1
        elif data[mid][0]>key:
            high=mid-1
        return -1
def sort():
    for j in range(0,len(data)):
        #swapped=False
       # i=0
        for i in range(len(data)-1):
            if data[i][0]>data[i+1][0]:
                data[i],data[i+1]=data[i+1],data[i]
                #swapped=True
        #if swapped==False:
          #  break
    print(data)            
    
