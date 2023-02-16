print('hi this project about time')
import datetime
import random
import time
time_minute = datetime.datetime.today().minute
random_time = random.randint(2,3)
for i in range(100):
    time.sleep(random_time)
    time_minute = datetime.datetime.today().minute
    odd_numbers = list(range(0,61,2))
    if time_minute in odd_numbers:
        print('odd')
    else:
        print('not odd')
print('bye bye')
print(mojex)
