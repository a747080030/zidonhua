import seldom
from public_test.login import UserLoginUi
from test_data import UserInfo
from seldom import Seldom, Steps
from test_loginUI import LoginUi
import time


class ManageCreate(seldom.TestCase):

    def start(self):
        self.login = UserLoginUi()
        self.login.login()
        # self.url = f"{Seldom.base_url}/api/v1/project/"
        self.project_name = str(time.time())

    def test_create(self):
        Steps(desc="创建项目").find("[cy-data=create-project]").click().find("[cy-data=project-name]").\
            type(self.project_name).find("[cy-data=project-desc]").type("UI测试的描述文本").find("[cy-data=save-project]").\
            click()

        self.assertElement(css=".el-message__content")
        Steps(desc="验证数据").find(".el-input__inner").click()\
            .find("div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)").click()\
            .find("ul.el-pager > li:nth-last-child(1)").click()

        self.assertText(self.project_name)

    def test_edit(self):
        Steps(desc="编辑项目验证").\
            find("div:nth-last-child(1) > div > div > div.el-card__header > div > span:nth-child(2) > div > i").\
            move_to_click().find("body > ul > li:nth-child(1) > button > span").click().\
            find("[cy-data=project-name]").clear().type(self.project_name).find("[cy-data=save-project]").click()

        self.assertText(self.project_name)

    def test_delete(self):
        Steps(desc="删除最后一个项目").find(".el-input__inner").click()\
            .find("div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)").click()\
            .find("ul.el-pager > li:nth-last-child(1)").click().\
            find("div:nth-last-child(1) > div > div.el-card__header > div > span:nth-child(2) > div > i").\
            move_to_click().find("body > ul > li:nth-child(2) > button > span").click()

        self.assertElement(css=".el-message__content")


