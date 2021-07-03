#Python 3 code to convert string to md5 hashing

import hashlib

# Taking string as input

Text = input('Enter any Text:')
  
# Then converting Text  to md5()

md5_hash = hashlib.md5(Text.encode())
  
# printing the equivalent md5 hashing value.
print('MD5 HASH : ',end='')
print(md5_hash.digest())
