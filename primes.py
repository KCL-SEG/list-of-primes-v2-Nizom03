"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math
def primes(number_of_primes):
    if (number_of_primes==0 ):
        raise ValueError('A very specific bad thing happened.')
    if (number_of_primes<0 ):
        raise ValueError('A very specific bad thing happened.')
    list = []

    for num in range(2,100):
        if all(num%i!=0 for i in range(2,num)):
           print (num)
           if (len(list)<number_of_primes):
               list.append(num)

    return list
