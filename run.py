import seldom
from seldom import Seldom
from seldom import SeldomTestLoader
from seldom import TestMainExtend
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")


if __name__ == '__main__':
    # run test file
    # seldom.main("./test_dir/test_web_sample.py")
    # run test dir
    seldom.main("./test_dir/", browser="chrome", base_url="http://quick.testpub.cn", title="小叮当测试", tester="xiaodingdan", debug=False)
    # SeldomTestLoader.collectCaseInfo = True
    # main_extend = TestMainExtend(path="./test_dir/")
    # case_info = main_extend.collect_cases(json=True)
    # print(case_info)