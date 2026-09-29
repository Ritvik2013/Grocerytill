print("Hi welcome to the Grocery Store")
billing=True
total_cost=0
while billing:
    name=input("What is your name?")
    item_count=int(input(f"Hi {name}, how many of this item do you want to buy?"))
    if item_count<=0:
        print("Invalid amount. Please type in a positive interger.\n")
        continue
    customer_cost=0
    item_number=1
    while item_number<=item_count:
        item_name=input(f"What is the name of item number {item_number}?")
        price=int(input(f"What is the price of item number {item_number}?"))
        quantity=int(input(f"How many of this item do you want to buy?"))
        if price<=0 or quantity<=0:
            print("Invalid amount. Please type in a positive interger.\n")
            continue
        item_number+=1
        item_total=price*quantity
        customer_cost+=item_total
    print(f"The total cost for {name} is {customer_cost}$")
    total_cost+=customer_cost
    if price<50:
        low_price_items+=quantity
    elif price>=50 and price<100:
        mid_price_items+=quantity
    else:
        high_price_items+=quantity
    again=input("Is this the Next costomer?").lower()
    if again=="no":
        billing=False
for slot in range(1,4):
    if slot==1:
        price_range, total= "Low Price Items", low_price_items
    elif slot==2:
        price_range, total= "Mid Price Items", mid_price_items
    elif slot==3:
        price_range, total= "High Price Items", high_price_items
    if total>0:
        print(f"{price_range} sold: {total}",end="")

        for item in range(total):
            print("*",end="")