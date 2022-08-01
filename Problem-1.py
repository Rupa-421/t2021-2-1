# Creating a class
class Calculator:
    def input(self,a,b,type_of_operation):
        # If zero division not possible
        if b == 0:
            print("Division by zero not possible")
        #Checking the type of operation and returning the output
        if type_of_operation == '+':
            return a+b
        elif type_of_operation == '-':
            return a-b
        elif type_of_operation == '*':
            return a*b
        elif type_of_operation == '/':
            return a/b
#Creating an object for the class
obj=Calculator()
#Taking the input
inputstring=input("enter input in the form of a b type_of_operation: ")
listofinputstring=inputstring.split()
a,b,type_of_operation=listofinputstring[0],listofinputstring[1],listofinputstring[2]
print("The operation results "+str(obj.input(float(a),float(b), type_of_operation)))