# coding=utf-8

from selenium import webdriver
from PIL import Image
from io import BytesIO
import base64 as b64
import code
import time
import random

class XueXiQiangGuo:
    def __init__(self, NewsNum, NewsTime):
        self.NewsNum = NewsNum
        self.NewsTime = NewsTime
        self.dr = webdriver.Chrome()

    def login(self):
        self.dr.get("https://pc.xuexi.cn/points/login.html")
        Iframe = self.dr.find_elements_by_tag_name('iframe')[2]
        self.dr.switch_to.frame(Iframe)
        # QrData = self.dr.find_element_by_css_selector(".login_content>.login_body>.login_qrcode>.login_qrcode_content>img").get_attribute("src")
        QrData = self.dr.find_element_by_css_selector(".login_qrcode_content>img").get_attribute("src")
        # print QrData
        # QrStr = b64.b64decode(QrData.split(",")[-1])
        # QrImg = Image.frombytes(QrStr)
        # QrImg.show()
        self.dr.switch_to.default_content()
        raw_input()

    def learn(self):
        self.dr.get("https://www.xuexi.cn/3695ce40a2f38ca24261ee28953ce822/9a3668c13f6e303932b5e0e100fc248b.html")
        link = self.dr.find_elements_by_id("Ca4gvo4bwg7400")
        print "学习新闻:"
        time.sleep(10) 
        for i in range(0,self.NewsNum):
            print link[i].text
            link[i].click()   
            time.sleep(10)   
        MainPage = self.dr.current_window_handle
        AllPage = self.dr.window_handles
        # LearnPage = {}
        for i in AllPage:
            if i != MainPage:
                self.dr.switch_to_window(i)
                # LearnPage[i] = self.dr.execute_script('return document.body.scrollHeight')
                self.dr.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(self.NewsTime*60)

        interp.interact("")

    def quit(self):
        self.dr.quit()

if __name__ == "__main__":
    interp = code.InteractiveConsole(globals())
    # 每次打开6篇文章,打开4分钟
    zz = XueXiQiangGuo(6,4)
    zz.login()
    zz.learn()
    # zz.quit()