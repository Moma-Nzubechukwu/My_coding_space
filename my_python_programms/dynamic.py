import time
import sys

for i in range(100):
    sys.stdout.write(f"\rCount: {i}")
    sys.stdout.flush()
    time.sleep(0.05)
print()
