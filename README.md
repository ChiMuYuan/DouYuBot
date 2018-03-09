# DouYuDM
斗鱼弹幕收集和发送
# 开发中

从ini读入配置文件，解析chrome浏览器的cookies为Sqlite存储，使用windll.crypt32.CryptUnprotectData解码

客户端将cookie和用户信息发送给Server服务端，Server写入文件完成，多线程维护验证成功