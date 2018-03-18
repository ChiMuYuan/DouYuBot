
def encodeBin(Str):
    code = [0xb1, 0x02, 0x00, 0x00]
    end = 0
    lenth = [4 + 4 + len(Str.encode("utf8")) + 1, 0, 0, 0]
    Str = bytearray(Str, "utf8")
    tot = bytearray()
    for i in lenth:
        tot.append(i)
    for i in lenth:
        tot.append(i)
    for i in code:
        tot.append(i)
    for i in Str:
        tot.append(i)
    tot.append(end)
    return tot

def decodeBin(data):
    mid = data.find(b'type@=chatmsg/')
    # cqid = data.find(b'type@=bc_buy_deserve/')
    # spid = data.find(b'type@=spbc/')
    if mid == 12:
        nick = bytearray()
        txt = bytearray()
        nid = data.index(b'nn@=')
        tid = data.index(b'txt@=')
        eid = data.index(b'/cid@=')
        for i in range(nid + 4, tid - 1):
            nick.append(data[i])
        for i in range(tid + 5, eid):
            txt.append(data[i])
        try:
            result = [nick.decode("utf8"), txt.decode("utf8")]
            return result
        except Exception:
            return ["", ""]
    return ["", ""]
