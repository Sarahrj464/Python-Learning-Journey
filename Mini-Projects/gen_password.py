import random

import string

pass_len=10
charValue = string.ascii_letters + string.digits + string.punctuation

# using list comprehension
password="".join([random.choice(charValue) for i in range(pass_len)])


# password=""
# for i in range(pass_len):
#   password+=random.choice(charValue)
  
print("Random password:",password)