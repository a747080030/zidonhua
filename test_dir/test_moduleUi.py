import seldom
from public_test import login
from seldom import Seldom, Steps
import time


class ModuleUi(seldom.TestCase):
    def start(self):
        login1 = login.UserLoginUi()
        self.time = str(time.time())
        self.login = login1.login()
        Steps(desc="进入用例管理界面").find(".el-icon-s-grid").click()

    def test_create(self):
        Steps(desc="构建根节点").find(".el-input__inner").move_to_click().\
            find("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-last-child(1) > span").\
            click().find(".el-icon-circle-plus-outline").click().\
            find("#nav > div > section > section > main > div > div.project-dialog > div > div > div.el-dialog__body > form > div:nth-child(2) > div > div > input").\
            type(self.time).find("#nav > div > section > section > main > div > div.project-dialog > div > div > div.el-dialog__body > form > div:nth-child(4) > div > div > button.el-button.el-button--primary").click()

        self.assertElement(css=".el-message__content")

    # def test_edit(self):
    #     Steps(desc="编辑验证").find("#nav > div > section > section > main > div > div.el-card.box-card.is-always-shadow > div > div.module-tree > div > div.el-card__body > div > div.el-tree-node.is-current.is-focusable > div > span.custom-tree-node").click().\
    #         find("#nav > div > section > section > main > div > div.el-card.box-card.is-always-shadow > div > div.filter-line > button").click()

