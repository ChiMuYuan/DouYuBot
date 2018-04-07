import time, uuid, hashlib, socket
from PyBG import DouYucode
from ConfigPackage import ReadConf

def senddamu(txt):
    RC = ReadConf.RSConf("./ConfigPackage/")
    SocketSDM = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SocketSDM.connect("119.90.49.89", 8092)
    timenow = str(time.time())
    uuidnow = str(uuid.uuid4()).replace("-", "").upper()
    MD5 = hashlib.md5()
    MD5.update((timenow + "7oE9nPEG9xXV69phU31FYCLUagKeYtsF" + uuidnow).encode("utf8"))
    vknow = MD5.hexdigest()
    loginInfo = "type@=loginreq/username@=" + RC.acf_username + "/ct@=0/password@=/roomid@=" + RC.room_id + "/devid@=" + uuidnow + "/rt@=" + timenow + "/vk@=" + vknow + "/ver@=20150929/aver@=2017073111/ltkid@=" + RC.acf_ltkid + "/"
    SocketSDM.sendall(DouYucode.encodeBin(loginInfo))
    danmu = "type@=chatmessage/receiver@=0/content@=" + txt + "/scope@=/col@=0/pid@=/p2p@=0/nc@=0/rev@=0/ifs@=0/"
    SocketSDM.sendall(DouYucode.encodeBin(danmu))