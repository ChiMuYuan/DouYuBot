# Client/Server
import configparser


class RCConf:
    def __init__(self, path):
        conf = configparser.ConfigParser()
        conf.read_file(open(path + 'DouYuDMC.ini', 'r'))
        self.IP = conf.get('server', 'IP')
        self.PORT = conf.getint('server', 'PORT')
        self.cookiespath = conf.get('cookie', 'path')
        self.host_key = conf.get('cookie', 'host_key')
        self.room_id = conf.getint('douyuinfo', 'room_id')
        self.nickname = conf.get('douyuinfo', 'nickname')

class RSConf:
    def __init__(self, path):
        conf = configparser.ConfigParser()
        conf.read_file(open(path + 'DouYuDMS.ini', 'r'))
        self.IP = conf.get('server', 'IP')
        self.PORT = conf.getint('server', 'PORT')
        self.acf_username = conf.get('cookie', 'acf_username')
        self.acf_ltkid = conf.get('cookie', 'acf_ltkid')
        self.acf_stk = conf.get('cookie', 'acf_stk')
        self.room_id = conf.getint('douyuinfo', 'room_id')
        self.nickname = conf.get('douyuinfo', 'nickname')
