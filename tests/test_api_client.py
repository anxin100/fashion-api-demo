import unittest
import sys
import os
from unittest.mock import patch
import json

# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.api_client import ApiClient

class TestApiClient(unittest.TestCase):
    def setUp(self):
        """
        在每个测试方法执行前设置测试环境
        """
        # 初始化 ApiClient 实例
        self.api_client = ApiClient(base_url="http://127.0.0.1:8002")

    @patch('http.client.HTTPSConnection')
    def test_check_email_registered(self, mock_https_connection):
        """
        测试检查邮箱是否已注册的功能
        """
        # 模拟响应数据
        mock_response = unittest.mock.Mock()
        mock_response.read.return_value = json.dumps({
            "status": "success",
            "data": {
                "is_registered": False
            }
        }).encode()
        
        # 设置模拟连接的行为
        mock_conn = unittest.mock.Mock()
        mock_conn.getresponse.return_value = mock_response
        mock_https_connection.return_value = mock_conn

        # 测试用例 1: 检查一个邮箱地址
        test_email = "test@example.com"
        result = self.api_client.check_email_registered(test_email)
        
        # 确保返回的是字符串类型（JSON 格式）
        self.assertIsInstance(result, str)
        
        # 验证返回的 JSON 数据结构
        parsed_result = json.loads(result)
        print("test_check_email_registered result:", parsed_result)
        # 验证是否调用了正确的 endpoint
        # mock_conn.request.assert_called_once_with(
        #     "GET", 
        #     "/api/system/auth/email/is/registered/?email=test@example.com"
        # )

def main():
    unittest.main()

if __name__ == "__main__":
    main() 