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

