# Monte_Carlo_Project
The main focus of this project is on the pursuit of cracking 1024 bit RSE encrption

The goal is to implement some type of Monte Carlo analysis in order to
build a type of model of the system

RSE Encryption:

Consists of a public key and a private key

public key has a prime number and a public exponent

method rse_encryption works as such

given:
 a message to encrypt, a modulus (combo of two unique primes), and a public exponent

calculates:
tmp = message ** public_exponent
cypherText = one mod modulus

returns

RSE Dencryption:

given:
public prime
cypher text
private prime

calculates:
tmp = cypher ** private prime

message = cypher mod publicPrime

returns original message


Primes:

using Miller-Rabin Primality test to generate


method generate primes

given:
bit length n
k number of primes to generate


calculates:
number of necessary steps:
	necessary_steps = math.floor( math.log(2**n) / 2 )

n random bits as first number to test for primality
	x = random.getrandbits(n)

stops when if condition met
	if miller_rabin_primality_test(x, s=7)

returns primes

method miller_rabin primality test

I don't understand this check but it returns primes

return

to be implemented
Number sieve algorithm for cracking keys
