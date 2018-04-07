#
# import time
# from datetime import datetime
# time_str1 = "2018/03/09 15:38:59"
# time_str2 = "2018/03/09 15:39:59"
# tobj = time.strptime(time_str1, "%Y/%m/%d %H:%M:%S")
# tobj2 = time.strptime(time_str2, "%Y/%m/%d %H:%M:%S")
# tobj3 = time.mktime(time.localtime(time.time()))
# tobj4 = time.time()
#
# print(time.strftime("%H:%M:%S", time.localtime(time.time())))
# print(tobj)
# print(tobj2)
# print(int(tobj3))
# print(int(tobj4))
# print(type(datetime.now()))
import time, datetime


def gettime():
    for x in range(24):
        a = datetime.datetime.now().strftime("%Y-%m-%d") + " %2d:00:00" % x

        timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")

        timeStamp = int(time.mktime(timeArray))
        print(timeStamp)
        print(timeStamp % 1800)


if __name__ == "__main__":
    gettime()