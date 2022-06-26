import seldom
from public_test.login import UserLogin, GetId
from seldom import Seldom
from seldom.request import check_response
from test_data import UserInfo


class Management(seldom.TestCase):

    @classmethod
    def start_class(cls):
        login1 = UserLogin(UserInfo.user_1)
        cls.token1 = login1.login()

    def start(self):
        self.url = f"{Seldom.base_url}/api/v1/project/"
        self.headers = {"token": self.token1}

    def test_create(self):
        """创建项目"""
        data = {
            "name": "名字啦", "describe": "不可描述", "status": True
        }
        self.post(self.url, data=data, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("success", True)

    def test_management(self):
        """修改项目"""
        project_id = GetId(self.token1)
        id = int(project_id.get_id())
        data = {
            "id": id,
            "name": "测试测试2",
            "describe": "不可描述1",
            "status": True,
            "create_time": "2022-06-06 06:47:40"
        }
        self.put(self.url, data=data, headers=self.headers)
        self.assertPath("success", True)