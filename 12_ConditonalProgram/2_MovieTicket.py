 # Movie tickets are priced based on ages : $12 for adult 18 and over
 #                                         $8 for children
 # Everyone gets a $2 discount on Wednesday

day = input("Enter the day(format- Sunday ): ") 
age = int(input("Enter the age: "))

price = 12 if age >=18 else 8

if day == "Wednesday":
    price -= 2

print("Price for you is $",price)