product=1
def product_of_numbers(num):
    global product
    for i in str(num):
        product=int(i)*product

    return product        

print(product_of_numbers(1234))



def product_of_numbers_v2(num):
    result = 1
    for digit in str(num):
        result *= int(digit)
    return result

print(product_of_numbers_v2(1234))