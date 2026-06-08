Menu={"pista": 30, "kesar": 25, "badam": 35, "kulfi": 20, "kesarpista": 40}
print("WELCOME TO CHACHA ICECREAM WALA:")
print("pista: RS30\n", "kesar: RS25\n", "badam: RS35\n", "kulfi: RS20\n", "kesarpista: RS40\n")
order_total=0
item_1=input("order your item:")
if item_1 in Menu:
        order_total+= Menu[item_1]
print(f'your item{item_1} has been added to your order')
    
item_2=input("order your second item:")
if item_2 in Menu:
        order_total+= Menu[item_2]
print(f'your item {item_2} has been added to your order')
print(f"the total of your order is: {order_total}")
