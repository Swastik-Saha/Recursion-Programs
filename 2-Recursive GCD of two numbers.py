"""
Euclid was a Greek mathematician who lived approximately 2,300 years ago. His
algorithm for computing the greatest common divisor of two positive integers, a and
b, is both efficient and recursive.
Write a program that implements Euclid’s algorithm and uses it to determine the
greatest common divisor of two integers entered by the user.
"""

def gcd(a, b):
    
    if a > b:
        larger = a
        smaller = b
    else:
        larger = b
        smaller = a
    
    remainder = larger % smaller
    
    if remainder == 0:
        return smaller
    else:
        return gcd(smaller, remainder)

if __name__ == "__main__":
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    gcd_nums = gcd(a, b)
    print(f"GCD of {a} and {b} is {gcd_nums}")
    
    