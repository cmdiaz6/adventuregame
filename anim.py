import time
import sys, random

animation = "|/-\\"

# notes: random.randint(111111111,999999999)
for i in range(100):
    time.sleep(0.1)
#    string = str(random.randint(111111111111111111111111,999999999999999999999999))
#    string += string + string
    string = str(random.randint(0,1))
    for i in range(100):
        string += str(random.randint(0,1))
    sys.stdout.write("\r" + string + "\n" + string)

print("\nYour roll has now been analyzed!")

def anitxt(i):
    animation = "|/-\\"
    string = ""
    for j in range(len(animation)):
        string += animation[(i+j) % len(animation)] + " "
    return string

for i in range(0):
    time.sleep(0.1)
    sys.stdout.write("\r" + anitxt(i) + " " + str(i) + "%")
    sys.stdout.flush()

print("\nEnd!")

