# Fashion Demo

## 接口文档
https://apifox.com/apidoc/shared-6f676345-774a-4153-b52e-bdee79d37af8

## 请求示例

### 导入依赖

```bash
from src.api_client import ApiClient
```

### 运行

```bash
api_client = ApiClient(base_url="http://127.0.0.1:8002")
result = api_client.check_email_registered("test@example.com")
print(result)
```

### 运行测试

```bash
python -m unittest tests/test_api_client.py
```
