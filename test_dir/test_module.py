import seldom
from public_test import login
from test_data import UserInfo
from seldom import Seldom
from time import sleep


class ModuleTest(seldom.TestCase):

    @classmethod
    def start_class(cls):
        login1 = login.UserLogin(UserInfo.user_1)
        cls.token = login1.login()

    def start(self):
        self.url = f"{Seldom.base_url}/api/v1/module/"
        self.headers = {"token": self.token}

    def test_create_module(self):
        """创建根节点"""
        module_id = login.GetId(self.token)
        self.my_id = module_id.get_id()
        data = {
            "project_id": self.my_id,
            "name": "创建根节点",
            "describe": "111",
            "parent_id": 0
        }
        self.post(self.url, data=data, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("success", True)

    def test_create_z(self):
        """创建用例"""
        module_id = login.GetId(self.token)
        my_id = module_id.get_id()
        case_id = login.GetModuleId(self.token, my_id)
        my_case_id = case_id.get_module_id()
        url = f"{Seldom.base_url}/api/v1/case/create/"
        date = {
            "name": "这是名称啦",
            "module_id": my_case_id,
            "method": "GET",
            "url": "http://httpbin.org/get",
            "header": "{\"token\":\"123\"}",
            "params_type": "params",
            "params_body": "{\"hello\":\"world\"}",
            "result": "\"这是response\"",
            "assert_type": "include",
            "assert_text": "这是assert"
        }
        self.post(url=url, json=date, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("success", True)