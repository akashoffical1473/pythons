salary=30000
yrs=float(input("enter yrs:"))
if(yrs==10):
    print("percent to increase is 10%")
    a=10/100*salary
    print("the salary is extend to",a)
elif(yrs>6 and yrs<=10):
    print("percent to increase is 8%")
    b=8/100*salary
    print("the salary is extend to",b)
elif(yrs<6):
    print("percent to increase is 5%")
    c=5/10*salary
    print("the salary is extend to",c)   
else:
    print('there is no increment') 
