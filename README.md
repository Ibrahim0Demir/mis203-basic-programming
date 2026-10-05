# MIS 203 Basic Programming

**Name:** Ibrahim DEMIR    
**Student Number:** 2404109056  
**Department:** Management Information Systems   
**Course Name:** MIS203 Basic Programming   

Week 01 Assignment Details
AI Tool Used: Gemini

Prompt Used: Create a simple Python program that asks the user for their Name, Department, Age, and Career Goal, then prints a short student profile matching a specific example output format.

What did you change?: I reviewed the generated code and adjusted the variables and f-string formatting to match the exact output requirements.

Week 02 Assignment Details

AI Tool Used: None

What does break do in your program?
In this program, the break command is used for exiting the while loop.

Week 03  
AI Tool Used: Gemini  
  
Prompt Used: I pasted the assignment rules and my code, and asked: "Am I on the right track? Are there any mistakes in my code?"  

What did you change? I made a small mistake in the discount calculation at first, so I fixed the math formula for the final ticket price.  
  
Tests:  
1. Test 1 (Standard): Input: (Name: Ali, Age: 30, Day: weekend, Student: no) -> Result: `Ali: 250.00 TRY (Standard)`  
2. Test 2 (Boundary Age - Child): Input: (Name: Can, Age: 6, Day: weekday, Student: yes) -> Result: `Can: 120.00 TRY (Child)`  
3. Test 3 (Boundary Age - Student): Input: (Name: Zeynep, Age: 25, Day: weekday, Student: yes) -> Result: `Zeynep: 140.00 TRY (Student)`  
  
Why does the order of the rules matter?  
The order is critical because the `if/elif` structure stops checking as soon as it finds the first `True` condition. If the "Student" rule came before the "Child" rule, a 10-year-old student would receive a 30% discount instead of the 40% discount they deserve. Checking from the highest priority/discount downwards ensures everyone gets the correct category.  
