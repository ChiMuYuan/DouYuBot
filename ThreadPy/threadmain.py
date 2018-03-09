from threading import *
import time

global bool
bool = True

def test():
    global bool
    while bool:
        print("123")
        time.sleep(3)
        print(enumerate())

def threadmain():
    new = Thread(target=test, name="test1", daemon=False)
    new.start()
    print("threadmain end")
    print(enumerate())

threadmain()
if input() == "0":
    bool = False
print(bool)
