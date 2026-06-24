items ={
    "milk":(50,2),
    "eggs(12)":(150,6),
    "butter":(260,12),
    "bread":(50,0),
    "chicken 1kg":(150,11),
    "vegetables":(200,5),
    "fruits":(200,7),
    "sugar 1kg":(60,3),
    "bakery":(400,27),
    "rice":(150,2)


}
def calculate_items(price,qty,gst):
    subtotal = price*qty
    gst_amount = (price * gst) /100
    return subtotal,gst_amount
def apply_discount(amount,discount):
    return amount -(amount*discount) / 100
    

   
    


     

           

        






