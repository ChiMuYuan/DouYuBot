from lxml import etree

a = "//*[@id=\"wp_news_w6\"]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/a"
t = open("C:/Users/ChiMu/Desktop/杂物/test/公告新闻.html", "r", encoding="utf8").read()

html = etree.HTML(t)
html_Data = html.xpath(a)
print(html_Data)
print(html_Data[0].text)
