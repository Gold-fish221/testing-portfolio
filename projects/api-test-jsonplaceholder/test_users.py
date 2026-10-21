import requests

BASE = "https://jsonplaceholder.typicode.com"


def test_users_1():
    # 第 1 空：发 GET 请求，URL 是 /users/1，把响应存到 r
    r = requests.get(f"{BASE}/posts/1")
    # 第 2 空：断言状态码是 200
    assert r.status_code == 200
    # 第 3 空：断言返回的 id 等于 1（提示：r.json()["id"]）
    assert r.json()["id"]  == 1

def test_users_2():
    # 第 1 空：发 GET 请求，URL 是 /users/1，把响应存到 r
    r = requests.get(f"{BASE}/posts/1")
    # 第 2 空：断言状态码是 200
    assert r.status_code == 200
    # 第 3 空：断言返回的 id 等于 1（提示：r.json()["id"]）
    assert r.json()["id"]  == 1