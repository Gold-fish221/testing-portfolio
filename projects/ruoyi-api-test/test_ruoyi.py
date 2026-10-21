import requests

BASE = "http://localhost:8080"

def test_01_login_success():
    r = requests.post(BASE + "/login", data={
        "username": "admin",
        "password": "admin123",
        "rememberMe": "false"
    })
    assert r.json()["code"] == 0

def test_02_login_wrong_password():
    r = requests.post(BASE + "/login", data={
        "username": "admin",
        "password": "wrong_pwd",
        "rememberMe": "false"
    })
    assert r.json()["code"] == 500  # 错误密码应失败

def test_03_login_sql_inject():
    r = requests.post(BASE + "/login", data={
        "username": "' or 1=1 --",
        "password": "admin123",
        "rememberMe": "false"
    })
    assert r.json()["code"] != 0  # 注入绝不能成功

def test_04_list_without_login():
    r = requests.post(BASE + "/system/user/list",
                      data={"pageNum": 1, "pageSize": 5})
    assert "rows" not in r.text  # 未登录应返回登录页，不是用户数据

def test_05_list_after_login():
    s = requests.Session()  # Session 自动带 Cookie
    s.post(BASE + "/login", data={
        "username": "admin",
        "password": "admin123",
        "rememberMe": "false"
    })
    r = s.post(BASE + "/system/user/list",
               data={"pageNum": 1, "pageSize": 5})
    d = r.json()
    assert d["code"] == 0
    assert len(d["rows"]) > 0

def test_06_bug347_no_java_exception_leak():
    # 对应禅道 Bug#347：缺失 rememberMe 不应泄露 Java 异常原文
    # 当前 bug 未修复，此用例预期 FAILED；修复后转绿 → 关闭 bug
    r = requests.post(BASE + "/login", data={
        "username": "admin",
        "password": "admin123"
        # 故意不传 rememberMe，触发缺陷
    })
    msg = r.json().get("msg", "")
    assert "Boolean" not in msg
    assert "invoke" not in msg
    assert "null" not in msg.lower()