import seldom
from seldom import Seldom
from seldom.request import check_response, HttpRequest
from test_data import UserInfo


class UserLogin(HttpRequest):
    def __init__(self, user):
        self.username = user.get("username")
        self.password = user.get("password")

    @check_response(describe="获取token", status_code=200, ret="data.Token")
    def login(self):
        url = f"{Seldom.base_url}/api/v1/login/"
        r = self.post(url, data={"username": self.username, "password": self.password})
        return r


class GetId(HttpRequest):
    """封装获取项目最后一个的id"""
    def __init__(self, token1):
        self.token = token1
        self.headers = {"token": self.token}

    @check_response(describe="获取id", status_code=200, ret="data.projectList[-1].id")
    def get_id(self):
        r = self.get(f"{Seldom.base_url}/api/v1/project/?page=1&size=6", headers=self.headers)
        return r


class GetModuleId(HttpRequest):
    """获取模块根节点的id"""
    def __init__(self, token1, project_id):
        # my_token = UserLogin(UserInfo.user_1)
        # token = my_token.login()
        # project_id = GetId(token)
        # my_project_id = project_id.get_id()
        self.token = token1
        self.my_id = project_id
        self.headers = {"token": self.token}
        self.url = f"{Seldom.base_url}/api/v1/project/{self.my_id}/moduleTree"

    @check_response("获取根节点id", 200, ret="data[0].id")
    def get_module_id(self):
        r = self.get(self.url, headers=self.headers)
        return r


class GetClassId(HttpRequest):
    """获取用例id以及根节点id"""
    def __init__(self, token, project_id, module_id):
        self.token = token
        self.project_id = project_id
        self.module_id = module_id
        self.headers = {"token": self.token}
        self.url = f"{Seldom.base_url}/api/v1/module/{self.module_id}/cases/?page=1&size=5"

    # @check_response("获取根节点id", 200, ret="data.taskList[0].moduleId")
    # def get_module(self):
    #     r = self.get(self.url, headers=self.headers)
    #     return r

    @check_response("获取用例id", 200, ret="data.caseList[0].id")
    def get_class(self):
        r = self.get(self.url, headers=self.headers)
        return r


class UserLoginUi(seldom.TestCase):

    def login(self):
        url = f"{Seldom.base_url}/#/login"
        self.open(url)
        self.type_enter(css="[type=text]", text="admin", clear=True)
        self.type_enter(css="[type=password]", text="admin123456", clear=True)
        self.click(css="#loginButton")
        self.sleep(3)