'''
Write a Python program to compute following operations on String: 
a) To display word with the longest length 
b) To determines the frequency of occurrence of particular character in the string 
c) To check whether given string is palindrome or not 
d) To display index of first appearance of the substring'''

# Taking input
s=input("Enter the string:\n")
print("String is :",s)

def longest():
# For split string into list contain each word as element
    l=list(s.split())
# For counting longest word in the string
    cnt=[]
    for i in l:
        if len(cnt)<=len(str(i)):
            cnt=str(i)
    print("Longest word is :",cnt)
# For count longest words length (We can directly count lenght of word we got )  OR
    count=[]
    for i in l:
        count.append(str(len(i)))
    j=0
    for i in count:
        if int(str(i))>=int(j):
            j=str(i)
        else:
            continue
    print("Length of longest word is :",j)

def frequency():
# Checking no. of string selected one by one
    n=input("Enter letter you want to count :")
    count=0
    for i in s:
        if i==n:
            count=count+1
    print("There are  ",count," '",n,"'  in string.")
    
def pallen():
# Reversing the string
    str=''
    for i in s:
        str=i+str
    print("reverse sting is  :",str)
    if str==s:
        print("It is Pallendrome.")
    else:
        print("It is not Pallendrome.")
        
def first_appear():
    sub=input("Enter substring whose index you want to find :")
    if sub in s:
        print(s.index(sub))
    else:
        print("Substring is not in String")

def choice():
    while True:
        c=int(input("What do you want to do?\n1.Display word with the longest length\n2.Give frequency of occurrence of character in the string\n3.Check whether given string is palindrome or not\n4.Index of first appearance of the substring\n5.Exit\n"))
        if c==1:
            longest()
        elif c==2:
            frequency()
        elif c==3:
            pallen()
        elif c==4:
            first_appear()
        elif c==5:
            break
        else:print("Invalid Choice")
choice()
print("******************** THANK YOU *********************") 
            
