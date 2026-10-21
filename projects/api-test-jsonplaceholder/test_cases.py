import requests

BASE = "https://jsonplaceholder.typicode.com"


def test_tc001_正常创建():
    payload = {"title": "测试标题", "body": "内容", "userId": 1}
    r = requests.post(f"{BASE}/posts", json=payload)
    assert r.status_code == 201


def test_tc002_title为空():
    payload = {"title": "", "body": "内容", "userId": 1}
    r = requests.post(f"{BASE}/posts", json=payload)
    assert r.status_code == 400


def test_tc003_缺少title():
    payload = {"body": "内容", "userId": 1}
    r = requests.post(f"{BASE}/posts", json=payload)
    assert r.status_code == 400


def test_tc004_title超长():
    payload = {"title": "d" * 500, "body": "内容", "userId": 1}
    r = requests.post(f"{BASE}/posts", json=payload)
    assert r.status_code == 400


def test_tc005_userId为0():
    payload = {"title": "测试标题", "body": "内容", "userId": 0}
    r = requests.post(f"{BASE}/posts", json=payload)
    assert r.status_code == 400


def test_tc006_userId为负1():
    payload = {"title": "测试标题", "body": "内容", "userId": -1}
    r = requests.post(f"{BASE}/posts", json=payload)
    assert r.status_code == 400


def test_tc007_userId为字符串():
    payload = {"title": "测试标题", "body": "内容", "userId": "abc"}
    r = requests.post(f"{BASE}/posts", json=payload)
    assert r.status_code == 400


def test_tc008_body为空():
    payload = {"title": "测试标题", "body": "", "userId": 1}
    r = requests.post(f"{BASE}/posts", json=payload)
    assert r.status_code == 400
