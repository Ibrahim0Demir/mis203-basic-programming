Week 3 Lab: Order Approval Policy  

Testing and Changes  
Test I ran: I tested a member order for exactly 500 TRY. I wanted to see if the 10% discount works at the exact boundary, and it did.  
What I changed: I realized I could enter negative numbers for the quantity. I added an `if requested_quantity <= 0` check to fix this. I also added `.strip().lower()` for inputs to prevent errors if I type capital letters.  
  
Test Cases  
Test 1 (Just below 500): 499 TRY, Member: yes -> Result: Approved, Regular price (499.0 TRY)  
Test 2 (Exactly 500): 500 TRY, Member: yes -> Result: Approved, 10% discount applied (450.0 TRY)  
Test 3 (Above 500): 600 TRY, Member: yes -> Result: Approved, 10% discount applied (540.0 TRY)  
Test 4 (Invalid Quantity): Quantity: -2 -> Result: Rejected (Invalid quantity)  
Test 5 (Low Stock): Stock: 2, Quantity: 5 -> Result: Rejected (Insufficient stock)  
