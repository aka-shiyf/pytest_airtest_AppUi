"""
    实现部分前置
    @pytest.fixture（scope="作用域"，params="数据驱动",autouse="自动执行",ids="自定义参数名",name="重命名")
     作用域：function,class,module,package/session
    yield和return都表示返回，yield返回多次多个数据，return只会返回一次，return后不能接代码
    @pytest.fixture()一般会和conftest.py文件一起使用
    conftest.py名称是固定的，功能很强大
    1.conftest.py文件是单独存放@pytest.fixtrue()的方法，用处是可以在多个py文件之间共享前置配置
    2.conftest.py里面的方法在调用时不需要导入，可以直接使用
    3.conftest.py可以有多个，也可以有多个不同层级
"""
import pytest

from start_alipay import start


@pytest.fixture(scope="session",autouse=True)
def login_alipay():
    start()
