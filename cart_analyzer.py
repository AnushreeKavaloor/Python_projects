from functools import reduce
cart = [("pen", 10), ("notebook", 50), ("eraser", 5), ("bag", 300), ("scale", 15)]

# 10% discount is given on every product using map() function
discounted = list(map(lambda x:(x[0],x[1]*0.9), cart))

# Highest-priced items are filtered using filter() 
highest_price = list(filter(lambda p:p[1]>=20, discounted))

# Total price of highest-priced products is calculated using reduce()
total_price = reduce(lambda a,b: a[1]+b[1], highest_price)

print(discounted)
print(highest_price)
print(total_price)
