# 软件测试作品集 · 王明明

2027 届 · 区块链工程 · 求职方向：软件测试实习生

本仓库收录求职作品：接口测试自动化脚本、Postman 接口测试集合、测试用例文档，均来自对真实/公开 API 的完整测试实践。

## 目录结构

```
testing-portfolio/
├── projects/
│   ├── api-test-jsonplaceholder/   # 公开 API 测试练习（用例设计 + 自动化 + 失败分析）
│   └── ruoyi-api-test/             # 若依开源系统接口自动化（正向/负向/安全 + 缺陷守护用例）
├── postman/
│   └── ruoyi_api.postman_collection.json   # Postman 接口测试集合（6 个请求，含断言）
└── testcases/
    ├── test01_已修正.xlsx           # 公开 API 测试用例文档（8 条，含测试结论）
    └── ry001.xlsx                   # 若依用户管理模块用例文档（9 条，含实际结果）
```

## 项目一览

| 项目 | 技术 | 要点 |
|---|---|---|
| 若依 RuoYi 接口测试 | Python、pytest、requests、Postman | 6 条自动化（5 通过 + 1 缺陷守护用例）、5 组正向/负向/安全用例、禅道缺陷跟踪 |
| 公开 API 测试练习 | Postman、pytest、Excel | 8 条用例设计、失败用例分析与预期修正 |

## 快速运行

```bash
git clone <本仓库地址>
cd testing-portfolio
pip install -r requirements.txt

# 若依接口测试（需要本地部署的 RuoYi，见项目 README）
cd projects/ruoyi-api-test
python -m pytest test_ruoyi.py -v

# 公开 API 测试练习（无需环境，直接联网运行）
cd projects/api-test-jsonplaceholder
python -m pytest -v
```

## Postman 集合导入

Postman → Import → 选择 `postman/ruoyi_api.postman_collection.json`。

执行顺序：`01 登录-成功` → `02 用户列表-带会话`；`03-06` 为负向/安全用例；`06` 执行前先清空 Cookies。

## 说明

- 所有测试均在本地/公开演示环境进行，不涉及任何生产数据。
- 用例文档中的手机号、邮箱为构造测试数据，非真实个人信息。
- `test_ruoyi.py` 中 `test_06` 为对应已知缺陷（异常信息泄露）的守护用例，当前预期失败，缺陷修复后将自动转绿。
