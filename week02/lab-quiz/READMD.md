If you run the program and type letters when asked for a quantity, Python will immediately crash and display a ValueError. The error message will look something like this:  
ValueError: invalid literal for int() with base 10: 'two'  
Test Run  
I tested the program with 2 items at 50.00 TRY and 1 item at 80.00 TRY. I applied a delivery fee of 20.00 TRY and a tax rate of 10%. The program successfully calculated the subtotal as 180.00 TRY, the tax as 18.00 TRY, and the final total as 218.00 TRY.
Change After Testing  
During the initial coding phase, I encountered a syntax error because I missed a closing parenthesis on the `delivery_fee = float(...)` line. I corrected this structural error to allow the script to execute properly.
