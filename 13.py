'''
Write a program to display the multiplication table as below with a given range
Sample Input
Start Table : 5
End Table: 8
'''

print("Tables")

n=int(input("Enter start number: "))
e=int(input("Enter end number: "))

i=n
while i<=e:
    for j in range(1,11):
        print(j,"*",i,"=",j*i)
    i+=1