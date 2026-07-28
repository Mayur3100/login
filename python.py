# A simple calculator function
def calculate():
    while True:
        try:
            op = input("Enter operator (+,-,*,/) or 'q' to quit: ")
            if op == 'q': break
            n1 = float(input("First number: "))
            n2 = float(input("Second number: "))
            
            if op == '+': print("Result:", n1 + n2)
            elif op == '-': print("Result:", n1 - n2)
            elif op == '*': print("Result:", n1 * n2)
            elif op == '/':
                print("Result:", n1 / n2 if n2 != 0 else "Error: Div by 0")
        except ValueError: print("Invalid input.")



# calculate() # Uncomment to run
