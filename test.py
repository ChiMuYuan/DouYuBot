import test2
from threading import *
import test3


tt = Thread(target = test2.testtt, daemon = False)
tt.start()
print(test3.getbool())
if input() == "0":
    test3.setbool(False)
print(test3.getbool())
print("end")