'''Accept the name, age, gender (‘M’ or ‘F’), number of days, and display the wages
accordingly.
Age: greater than or equal to 18 and greater than 30, gender: "M”, then wages will
be Rs 700 per day.
Age: greater than or equal to 18 and less than 30, gender: "F" then wages will be Rs
750 per day.
If age is greater than or equal to 30 and less than or equal to 40, and gender is "M’,
then wages will be Rs 800 per day.
Age: greater than or equal to 30 and less than or equal to 40; gender: "F," then
wages will be Rs 800 per da'''

name=input("Enter name: ")
gen=input("Enter gender(M/F): ")
age=int(input("Enter age: "))
da=int(input("Enter your total no.of working days: "))

if age>=18 and age<30 and gen=='M':
    print("Wage = ",da*700)
elif age>=18 and age<30 and gen=='F':
     print("Wage = ",da*750)
elif age>=30 and age<=40 and gen=='M':
     print("Wage = ",da*800)
elif age>=30 and age<=40 and gen=='F':
     print("Wage = ",da*850)
else:
    print("Invalid")
