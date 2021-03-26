def calculate(data):
    profit = (data["price"] - data["cost"]) * data["inventory"]
    return int(round(profit))


test_cases = [
    {"cost": 32.67, "price": 45.00, "inventory": 1200},
    {"cost": 0, "price": 2, "inventory": 100},
    {"cost": 10, "price": 8, "inventory": 100},
    {"cost": 12.56, "price": 12.99, "inventory": 1000},
    {"cost": 50, "price": 72, "inventory": 0},
    {"cost": 100, "price": 90, "inventory": 0},
    {"cost": 30.58, "price": 29.74, "inventory": 598},
    {"cost": 46841.36, "price": 78241.12, "inventory": 6454135},
    {"cost": 0, "price": 0, "inventory": 0},
    {"cost": 1000, "price": 1000, "inventory": 100},
]

i = 1
for test in test_cases:
    print("Case {0}:".format(i))
    print("Info {0}".format(test))
    print("")
    print("Profit: ${0}".format(calculate(test)))
    print("")
    i = i + 1