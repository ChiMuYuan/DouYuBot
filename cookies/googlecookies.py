#Client
# -*- coding: utf-8 -*-

from ctypes import *
from ctypes.wintypes import DWORD
import sqlite3;
from ConfigPackage import *

LocalFree = windll.kernel32.LocalFree;
memcpy = cdll.msvcrt.memcpy;
CryptUnprotectData = windll.crypt32.CryptUnprotectData;
CRYPTPROTECT_UI_FORBIDDEN = 0x01;

class DATA_BLOB(Structure):
    _fields_ = [("cbData", DWORD), ("pbData", POINTER(c_char))];

def getData(blobOut):
    cbData = int(blobOut.cbData);
    pbData = blobOut.pbData;
    buffer = c_buffer(cbData);
    memcpy(buffer, pbData, cbData);
    LocalFree(pbData);
    return buffer.raw;

def decrypt(plainText):
    bufferIn = c_buffer(plainText, len(plainText));
    blobIn = DATA_BLOB(len(plainText), bufferIn);
    blobOut = DATA_BLOB();

    if CryptUnprotectData(byref(blobIn), u"python_data", None, None, None, CRYPTPROTECT_UI_FORBIDDEN, byref(blobOut)):
        return getData(blobOut);
    else:
        raise Exception("Failed to encrypt data");


def getcookies():
    RC = ReadConf.RCConf("./ConfigPackage/")
    cookiesfile = RC.getcookiespath()
    host_key = RC.gethost_key()
    conn = sqlite3.connect(cookiesfile)
    cur = conn.cursor()
    sql = "select name, encrypted_value from cookies where host_key like \'%" + host_key + "%\'"
    cur.execute(sql)
    sqlresult = cur.fetchall()
    cur.close()
    conn.close()
    cookies = []
    for sqlr in sqlresult:
        if sqlr[0] == "acf_username" or sqlr[0] == "acf_ltkid" or sqlr[0] == "acf_stk" :
            cookies.append(sqlr[0])
            cookies.append(decrypt(sqlr[1]).decode())
    return cookies