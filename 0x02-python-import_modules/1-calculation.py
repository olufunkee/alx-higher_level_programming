#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    summ = add(a, b)
    subb = sub(a, b)
    prod = mul(a, b)
    quot = div(a, b)

    print("{} + {} = {}".format(a, b, summ))
    print("{} - {} = {}".format(a, b, subb))
    print("{} * {} = {}".format(a, b, prod))
    print("{} / {} = {}".format(a, b, quot))
