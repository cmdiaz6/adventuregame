import time
import sys

animation = "|/-\\"

def anitxt(i):
    animation = "|/-\\"
    string = ""
    for j in range(len(animation)):
        string += animation[(i+j) % len(animation)] + " "
    return string

for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r" + anitxt(i) + " " + str(i) + "%")
    sys.stdout.flush()

print("End!")

