#  Final Bill Calculator
#  A simple Python program that calculates the final bill amount after applying a discount based on the bill value

def total_amount(amount):

   if amount >= 10000:
      discount_rate = 0.50
   elif amount >= 5000:
      discount_rate = 0.25
   elif amount >= 3000:
      discount_rate =0.11
   elif amount >= 1500:
      discount_rate = 0.4
   else:
      discount_rate = 0.00

   discount_amount = amount * discount_rate
   final_amount = amount - discount_amount
   return final_amount 

bills = [3456,5678,12009,4567,345,5467,8756,12300,1298,6087,234,126]

for i in range(len(bills)):
   final_bill = total_amount(bills[i])
   print(f"Bill {i + 1}: Final Amount = ₹{final_bill:.2f}")









                   
   
