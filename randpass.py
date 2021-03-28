# Program: Random Password Generator
# Author: R
# Creation Date: 12-27-2020

#!/usr/bin/env python3 

import random
import string

def randStr(char = string.ascii_uppercase +
            string.ascii_lowercase + string.digits +
            string.punctuation, N=24):
    return ''.join(random.choice(char) for _ in range(N))

print(randStr())
