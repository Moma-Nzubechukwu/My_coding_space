wallet_balance = 5_000
print(wallet_balance)
shopping_cart_total = input("Enter total cost of items (including shipping): ")
# We know the input function always returns a string, so we convert the value of
# shopping_cart_total to float
shopping_cart_total = float(shopping_cart_total)
# Now we can check if the user's wallet balance can cover the cost of the items
# in the shopping cart
if wallet_balance >= shopping_cart_total:
 wallet_balance = wallet_balance - shopping_cart_total
 print("Order confirmed. You new wallet balance is: ", wallet_balance)
else:
 print("Insufficient funds in your wallet. You can add funds with your credit/de")
