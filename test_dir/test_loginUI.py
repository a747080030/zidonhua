import seldom
import selenium.webdriver
from seldom import Seldom, Steps, data
import time


class LoginUi(seldom.TestCase):

    def start(self):
        self.url = f"{Seldom.base_url}/#/login"

    @data(
        [
            ("密码正确", "admin", "admin123456", "用户名密码错误"),
            # ("无账号", "", "1234", "请输入账号"),
        ]
    )
    def login(self, _, username, password, message):
        Steps(desc="登陆测试").open(self.url).find("[type=text]").clear().sleep(2).type(username)
        self.execute_script('document.querySelector("[type=password]").value="";')
        Steps(desc="继续").find("[type=password]").type(password).sleep(2).find("#loginButton").click()



