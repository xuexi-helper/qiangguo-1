# coding=utf-8

from selenium import webdriver
from PIL import Image
from io import BytesIO
import base64 as b64
import code  

def login():
    dr.get("https://pc.xuexi.cn/points/login.html")
    Iframe = dr.find_elements_by_tag_name('iframe')[2]
    dr.switch_to.frame(Iframe)
    # Qrcode = dr.find_element_by_css_selector(".login_content>.login_body>.login_qrcode>.login_qrcode_content>img").get_attribute("src")
    QrData = dr.find_element_by_css_selector(".login_qrcode_content>img").get_attribute("src")
    print QrData
    # QrStr = b64.b64decode(QrData.split(",")[-1])
    # QrImg = Image.frombytes(QrStr)
    # QrImg.show()
    dr.switch_to.default_content()
    raw_input()

def learn():
    dr.get("https://www.xuexi.cn/3695ce40a2f38ca24261ee28953ce822/9a3668c13f6e303932b5e0e100fc248b.html")
    link = dr.find_elements_by_css_selector(".word-item")
    for i in link:
        print i.text
    link[4].click()
    link[6].click()
    link[8].click()
    link[10].click()

    interp = code.InteractiveConsole(globals())  
    interp.interact("")

dr = webdriver.Chrome()
login()
learn()