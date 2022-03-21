import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
gp.setup(22, gp.OUT)

ledd = [21,20,16,12,7,8,25,24]
dac = [26,19,13,6,5,11,9,10]
gp.setup(dac, gp.OUT)
gp.setup(ledd, gp.OUT)
try:
    while True:
        inn = input("green or blue or aux:")
        if(inn == "green"):
            p = gp.PWM(21, 1000)
            p.start(0)
        elif(inn == "aux"):
            p = gp.PWM(22, 1000)
            p.start(0)
        elif(inn == "blue"):
            p = gp.PWM(26, 1000)
            p.start(0)
        else:
            print("INPUT CRITICAL ERROR TRY AGAIN")
            for i in range(15):
                gp.output(dac, 1)
                time.sleep(0.1)
                gp.output(dac, 0)
                gp.output(ledd, 1)
                time.sleep(0.1)
                gp.output(ledd, 0)
            continue
        inn = input("enter or !stop:")
        if(inn =="!stop"): break
        inn = int(inn)
        p.ChangeDutyCycle(inn)
        print("out", 3.3*inn/100)
finally:
    gp.cleanup()