# Fashion Demo

## 接口文档


## 请求示例

### 导入依赖

```bash
import http.client
import json
from urllib.parse import urlparse
```

### 运行开发服务器

```bash
def check_email_registered(base_url, email):
    """
    检查邮箱是否已注册
    
    Args:
        email (str): 要检查的邮箱地址
        
    Returns:
        dict: API响应数据，包含邮箱注册状态
    """
    try:
        endpoint = f"/api/system/auth/email/is/registered/?email={email}"

        parsed_url = urlparse(base_url)
        host = parsed_url.netloc
        protocol = parsed_url.scheme
        
        if protocol == 'https':
            conn = http.client.HTTPSConnection(host)
        else:
            conn = http.client.HTTPConnection(host)
            
        conn.request("GET", endpoint)
        response = conn.getresponse()
        data = response.read().decode()

        # 格式化输出 JSON 数据
        parsed = json.loads(data)
        return_data = json.dumps(parsed, indent=2)

        return return_data
        
    except Exception as e:
        return json.dumps({
            "error": str(e),
            "status": "error"
        }, indent=2)
    finally:
        if 'conn' in locals():
            conn.close()
```

