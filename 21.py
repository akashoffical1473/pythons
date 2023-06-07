'''The rules for determining whether or not a year is a leap year follow:
● Any year that is divisible by 400 is a leap year.
● Of the remaining years, any year that is divisible by 100 is not a leap year.
● Of the remaining years, any year that is divisible by 4 is a leap year.
● All other years are not leap years.
Write a program that reads a year from the user and displays a message indicating
whether or not it is a leap year'''

yr=int(input("Enter a year to check whether leap yr or not: "))

if  (yr%400==0) or (yr%4==0) and (yr%100!=0):
    print(yr,"is a leap year")
else:
    print(yr,"is not a leap year")