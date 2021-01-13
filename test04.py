import unittest
import requests

# 用接口测试进行查询
class Cpgl(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    # 正常输入全部查询
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
