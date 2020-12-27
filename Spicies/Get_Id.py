from selenium.webdriver.chrome.options import Options
import requests
import re
from selenium import webdriver
from time import sleep

def get_Id(name):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chromedriver = "C://Users//yezi//AppData//Local//Google//Chrome//Application//chromedriver.exe"


    #name = input("请输入歌曲名字")
    
    url_1 = 'https://music.163.com/#/search/m/?s=' + name + '&type=1'

    #初始化browser对象
    browser = webdriver.Chrome(chromedriver, options=chrome_options)
    #访问url
    browser.get(url=url_1)
    #网页中有iframe框架，进行切换
    browser.switch_to.frame('g_iframe')
    #等待0.5秒
    sleep(0.5)
    #抓取页面信息
    page_text = browser.execute_script("return document.documentElement.outerHTML")
    #退出浏览器
    browser.quit()

    ex1 = '<a.*?id="([0-9]*?)"'
    id_list = re.findall(ex1,page_text,re.M)[::2]

    return id_list[0]







