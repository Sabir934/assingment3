#write  a program to get sqrt 
#logarithm number
#sine in radians 

       
import math


    
number=float(input("Enter  a positive number"))


if number<=0:
    
    print("Please enter a number greater than 0 for square root and logarithm")

else:
    sqrt_result=math.sqrt(number)
    log_result=math.log(number)
    sin_result=math.sin(number)
    

print(f"Result for the number {number}")
print(f"Square root {sqrt_result}")
print(f"Natural logarithm is {log_result}")
print(f"Sine (in radians){sin_result}")



    
    
        
        