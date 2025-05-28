import time
import os

for i in range(20):
    os.system('cls' if os.name == 'nt' else 'clear')  # clear screen
    print(" " * i + "→ Moving right →")
    time.sleep(0.1)
