import grocery_module as gm

cart = []

print("---------grocery store------------")
print("ID|ITEM|PRICE|GST%")
def show_menu():
 for i in gm.items:
    name,price,gst = gm.items[i]
    print(f"{i}. {name} - RS{price} (gst{gst}%)")

# while True:
#     show_menu()
#     choice = input("\n Enter item ID to add (or q to quit): ")
#     if choice.lower() == 'q':
#         break
#     choice = int(choice)
#     if choice not in gm.items:
#         print("Invalid item ID")
#         continue

#     qty = int(input("Quantity: "))
#     cart.append((choice,qty))
#     print("added to cart")

#     discount = float(input("Enter discount percent% (0 for none)"))


def show_bill(cart,discount):
    print("\n===========Grocery store Bill============")
    print(f"{'item':<15}{'Qty':<5}{'price':<8}{'gst':<8}{'total':<10}")
    subtotal = 0
    total_gst = 0

    for choice,qty in cart: 
        name,price,gst=gm.items[choice]

        total_items,gst_amount = gm.calculate_items(price,qty,gst)

        discounted_subtotal = gm.apply_discount(total_items, discount)


        subtotal += discounted_subtotal
        total_gst += gst_amount

        print(f"{name:<15}{qty:<5}{price:<8.2f}{gst_amount:<8.2f}{discounted_subtotal:<10.2f}")

    subtotal_after_discount = gm.apply_discount(subtotal,discount)
    final_amount = subtotal_after_discount + total_gst

    print("-"*41)
    print(f"{'subtotal:':<30} RS{subtotal:.2f}")
    print (f"{f'discount ({discount}%):':<30}Rs{subtotal_after_discount :.2f}")
    print(f"{'gst_total:':<30}Rs {total_gst:.2f}")
    print("-" *41)
    print(f"{'Final_amount :':<30}Rs{final_amount:.2f}")
    print("-" *41)
    print("thank you")
    

if __name__ == "__main__":
           
    while True:
        show_menu()
        choice = input("\nEnter item ID to add (or q to quit): ")
        if choice.lower() == 'q':
         break
        if not choice.isdigit() or int(choice) not in gm.items:
          print("Invalid item Id.try again")
          continue
        choice = int(choice)
        qty = input("\nEnter quantity :")
        if not qty.isdigit():
          print("qty mus be a number.try again")
          continue
        qty =int(qty)
        
        discount = input("Enter discount %:")
        discount = int(discount) if discount.isdigit() else 0
        cart.append((choice,qty))