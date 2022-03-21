import RPi.GPIO as gp
import time
def d2b(a):
    return[int(bit) for bit in bin(a)[2:].zfill(8)]
def ans(aa):
    print(round(3.3*(int(aa)/255),2),"B")
dac = [26,19,13,6,5,11,9,10]
gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)
check = 0
flag = True
try:
    print("Input program number:")
    n = int(input())
    if(n == 1):
        while flag:
            print("enter num or write !stop to end:")
            inn = input()
            if inn !="!stop":
                gp.output(dac, d2b(int(inn)))
                ans(inn)
            else:
                break
    else:
        p = float(input("enter period in milisecounds:"))
        p = p/100
        while True:
            for i in range(256):
                gp.output(dac,d2b(i))
                time.sleep(p)
            for i in range(255,1, -1):
                gp.output(dac,d2b(i))
                time.sleep(p)
            print("want conti(y or n)")
            a = input()
            if(a =="n"): break
except ValueError:
    print("incorrect input")
except NameError:
    print("not decimal")
except Exception:
    print("erorr")
finally:
    gp.output(dac,0)
    gp.cleanup()
