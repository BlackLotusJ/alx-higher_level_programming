#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    a=10
    b=5
    print("{:d}".format(calc.add(a, b)))
    print("{:d}".format(calc.sub(a, b)))
    print("{:d}".format(calc.mul(a, b)))
    print("{:d}".format(calc.div(a, b)))
