'''Three numbers form a Pythogorean triple if the sum of the squares of two numbers
is equal to the square of the third.If
they form a Pythoagorean triple, then print ‘1," otherwise print ‘0’.'''

a,b,c=map(int,input("Enter triangle sides with space :").split())

sum=(a**2)+(b**2)
result=print("1") if sum==(c**2) else print("0")

    