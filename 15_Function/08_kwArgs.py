# Create a function that accepts any number of argument and prints them in the format 
# Key:Value
def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="adarsh", power="unknown")
print_kwargs(name="adarsh")
print_kwargs(name="adarsh", power="unknown",work="no")