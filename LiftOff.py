# Lift Off
# Pawelski
# 10/7/2024
# Programming Fundamentals

import time

start = int(input("At what number do you want to start the count down? >> "))

count = start
while count > 0:
    print(count)
    time.sleep(1)
    count = count - 1
print("Lift off!")
