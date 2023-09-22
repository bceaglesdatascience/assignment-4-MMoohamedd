purchase = int(input("Number of purchases: "))
sales_tax = float(input("Sales tax: "))
customer_list =[]
costs_list =[]
for i in range(purchase):
    customer = str((input("Customer: ")))
    customer_list.append(customer)
    costs = float(input("Cost: "))
    costs_list.append(costs)

def add_tax(costs_list,sales_tax):
    sales_tl=[]
    for cost in costs_list:
        cost= cost * (1 + sales_tax)
        sales_tl.append(cost)
    return sales_tl

items_with_tax= add_tax(costs_list, sales_tax)

customer_tax = {}
for i in range (purchase):
    customer =customer_list[i]
    item =items_with_tax[i]
    if customer in customer_tax:
        customer_tax[customer] += item
    else:
        customer_tax[customer] = item 
print(customer_tax)