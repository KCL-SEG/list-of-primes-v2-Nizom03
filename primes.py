"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math
def primes(number_of_primes):
    if (number_of_primes==0 ):
        raise ValueError('A very specific bad thing happened.')
    if (number_of_primes<0 ):
        raise ValueError('A very specific bad thing happened.')
    list = []

    for num in range(2,number_of_primes):
            if (num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
                list.append(num)
                # print(num)

    return list
