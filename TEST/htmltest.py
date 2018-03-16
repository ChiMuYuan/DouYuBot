
import time
time_str1 = "2018/03/09 15:38:59"
time_str2 = "2018/03/09 15:39:59"
tobj = time.strptime(time_str1, "%Y/%m/%d %H:%M:%S")
tobj2 = time.strptime(time_str2, "%Y/%m/%d %H:%M:%S")
tobj3 = time.mktime(time.localtime(time.time()))
tobj4 = time.time()
print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time())))