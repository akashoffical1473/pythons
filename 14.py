'''Write a program that displays a temperature conversion table for degrees Celsius
and degrees Fahrenheit. The table should include rows for all temperatures
between 0 and 100 degrees Celsius that are multiples of 10 degrees Celsius.
Include appropriate headings on your columns. The formula for converting
between degrees Celsius and degrees Fahrenheit'''

print("Celsius to Fahrenheit")

c=int(input("Enter end range: "))
print('C','F')
i=0
while(i<=c):
    f=((i*9)/5)+32
    print(i,f)
    i=i+10