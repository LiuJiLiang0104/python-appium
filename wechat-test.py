#-*- coding: UTF-8 -*-

import os
import unittest
from time import sleep
from appium import webdriver

PATH = lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__), p)
)

class WechatTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['newCommandTimeout'] = '300'
        desired_caps['deviceName'] = 'YT4PQCY5ROS4CMKN'
        desired_caps['app'] = PATH('wechat-6.3.22.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        
        
    def tearDown(self):
        self.driver.quit()
        
        
    def test_login(self):
        sleep(3)
        # 点击登录
        el = self.driver.find_element_by_id('com.tencent.mm:id/c32')
        el.click()
        sleep(5)
        # 输入帐号和密码
        el = self.driver.find_element_by_id('com.tencent.mm:id/bho')
        el.send_keys('telephone')
        el = self.driver.find_element_by_id('com.tencent.mm:id/ew')
        el.send_keys('password')
        el = self.driver.find_element_by_id('com.tencent.mm:id/a6d')
        el.click()
        sleep(5)
        # 点击弹出框 否
        el = self.driver.find_element_by_id('com.tencent.mm:id/bhd')
        el.click()
        sleep(20)
        # 点击通讯录
        #el = self.driver.find_element_by_id('com.tencent.mm:id/bhj')
        el = self.driver.find_element_by_android_uiautomator('new UiSelector().text("通讯录")')
        el.click()
        sleep(3)
        # 点击公共号,打开公共号列表
        el = self.driver.find_element_by_id('com.tencent.mm:id/nv')
        el.click()
        
        # 打开单个公共号
        el = self.driver.find_element_by_android_uiautomator('new UiSelector().text("某个公共账号")')
        el.click()
        sleep(5)
        
        # 打开公共号设置
        el = self.driver.find_element_by_accessibility_id('聊天信息')
        el.click()
        sleep(5)
        
        # 查看历史消息
        el = self.driver.find_element_by_android_uiautomator('new UiSelector().text("查看历史消息")')
        el.click()
        sleep(3)
        
        # 打开更多
        el = self.driver.find_element_by_accessibility_id('更多')
        el.click()
        sleep(3)
        
        # 复制
        el = self.driver.find_element_by_android_uiautomator('new UiSelector().text("复制链接")')
        el.click()
        
        # 获取剪切板内容 还未实现

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WechatTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
