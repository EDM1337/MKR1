def fileRead(filename):
    product_price = {}

    with open(filename, 'r') as file:
        for line in file:
            product, date, price = line.strip().split(", ")
            price = int(price)
            year, month = date.split("-")

            if product in product_price:
                product_price[product].append((month, price))
            else:
                product_price[product] = [(month, price)]

    return product_price

def printPrice(product_price):
    for product, prices in product_price.items():
        print(product + ":")
        monthly_prices = {}
        for month, price in prices:
            if month in monthly_prices:
                monthly_prices[month].append(price)
            else:
                monthly_prices[month] = [price]

        for month, prices in monthly_prices.items():
            if len(prices) > 1:
                price_change = prices[-1] - prices[0]
                print(month + ": " + str(price_change))



