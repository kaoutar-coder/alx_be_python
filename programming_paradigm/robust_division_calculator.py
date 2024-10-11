def safe_divide(numerator, denominator):
    try:
        numerator= float(input("enter the numerator: "))
        denominator= float(input("enter the denominator: "))

        result=numerator/denominator

        return f"the result of divising {numerator} by {denominator} is {result}"

    except ZeroDivisionError:
        return"sorry we cant divided by zero"

    except KeyError:
        return"error: the inputs can be a numbers"














                 
         
        
   
    

