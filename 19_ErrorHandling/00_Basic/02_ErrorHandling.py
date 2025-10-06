file = open('youtube.txt','w') # if file does not exist-> it will auto create it

try:
    file.write('chai aur code')
finally:
    file.close()
# alternate method   
with open('youtube.txt','w') as file:
    file.write('chai aur python')