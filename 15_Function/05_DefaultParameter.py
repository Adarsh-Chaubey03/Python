# Write a function to greet a user. If no name is provided it should greet default name
def greet(name ="User"):
    return "Hello, " + name + "!"

print(greet("adarsh"))
print(greet())