import unittest
import time
from main import secondCrack,thirdCrack
from RSEfuncs import basicEncrypt, getMessage, advancedEncryptionCase
from genPrimes import generatePrimes


class TestStringMethods(unittest.TestCase):


    def test_basicEncrypt(self):

        message = 123456789
        modulus = 10142789312725007
        pub_exp = 5

        self.assertEqual(7487844069764171, basicEncrypt(message,pub_exp,modulus))

    def test_getMessage(self):

        modulus = 10142789312725007
        private_exp = 8114231289041741
        cypher_text = 7487844069764171

        self.assertEqual(123456789, getMessage(cypher_text,private_exp, modulus))



    def test_advancedEncryption(self):

        self.assertEqual(b'basic', advancedEncryptionCase('basic',1024))

    def test_advancedEncryption2(self):

        self.assertEqual(b'A little more advanced', advancedEncryptionCase('A little more advanced',2048))

    def test_genPrimes(self):
        x = generatePrimes(16,1)[0]
        output = True
        if x >= 2:
            for y in range(2,x):
                if not ( x % y ):
                    output = False
        else:
            output = False
        self.assertEqual(output, True)

    def test_factoring2(self):

        q = generatePrimes(16,1)[0]
        n = generatePrimes(16,1)[0]
        primeNum = q*n

        start = time.time()

        one,two = secondCrack(primeNum, 2000)
#        two = getSecondPrime(primeNum, one)

        elapsed = time.time()-start
        print('time for second method')
        print(elapsed)
        self.assertEqual(primeNum, one*two)

    def test_factoring3(self):

        q = generatePrimes(16,1)[0]
        n = generatePrimes(16,1)[0]
        primeNum = q*n

        start = time.time()

        one,two = thirdCrack(primeNum)

        elapsed = time.time()-start
        print('time for sympy method')
        print(elapsed)
        self.assertEqual(primeNum, one*two)

if __name__ == '__main__':
    unittest.main()