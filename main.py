#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "Rob Spears (GitHub: Forty9Unbeaten)"


def add(x, y):
    """Add two integers. Handles negative values."""
    return sum([x, y])


def multiply(x, y):
    """Multiply two integers. Handles negative values"""

    def assure_positive(num):
        return -num if num < 0 else num

    negativeAnswer = False
    if (x < 0) is not (y < 0):
        negativeAnswer = True
    x = assure_positive(x)
    y = assure_positive(y)

    product = 0
    for i in range(0, y):
        product = add(product, x)

    return -product if negativeAnswer else product


def power(x, n):
    """Raise x to power n, where n >= 0"""
    power_result = 1
    for i in range(0, n):
        power_result = multiply(power_result, x)
    return power_result


def factorial(x):
    """Compute factorial of x, where x > 0"""
    fact = 1
    for i in range(2, x + 1):
        fact = multiply(fact, i)
    return fact


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    prev_num = 0
    next_num = 1
    fib_sum = 1
    for i in range(2, n):
        fib_sum = add(prev_num, next_num)
        prev_num = next_num
        next_num = fib_sum
    return fib_sum


if __name__ == '__main__':
    print('*** Addition of 2 + 4 ***')
    print(add(2, 4))
    print('*** Multiply 6 by -8 ***')
    print(multiply(6, -8))
    print('*** 2 to the power of 8 ***')
    print(power(3, 4))
    print('*** Factorial of 4 ***')
    print(factorial(4))
    print('*** 8th number in the Fibonacci sequence ***')
    print(fibonacci(8))
