import seldom
from seldom import Seldom
from public_test import login
from test_data import UserInfo
import time

class Task(seldom.TestCase):
    @classmethod
    def start_class(cls):
        get_token = login.UserLogin(UserInfo.user_1)
        cls.token = get_token.login()

    def start(self):
        self.headers = {"token": self.token}

    def test_create_task(self):
        url = f"{Seldom.base_url}/api/v1/task/create/"
        project_id1 = login.GetId(self.token)
        project_id = project_id1.get_id()
        module_id1 = login.GetModuleId(self.token, project_id)
        module_id = module_id1.get_module_id()
        class_id1 = login.GetClassId(self.token, project_id, module_id)
        class_id = class_id1.get_class()
        data = {
            "project_id": project_id,
            "id": 0,
            "name": "以为是",
            "describe": "啊啊啊",
            "cases": [{
                "moduleId": module_id,
                "casesId": [class_id]
            }]
        }
        self.post(url, json=data, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("success", True)
