''' Write a python program to compute following computation on matrix: 
a) Addition of two matrices 
b) Subtraction of two matrices 
c) Multiplication of two matrices 
d) Transpose of a matrix
'''
def addition():
    add=[]
    for i in range(R1):
        addc=[]
        for j in range(C1):
            addr=matrix1[i][j]+matrix2[i][j]
            addc.append(addr)
        add.append(addc)
    print("\nAddition of matrices is:")
    for i in range(R1):
        for j in range(C1):
            print(add[i][j],end=" ")
        print()

def substraction():
    sub=[]
    for i in range(R1):
        subc=[]
        for j in range(C1):
            addr=matrix1[i][j]-matrix2[i][j]
            subc.append(addr)
        sub.append(subc)
    print("\nSubstraction of matrices is :")
    for i in range(R1):
        for j in range(C1):
            print(sub[i][j],end=" ")
        print()
    
def multiplication():
    M=[]
    for i in range(R1):
        multi=[]
        for j in range(C1):
            m=0
            multi.append(m)
        M.append(multi)
    for i in range(R1):
        for j in range(C2):
            for k in range (R2):
                M[i][j]+=matrix1[i][k]*matrix2[k][j]
    print("Multiplication of matrices is :")
    for i in range(R1):
        for j in range(C1):
            print(M[i][j],end=" ")
        print()
            
def transpose():
    flag=1
    T=[]
    for i in range(R1):
        t=[]
        for j in range(C1):
            trn=0
            t.append(trn)
        T.append(t)
        
    while flag==1:
        sel=int(input("Select matrix to transpose :\n1.FIRST\n2.SECOND\n3.Exit\n"))
        if sel==1:
            for i in range(R1):
                for j  in range(C1):
                    T[i][j]=matrix1[j][i]
            print("\nTranspose of first matrix is:")
            for i in range(R1):
                for j  in range(C1):
                    print(T[i][j],end=" ")
                print()
        elif sel==2:
            for i in range(R2):
                for j  in range(C2):
                    T[i][j]=matrix2[j][i]
            print("\nTranspose of second matrix is:")
            for i in range(R2):
                for j  in range(C2):
                    print(T[i][j],end=" ")
                print()
        elif sel==3:
            flag=0
        else:
            print("Invalid Input")
            

                
        
    
print("********** Matrix 1 **********")
R1=int(input("Enter no. of rows :"))
C1=int(input("Enter no. of columns :"))
matrix1=[]
for i in range(R1):
    row1=[]
    for j  in range(C1):
        ele1=int(input("Enter element = ",))
        row1.append(ele1)
    matrix1.append(row1)
print("First matrix is : ")
for i in range(R1):
        for j in range(C1):
            print(matrix1[i][j],end=" ")
        print()
    

print("********** Matrix 2 **********")
R2=int(input("Enter no. of rows :"))
C2=int(input("Enter no. of columns :"))
matrix2=[]
for i in range(R2):
    row2=[]
    for j  in range(C2):
        ele2=int(input("Enter element = ",))
        row2.append(ele2)
    matrix2.append(row2)
print("Second matrix is : ")
for i in range(R1):
        for j in range(C1):
            print(matrix2[i][j],end=" ")
        print()

mark=1
while mark==1:
    choice=int(input("What do you want to do?\n1.Addition\n2.Substraction\n3.Multiplication\n4.Transpose\n5.Exit\n"))
    if choice==1:
        addition()
    elif choice==2:
        substraction()
    elif choice==3:
        multiplication()
    elif choice==4:
        transpose()
    elif choice==5:
        mark=0
    else:
        print("Invalid Choice")
