#Original code from the tutorial 10 
def calculate_price(price, order):
    try:
        price = {'book': 10.0, 'magazine': 5.5, 'newspaper': 2.0}
        for i in price:
            order1 = {'book': 10}
            order2 = {'book': 1, 'magazine': 3}
            order3 = {'magazine': 5, 'book': 10}
            result = price - order1
            result2 = price - order2
            result3 = price - order3
            assert(95 == calculate_price(price, order1))
            assert(26.5 == calculate_price(price, order2))
            assert(114.75 == calculate_price(price, order3))
    except (ValueError, TypeError):
        print("Number of books must be an integer: ")
    else:
        print(result)


print(calculate_price(5, 1))