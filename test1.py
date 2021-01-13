import unittest
import requests

# 用接口测试进行查询
class Cpgl(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    # 正常输入全部查询
    def test_01(self):
        url = "http://123.57.140.190/manage/list_cp.php"

        payload = 'pro_name=%E7%94%98%E8%82%83%E5%9C%9F%E8%B1%86&cpbh=tudou001&cptxm=tudou001'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'PHPSESSID=nqnqkk4o88ijiobodpsaebimc1'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        a=response.text
        self.assertIn("甘肃土豆",a,msg="错误断言打印")

        # 模糊查询
    def test_02(self):
        url = "123.57.140.190:80"
        payload = 'pro_name=苹果'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'PHPSESSID=nqnqkk4o88ijiobodpsaebimc1'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        a=response.text
        self.assertIn("苹果",a,msg="断言错误被打印")
        # print(response.text)
    #     不存在编号查询
    def test_03(self):
        url = "http://123.57.140.190/manage/list_cp.php"

        payload = 'cpbh=kksdkh'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'PHPSESSID=nqnqkk4o88ijiobodpsaebimc1'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        a=response.text
        self.assertNotIn("kksdkh",a,msg="断言错误被答应")
if __name__ == '__main__':
    suite = unittest.TestSuite()  # 添加测试集
    suite.addTest(Cpgl("test_03"))  # 选择测试用例
    ru = unittest.TextTestRunner()  # 创建跑的测试集
    ru.run(suite)
