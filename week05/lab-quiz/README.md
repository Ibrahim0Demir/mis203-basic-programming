Lab 05 - Shipping Quote  

1. Test Ran  
I tested the discount rate boundary threshold using `assert`:  
- Tested `get_discount_rate(499.99)` to ensure it returned `0.0`.  
- Tested `get_discount_rate(500.0)` to ensure it triggered the `0.10` discount rate.  

2. Change Made After Testing  
After testing with float numbers, I noticed potential floating-point precision issues (e.g., extra decimal places in totals). To prevent this and keep financial values clean, I wrapped the return statements in `round(..., 2)`.  
  

Print vs return  
- `return` sends a computed value back to the caller so it can be stored in a variable or used in subsequent calculations.  
- `print()` only displays text on the screen/console and returns `None`, meaning the output cannot be reused by other functions.  