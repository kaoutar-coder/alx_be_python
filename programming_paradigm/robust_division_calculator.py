def safe_divide(numerator, denominator):
    try:
        
        result=float(numerator) / float(denominator)

        return f"the result of divising {numerator} by {denominator} is {result}"

    except ZeroDivisionError:
        return"sorry we cant divided by zero"

    except KeyError:
        return"error: the inputs can be a numbers"














                 
         
        
   
    

