import configparser

class RConf:
    def __init__(self, path):
        conf = configparser.ConfigParser()
        conf.read_file(open(path + 'DouYuDM.ini', 'r'))
        self.cookiespath = conf.get('cookie', 'path')
        self.host_key = conf.get('cookie', 'host_key')
        self.room_id = conf.getint('douyuinfo', 'room_id')
        self.nickname = conf.get('douyuinfo', 'nickname')
        self.IP = conf.get('server', 'IP')
        self.PORT = conf.getint('server', 'PORT')

    def getcookiespath(self):
        return self.cookiespath

    def gethost_key(self):
        return self.host_key;

    def getroom_id(self):
        return self.room_id

    def getnickname(self):
        return self.nickname

    def getIP(self):
        return self.IP

    def getPORT(self):
        return self.PORT