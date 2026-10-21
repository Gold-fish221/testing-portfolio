# 公开 API 接口测试练习（JSONPlaceholder）

以 https://jsonplaceholder.typicode.com 为被测对象的接口测试入门实践，覆盖「用例设计 → Postman 手工断言 → pytest 自动化 → 失败分析」完整链路。

## 内容

| 文件 | 说明 |
|---|---|
| test_demo.py | 3 条基础用例：GET 列表、404 处理、POST 创建 |
| test_users.py | 按用例文档补全的断言练习 |
| test_cases.py | 对照 `testcases/test01_已修正.xlsx` 的 8 条用例翻译，其中 7 条按文档预期编写、与实际响应不符而保留 FAILED，用于练习失败用例阅读与预期修正 |

## 运行

```bash
pip install requests pytest
python -m pytest -v
```

无需本地环境，联网即可运行。

## 说明

`test_cases.py` 中的 FAILED 是有意保留的：按用例文档的预期编写断言，实际接口行为与文档不符时保留失败，用于定位"文档预期 vs 实际行为"的偏差——修正后的文档见 `testcases/test01_已修正.xlsx`。
