import seldom
from seldom import data


# class Login(seldom.TestCase):
#     """这是个登录模块"""
#     @data([
#         ("无密码", "admin", "", "10010"),
#         ("密码错误", "admin", "123", "10011"),
#         ("登录成功", "admin", "admin123456", "")
#     ])
#     def test_login(self, _, username, password, code):
#         data = {"username": username, "password": password}
#         self.post("/api/v1/login/", data)
#         self.assertPath("error.code", code)

