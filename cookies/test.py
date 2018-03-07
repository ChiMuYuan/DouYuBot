# -*- coding: utf-8 -*-

from ctypes import *
from ctypes.wintypes import DWORD
import sqlite3;

cookieFile="C:\\Users\\ChiMu\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies"
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

cookies = c.fetchall();
c.close();

for row in cookies:
    dc = decrypt(row[4]);
    print('name: {0} encrpyted_value: {1}'.format(row[1], dc));


