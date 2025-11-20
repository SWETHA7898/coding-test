class Calculator:
  def calculate(self,a,b,operation):
    if operation == "addition":
      return a + b
    elif operation == "subtraction":
      return a - b
    elif operation == "multiplication":
      return a * b
    elif operation == "division":
      if b!=0:
        return a/b
      else:
        print("Zero divison Error")

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
operation=input("Enter type of opeartion (addition/subtraction/multiplication/divison):")
calc=Calculator()

result=calc.calculate(a,b,operation)
print(result)
