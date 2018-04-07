import time

WAIT = False

def setWAIT(newW):
    global WAIT
    WAIT = newW

def getWAIT():
    global WAIT
    return WAIT

def resetWAIT():
    time.sleep(30)
    global WAIT
    WAIT = True