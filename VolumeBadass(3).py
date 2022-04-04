import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
dac = [26, 19,13, 6, 5, 11, 9, 10]
leds = [21,20,16, 12, 7, 8,25,24]
g =  [1,0,0,0,0,0,0,0]
comp = 4
tr = 17
MVolt = 3.3
bitt = 8
level = 2 ** bit
volt = 0

gp.setup(dac, gp.OUT)
gp.setup(tr, gp.OUT, initial = 1)
gp.setup(comp, gp.IN)

def out(g):
    return g[0]* 128 + g[1]*64+ g[2]*32 + g[3]*16+g[4]*8+g[5]*4+g[6]*2+g[7]*1 + g[8]* 0

def d2b(v):
    return [int(bit) for bit in bin(v)[2:].zfill(8)]
def adc():
    g = [0,0,0,0,0,0,0,0]
    for i in range(bitt):
        g[i] = 1
        gp..output(dac,g)
        time.sleep(0.001)
        cV = gp.output(comp)
        if cV:
            g[i] = 1
        else:
            g[i] = 0
    return out(g) 
flag = True
try:
    while flag:
        voltage =  adc()
        print("voltage meaning ", voltage*MVolt/level, "dec", voltage)
        n = round(bitt/level*voltage)
        print(n)
        gp.output(leds, d2b(2**n-1))
        time.sleep(0.2)
except KeyBoardInterrupt:
    print("---------------Emergency stop---------------")
finally:
    gp.output(dac, 0)
    gp.output(tr, 0)
    gp.cleanup()