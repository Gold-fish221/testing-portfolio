import requests

BASE = "https://jsonplaceholder.typicode.com"


def test_get_post_1():
    r = requests.get(f"{BASE}/posts/1")
    assert r.status_code == 200
    assert r.json()["id"] == 1
    assert len(r.json()["title"]) > 0


def test_get_post_not_found():
    r = requests.get(f"{BASE}/posts/99999")
    assert r.status_code == 404


def test_create_post():
    payload = {"title": "hi", "body": "b", "userId": 1}
    r = requests.post(f"{BASE}/posts", json=payload)
    assert r.status_code == 201
    assert r.json()["id"] is not None
