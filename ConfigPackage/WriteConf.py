#Server
import configparser

def WConf(path, acf_username, acf_ltkid, acf_stk, room_id, nickname):
    oldfile = open(path + "DouYuDMS.ini", "r").readlines()
    shortfile = open(path + "DouYuDMS.ini", "w")
    for i in range(3):
        shortfile.write(oldfile[i])
    shortfile.write("\n")
    shortfile.close()
    conf = configparser.ConfigParser()
    conf.add_section("cookie")
    conf.add_section("douyuinfo")
    conf.set("cookie", "acf_username", acf_username)
    conf.set("cookie", "acf_ltkid", acf_ltkid)
    conf.set("cookie", "acf_stk", acf_stk)
    conf.set("douyuinfo", "room_id", room_id)
    conf.set("douyuinfo", "nickname", nickname)
    conf.write(open(path + "DouYuDMS.ini", "a"))