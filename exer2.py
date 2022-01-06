# Exercise 2: Print the following pattern
# Write a program to print the following number pattern using a loop.

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
def numbers():
    row = 5 
    for height in range(row + 2):
        for width in range(height):
            print(width, end=' ')
        print('')

def asterisk():
    row = 5 
    for height in range(row + 2):
        for width in range(height):
            print("*", end=' ')
        print('')

ask = str(input( 'write "asterisk" or "numbers":' ) )
if ask == "asterisk":
    asterisk()
elif ask == "numbers":
    numbers()
else:
    print( 'you aswer was incorrect, try again' )
    ask = str(input( 'write "asterisk" or "numbers":' ) )