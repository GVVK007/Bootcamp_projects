#Python 3 code to convert string to different hashing algorithms

import hashlib

#print(hashlib.algorithms_available)

# Taking string as input

Text = input('Enter any Text:')
  
# Then converting Text  to different hashes

sha384_hash = hashlib.sha384(Text.encode())

sha1_hash = hashlib.sha1(Text.encode())

sha224_hash = hashlib.sha224(Text.encode())


blake2s_hash = hashlib.blake2s(Text.encode())



# printing the equivalent hashing value.

print('SHA384 HASH : ',end='')
print(sha384_hash.digest())

print('SHA1 HASH : ',end='')
print(sha1_hash.digest())

print('SHA224 HASH : ',end='')
print(sha224_hash.digest())

print('BLACK2S HASH : ',end='')
print(blake2s_hash.digest())


