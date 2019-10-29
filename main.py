from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import numpy as np
from sympy.ntheory import factorint
from sympy import nextprime, prevprime
from genPrimes import generatePrimes
import math


def getCustKeys():
    q = generatePrimes(128,1)[0]
    p = generatePrimes(128,1)[0]
    n = q*p
    print(n)


def thirdCrack(modulo):
    '''currently 3 times faster than second method'''
    one,two = list(factorint(modulo))
    return one,two





















def secondCrack(modulo,maxruns=200):

    floor = math.sqrt(modulo)
    i = int(floor)
    high = i
    low = i
    j = 0
    while (j <= maxruns):

        high = nextprime(high)
        if low>3:
            low = prevprime(low)

        if int(np.mod(modulo,high)) == 0:

            return high,int(np.divide(modulo,high))

        elif int(np.mod(modulo,low)) == 0:
            return low,int(np.divide(modulo,low))
    j+=1

def firstCrack(modulo):
    '''
    Tests all odd numbers beginning at the square root of the modulo
    looks for when it equals 0

    Very buggy thus archived
    '''
    floor = math.sqrt(modulo)
    i = int(floor)

    while i > 0:
        temp = int(np.mod(modulo,i))

        if temp == 0:
            return i
        else:
            i-=2
