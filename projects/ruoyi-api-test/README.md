# 若依（RuoYi）接口自动化测试

对本地部署的 RuoYi 4.8.3 开源管理系统进行接口测试的自动化脚本。

## 测试范围

| 用例 | 类型 | 断言要点 |
|---|---|---|
| test_01 登录成功 | 正向 | code == 0 |
| test_02 错误密码 | 负向 | code == 500，提示与密码/用户相关 |
| test_03 SQL 注入 | 安全 | 注入载荷不能登录成功（code != 0） |
| test_04 未认证访问列表 | 安全 | 返回登录页 HTML，不含用户数据 |
| test_05 登录后查列表 | 正向 | requests.Session 会话保持，code == 0 且有数据 |
| test_06 异常信息泄露守护 | 缺陷守护 | 断言响应不含 Java 异常原文（对应禅道 Bug#347，**当前预期 FAILED**） |

## 运行前提

1. 本地部署 RuoYi 4.8.3，端口 8080（本仓库不含服务端代码，源码见若依官方仓库）。
2. 登录接口验证码开关已关闭（`security.captchaEnabled: false`），练习环境配置。
3. 账号 `admin / admin123`（若依默认）。

```bash
pip install requests pytest
python -m pytest test_ruoyi.py -v
```

## 预期结果

- 修复前：`5 passed, 1 failed`（test_06 为缺陷守护用例，失败即缺陷存在）
- 缺陷修复后：`6 passed`（守护用例转绿，可关闭禅道 Bug#347）
