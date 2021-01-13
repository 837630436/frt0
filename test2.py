import unittest
import requests
from selenium import webdriver
import time
# 导登录函数包
from config.login1 import DL
a=DL()
class Cpgl(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        a.login()
    @classmethod
    def tearDown(self):
        time.sleep(15)
        # a.we.close()
        # a.we.quit()
 # 产品管理-产品管理
    # #    正常查询,s输入全部，单个查询
    # def test_01(self):
    #     a.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()#产品管理
    #     a.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()#产品管理
    #     a.we.find_element_by_class_name("form-control").send_keys("山药")
    #     a.we.find_element_by_name("cpbh").send_keys("334969")
    #     a.we.find_element_by_name("cptxm").send_keys("31929")
    #     a.we.find_element_by_css_selector("[type='submit']").click()
    #     zs = a.we.find_element_by_xpath("/html/body/section/section/section/form/div/div/section/table/tbody/tr/td[5]").text
    #     self.assertEqual(zs, "334969", msg="断言错误被打印")
        # 模糊查询
    def test_02(self):
        a.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()  # 产品管理
        a.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()  # 产品管理
        a.we.find_element_by_class_name("form-control").send_keys("苹果")
        a.we.find_element_by_css_selector("[type='submit']").click()
        time.sleep(3)
        zs = a.we.find_element_by_xpath(
            "/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[4]/a").text
        # print(zs)
        self.assertIn("苹果", zs, msg="断言错误被打印")

    # 编辑修改产品
    def test_03(self):
        a.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()  # 产品管理
        a.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()  # 产品管理
        a.we.find_element_by_link_text("编辑").click()
        a.we.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input").clear()
        a.we.find_element_by_xpath(
            "/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input").send_keys("删单")
        a.we.find_element_by_name("cpbh").clear()
        a.we.find_element_by_name("cpbh").send_keys("kskkks00099")
        a.we.find_element_by_name("cptxm").clear()
        a.we.find_element_by_name("cptxm").send_keys("0000kskkks00099")
        # 无法对产品描述进行清空在修改造作******
        # a.we.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[8]/div/div/div[2]/iframe").clear()
        # a.we.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[8]/div/div/div[2]/iframe").send_keys("kskdjgidfghiujfdhjiuhjiuf")
        a.we.find_element_by_css_selector("[type='submit']").click()
        zs=a.we.find_element_by_xpath("/html/body/div[3]/div").text
        self.assertEqual(zs, "产品更新成功！", msg="断言错误被打印")

        # 删除
    # @unittest.skip("taio")
    def test_04(self):#单个删除
        a.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()  # 产品管理
        a.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()  # 产品管理
        a.we.find_element_by_xpath("/html/body/section/section/section/form/div/div/section/table/tbody/tr[11]/td[8]/span").click()
        a.we.find_element_by_xpath(
            "/html/body/div[4]/div[3]/a[1]").click()
        # h=a.we.switch_to_alert()
        # h.accept()#弹出确认删除
        zs = a.we.find_element_by_xpath("/html/body/div[3]/div").text
        self.assertEqual(zs, "产品删除成功！", msg="断言错误被打印")
    def test_05(self):#预览
        a.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()  # 产品管理
        a.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()  # 产品管理
        a.we.find_element_by_xpath("/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[7]/span").click()
        a.we.find_element_by_xpath("/html/body/div[4]/span[1]/a").click()

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()  # 添加测试集
    suite.addTest(Cpgl("test_06"))  # 选择测试用例
    ru = unittest.TextTestRunner()  # 创建跑的测试集
    ru.run(suite)