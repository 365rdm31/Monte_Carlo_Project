from __future__ import print_function
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import numpy as np
from sympy.ntheory import factorint
from sympy import nextprime, prevprime
from genPrimes import generatePrimes
import math
import time
import gmpy2

def getCustKeys():
    q = generatePrimes(16,1)[0]
    p = generatePrimes(16,1)[0]
    n = q*p
    print(n)
    return int(n)

def thirdCrack(modulo):
    '''currently 3 times faster than second method'''
    one,two = list(factorint(modulo))
    return one,two

def sieve(limit=1000000):
    '''credit to:
    https://stackoverflow.com/questions/2897297/speed-up-bitstring-bit-operations-in-python

    Returns a generator that yields the prime numbers up to limit.'''

    # Increment by 1 to account for the fact that slices do not include
    # the last index value but we do want to include the last value for
    # calculating a list of primes.
    sieve_limit = gmpy2.isqrt(limit) + 1
    limit += 1

    # Mark bit positions 0 and 1 as not prime.
    bitmap = gmpy2.xmpz(3)

    # Process 2 separately. This allows us to use p+p for the step size
    # when sieving the remaining primes.
    bitmap[4 : limit : 2] = -1

    # Sieve the remaining primes.
    for p in bitmap.iter_clear(3, sieve_limit):
        bitmap[p*p : limit : p+p] = -1

    return bitmap.iter_clear(2, limit)

def sieveCrack(modulo):
    floor = int(modulo/2)
    allPrimes = list(sieve(floor))
    length = len(allPrimes)
    for i in range(length):
        for j in range(length):

            tmp = allPrimes[length-i-1]*allPrimes[length-j-1]
#            print(tmp, modulo)

            if tmp == modulo:
                i = length
                return allPrimes[length-i-1],allPrimes[length-j-1]

            if tmp < modulo:
                j = len(allPrimes)


#sieveCrack(10142789312725007)
modulo = getCustKeys()
#sieveCrack(modulo)
result = list(sieve(modulo))
tmp = thirdCrack(modulo)
print(tmp)
print(result.index(tmp[0]))
print(result.index(tmp[1]))
#if __name__ == "__main__":
#    start = time.time()
#    result = list(sieve(1000000000))
#    print(time.time() - start)
#    print(len(result))



