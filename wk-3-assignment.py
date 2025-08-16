# 1. calculating discount price
def calculate_discount(price, discount_percent):
    if discount_percent >= 20 :
        new_price = price - (discount_percent)/100 * price
        print(f"The price of the prdouct is: #{new_price}")
    else :
        print(f"The price of the prdouct is: #{price}")

# 2. promptimg the user to enter the price and discount given
price = eval(input("Enter the normal price of the product: "))
discount_percent = eval(input("Enter the discount percentage on the product: "))
calculate_discount(price, discount_percent)
