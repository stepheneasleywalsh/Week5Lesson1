# Make a function that finds the first root
def SolveQuad1(a,b,c):
    delta = b**2 - 4*a*c
    root = (-b+delta**0.5)/(2*a)
    return(root)

# Make a function that finds the second root
def SolveQuad2(a,b,c):
    delta = b**2 - 4*a*c
    root = (-b-delta**0.5)/(2*a)
    return(root)

# Ask the person their name and their a,b and c
name = input("What is your name?")
print("Hello",name.capitalize(),"I can solve ax^2+bx+c=0")
a = int(input("a=?"))
b = int(input("b=?"))
c = int(input("c=?"))

# Show them the two roots
print("Root one is",SolveQuad1(a,b,c))
print("Root two is",SolveQuad2(a,b,c))

# Exit
quit()