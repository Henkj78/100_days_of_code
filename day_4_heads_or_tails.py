# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

# **Important**, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

import random

coin = random.randint(0, 1)

if coin == 0:
    print("Heads")
else:
    print("Tails")