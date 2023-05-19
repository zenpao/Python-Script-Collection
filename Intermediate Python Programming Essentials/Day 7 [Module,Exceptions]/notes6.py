#javier_jentzenpaolo_day
#Philippine Statistics Authortiy - Philippine Identification System (Benguet)
#Cordillera Administrative Region
#Information Systems Analyst I (COSW)

#IMPORT RANDOM MODULE
import random

print(random.randrange(1,10))

print("\n")

#CHECKED EXCEPTION
#ERROR EXCEPTION
#RUNTIME EXCEPTION

try:
    a = 15
    if a <= 17:
        raise Exception
except Exception:
    print("Error")
else:
    print("No error")
finally:  # executes regardless
    print("No error indeed\n")

try:
    file = open('filename.txt')
except Exception:
    print('Error')
else:
    print('No Error')
finally:
    file.close()