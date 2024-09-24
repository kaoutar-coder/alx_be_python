num1= float(input("Enter the first number:"))
num2= float(input("Enter the second number:"))
operation= input("Choose the operation (+, -, *, /):")

match operation:
    case "*":
        result1= num1 * num2
        print("The result is " + str(result1) + " ." )
    case "+":
        result2= int(num1 + num2)
        print("The result is " + str(result2) + " ." )
    case "-":
        result3= num1 - num2
        print("The result is " + str(result3) + " ." )
    case "/":
        if num2== 0 :
            print("Cannot divide by zero.")
        else:
         result4= num1 / num2
         print("The result is " + str(result4) + " ." )
