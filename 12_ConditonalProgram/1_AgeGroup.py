# Age : < 13 => Child
# Age : 13-19 => Teenager
# Age : 20-59 => Adult
# Age : >=60   => DEAD

age = int(input("Enter Age: "))

if (age < 13):
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Dead")
