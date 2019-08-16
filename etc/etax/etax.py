#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
class EtaxSpider():
    def __init__(self):
        option = ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_argument('--proxy-server=192.168.2.48:8080')
        option.add_experimental_option('excludeSwitches', ['enable-automation']) 
        # option.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        self.driver = Chrome(options=option,executable_path="/home/domizzi/dev/pyincome/etc/etax/chromedriver",desired_capabilities=capabilities)

        

    def get_slider(self):
        while True:
            try:
                slider = self.driver.find_element_by_id("nc_1_n1z")
                print "slider",slider
                break
            except:
                time.sleep(0.5)
                print "wait"
        return slider
    def login(self,url):
        self.driver.get(url)
        assert u"广东省电子税务局" in self.driver.title
        # driver.maximize_window()  #最大化
        time.sleep(1)

        for i in range(20):      
            try:
                content = self.driver.find_element_by_class_name('layui-layer-btn1')
                content.click()
            except :
                pass
            slide = self.get_slider()
            action = ActionChains(self.driver)
            action.click_and_hold(slide) # 鼠标左键按住span
   
            num = 0
            while 1:
                rn = random.randint(1,100)
                print num
                num=rn+num
                action.move_by_offset(num, 0) # 向右拖动258像素完成验证

                if 290 > num:
                    break
            action.perform()
            # time.sleep(1)
            action.reset_actions() # 页面进行了刷新，需要清除action之前存储的elements
            # time.sleep(1)
            
            time.sleep(random.randint(3,8))
            self.driver.refresh()
        elem = self.driver.find_element_by_id("userName")
        elem.clear()
        elem.send_keys(u"鑫视野")
        elem = self.driver.find_element_by_id("passWord")
        elem.clear()
        elem.send_keys("Wang13632392307")
        time.sleep(1)  

if __name__=="__main__":
    etaxSpider = EtaxSpider()
    etaxSpider.login("https://www.etax-gd.gov.cn/sso/login?service=https://www.etax-gd.gov.cn/xxmh/html/index_login.html?bszmFrom=1&t="+str(int(time.time())))