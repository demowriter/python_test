#coding:utf-8
import unittest
from selenium import webdriver
import time

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("开始测试")
    @classmethod
    def tearDownClass(cls):
        print("结束测试")
    def setUp(self):
        print("开始单个测试用例")
    def tearDown(self):
        print("结束单个测试用例")
        # 定义登录方法
    def login(self, username, password):
        self.dr = webdriver.Chrome()
        self.dr.get('https://passport.cnblogs.com/user/signin')  # cnblog登录页面
        self.dr.find_element_by_id('input1').send_keys(username)
        self.dr.find_element_by_id('input2').send_keys(password)
        self.dr.find_element_by_id('signin').click()

    def test_login_success(self):
        '''用户名、密码正确'''
        self.login('木xxxx', 'sxxxxx')  # 正确用户名和密码
        time.sleep(10)              #这里等待10秒的原因是由于cnblog存在验证机制，不想在验证码上花过多时间写代码，博主在等待时间手动处理。
        link = self.dr.find_element_by_id('lnk_current_user')
        self.assertTrue('木秀于林' in link.text)  # 用assertTrue(x)方法来断言  bool(x) is True 登录成功后用户昵称在lnk_current_user里

    def test_login_pwd_error(self):
        '''用户名正确、密码不正确'''
        self.login('木秀xxx', 'pwerror')  # 正确用户名，错误密码
        time.sleep(10) #这里等待10秒的原因是由于cnblog存在验证机制，不想在验证码上花过多时间写代码，博主在等待时间手动处理。
        error_message = self.dr.find_element_by_id('tip_btn').text
        self.assertIn('用户名或密码错误', error_message)  # 用assertIn(a,b)方法来断言 a in b  '用户名或密码错误'在error_message里
        self.dr.get_screenshot_as_file("F://PyCharm 2018.2.2//test_result//login_pwd_error.jpg")

    def test_login_pwd_null(self):
        '''用户名正确、密码为空'''
        self.login('木秀xxx', '')  # 密码为空
        error_message = self.dr.find_element_by_id('tip_input2').text
        self.assertEqual(error_message, '请输入密码')  # 用assertEqual(a,b)方法来断言  a == b  请输入密码等于error_message
        self.dr.get_screenshot_as_file("F://PyCharm 2018.2.2//test_result//login_pwd_null.jpg")

    def test_login_user_error(self):
        '''用户名错误、密码正确'''
        self.login('usernameerror', 'sxxxxxxx')  # 密码正确，用户名错误
        time.sleep(10)  #这里等待10秒的原因是由于cnblog存在验证机制，不想在验证码上花过多时间写代码，博主在等待时间手动处理。
        error_message = self.dr.find_element_by_id('tip_btn').text
        self.assertIn('用户名或密码错误', error_message)  # 用assertIn(a,b)方法来断言 a in b
        self.dr.get_screenshot_as_file("F://PyCharm 2018.2.2//test_result//login_user_error.jpg")

    def test_login_user_null(self):
        '''用户名为空、密码正确'''
        self.login('', 'sunsea1.')  # 用户名为空，密码正确
        error_message = self.dr.find_element_by_id('tip_input1').text
        self.assertEqual(error_message, '请输入登录用户名')  # 用assertEqual(a,b)方法来断言  a == b
        self.dr.get_screenshot_as_file("F://PyCharm 2018.2.2//test_result//login_user_null.jpg")

if __name__=="__main__":
    unittest.main()