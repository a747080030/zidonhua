import seldom
from seldom import Seldom, data
from seldom import Steps
from seldom import testdata
from seldom.db_operation import MySQLDB








# class TestRequest(seldom.TestCase):
#     """api test case"""
#     def start(self):
#         self.url=f"{Seldom.base_url}/api/v1/login/"
#
#     @data([
#         ("admin", "admin"),
#         ("admin", "admin123456")
#     ])
#     def test_login(self,username,password):
#         self.post(self.url,data={"username":username,"password":password})
#         self.assertPath("success", True)
#         Steps(desc="百度搜索").open("http://www.baidu.com",).find("#kw").type("seldom").find("#su").click()
#         Session = self.Session()
    
    # def start(self):
    #     self.base_url = "http://httpbin.org"
    #
    # def test_put_method(self):
    #     self.put(f'{self.base_url}/put', data={'key': 'value'})
    #     self.assertStatusCode(200)
    #
    # def test_post_method(self):
    #     self.post(f'{self.base_url}/post', data={'key':'value'})
    #     self.assertStatusCode(200)
    #
    # def test_get_method(self):
    #     payload = {'key1': 'value1', 'key2': 'value2'}
    #     self.get(f'{self.base_url}/get', params=payload)
    #     self.assertStatusCode(200)
    #
    # def test_delete_method(self):
    #     self.delete(f'{self.base_url}/delete')
    #     self.assertStatusCode(200)
    # def test_res(self):
    #     payload = {"hobby": ["basketball", "swim"], "name": "tom", "age": "18"}
    #     self.get("http://httpbin.org/get", params=payload)
    #     print(self.response)
    # def test_sqltest(self):
    #
    #     db = MySQLDB(host='192.168.5.190', port=int(3306),
    #              user='root',
    #              password='abc123..',
    #              database='sn_yfcp202105_workbench')
    #
    #
    #     ret = db.execute_sql("SELECT * FROM w_notice WHERE id = 1")
    #     print(ret)
#
# if __name__ == '__main__':
#     seldom.main()

    