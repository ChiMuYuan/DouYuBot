# import sqlite3
#
# con = sqlite3.connect('C:\\Users\\\\Desktop\\Cookies.sqlite')
# cur = con.cursor()
# con.row_factory = sqlite3.Row
# # cur.execute("select * from sqlite_master where type='table'")
# sql = "SELECT * FROM 'cookies' where host_key= \"%s\""%("www.douyu.com")
# cur.execute(sql)
# res = cur.fetchall()
# print (type(res))
# for i in range(len(res)) :
#     print (res[i])

# -*- coding: utf-8 -*-

from ctypes import *
from ctypes.wintypes import DWORD
import sqlite3;

# cookieFile='C:\Users\username\AppData\Local\Google\Chrome\User Data\Default\Cookies';
cookieFile="C:\\Users\\**\\Desktop\\Cookies.sqlite"
hostKey="www.douyu.com";

LocalFree = windll.kernel32.LocalFree;
memcpy = cdll.msvcrt.memcpy;
CryptProtectData = windll.crypt32.CryptProtectData;
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

def encrypt(plainText):
    bufferIn = c_buffer(plainText, len(plainText));
    blobIn = DATA_BLOB(len(plainText), bufferIn);
    blobOut = DATA_BLOB();

    if CryptProtectData(byref(blobIn), u"python_data", None,
                       None, None, CRYPTPROTECT_UI_FORBIDDEN, byref(blobOut)):
        return getData(blobOut);
    else:
        raise Exception("Failed to encrypt data");

def decrypt(cipherText):
    bufferIn = c_buffer(cipherText, len(cipherText));
    blobIn = DATA_BLOB(len(cipherText), bufferIn);
    blobOut = DATA_BLOB();

    if CryptUnprotectData(byref(blobIn), None, None, None, None,
                              CRYPTPROTECT_UI_FORBIDDEN, byref(blobOut)):
        return getData(blobOut);
    else:
        raise Exception("Failed to decrypt data");

conn = sqlite3.connect(cookieFile);
c = conn.cursor();
sql = "select host_key, name, value, path,encrypted_value from cookies where host_key like \'%" + hostKey+"%\'";
c.execute(sql);

cookies = c.fetchmany(14);
c.close();

for row in cookies:
    dc = decrypt(row[4]);
    print( \
"""
host_key: {0}
name: {1}
path: {2}
value: {3}
encrpyted_value: {4}
""".format(row[0], row[1], row[2], row[3], dc));


