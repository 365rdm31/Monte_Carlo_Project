from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import numpy as np

def basicEncrypt(message, public_exp, modulo):
    '''
    takes a message and encrpyts using a public key consisting of a public_exp and modulo
    '''
    cypher = pow(message, public_exp, modulo)

    return cypher

def getMessage(cypher, private_exp, modulo):
    '''
    returns the original unencrypted message by applying a private exponenet
    and a special private_exp which = public_exp^-1 mod (p-1)*(q-1)
    '''
    message = pow(cypher,private_exp,modulo)

    return message

def advancedEncryptionCase(message,key_length = 1024):
    #turns original message into bytes
    msg = bytes(message,encoding='ascii')

    #generates public and private keys
    keyPair = RSA.generate(key_length)

    pubKey = keyPair.publickey()
#    print(f"Public key:  (n={int(pubKey.n)}, e={int(pubKey.e)})")
#    pubKeyPEM = pubKey.exportKey()
#    print(pubKeyPEM.decode('ascii'))

#    print(f"Private key: (n={int(pubKey.n)}, d={int(keyPair.d)})")
#    privKeyPEM = keyPair.exportKey()
#    print(privKeyPEM.decode('ascii'))

    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(msg)
#    print("Encrypted:", binascii.hexlify(encrypted))

    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted)
#    print('Decrypted:', decrypted)
    return(decrypted)