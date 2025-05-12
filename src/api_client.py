import http.client
import json
from urllib.parse import urlparse

class ApiClient:
    def __init__(self, base_url="https://api.example.com"):
        """
        初始化 API 客户端
        
        Args:
            base_url (str): API 基础 URL，格式如 'https://api.example.com' 或 'api.example.com'
        """
        # 确保 base_url 格式正确
        if not base_url.startswith(('http://', 'https://')):
            base_url = 'https://' + base_url
        
        parsed_url = urlparse(base_url)
        self.host = parsed_url.netloc
        self.protocol = parsed_url.scheme

    def check_email_registered(self, email):
        """
        检查邮箱是否已注册
        
        Args:
            email (str): 要检查的邮箱地址
            
        Returns:
            dict: API响应数据，包含邮箱注册状态
        """
        try:
            endpoint = f"/api/system/auth/email/is/registered/?email={email}"
            
            if self.protocol == 'https':
                conn = http.client.HTTPSConnection(self.host)
            else:
                conn = http.client.HTTPConnection(self.host)
                
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