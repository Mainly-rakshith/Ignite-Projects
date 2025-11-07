# Rakshith Jayakarthikeyan
# PROG 1003 – HW2 - Code

num_letters = int(input("How many letters are in the message? "))
shift = int(input("What is the shift amount? (-26 to +26) "))

#Empty strings so you can store them later
original = "" 
message = ""

for i in range(num_letters): #Runs for how many letters the user stated
    ascii = int(input("What is the next ASCII char value? "))
    charachter = chr(ascii)
    original = original + charachter

#Capital letters
    if charachter >= 'A' and charachter <= 'Z': 
        new_value = ord(charachter) + shift #Shifts code
        if new_value > ord('Z'): #Go back to start
            new_value = new_value - 26 
        if new_value < ord('A'): #Go to end
            new_value = new_value + 26
        message = message + chr(new_value) #Adds to message

#Lowercase letters
    elif charachter >= 'a' and charachter <= 'z':
        new_value = ord(charachter) + shift
        if new_value > ord('z'):
            new_value = new_value - 26
        if new_value < ord('a'):
            new_value = new_value + 26
        message = message + chr(new_value)

#Anything else
    else:
        message = message + charachter

print("The input message was " + original)
print("The decoded message is " + message) 

