import requests
import os

code = 500
max_retries = 5

#配置账号和密码
your_account="你的账号";
your_password="你的密码";
your_mac="你的mac值可以在请求参数看 或者不代这个参数 浏览器会自动帮你填入"

# 定义请求的URL和参数
url = "http://10.17.8.18:801/eportal/portal/login"
params = {
    "callback": "dr1003",
    "login_method": "1",
    "user_account": os.getenv("USER_ACCOUNT", your_account+"@telecom"),  # 从环境变量读取，或使用默认值
    "user_password": os.getenv("USER_PASSWORD", your_password),  # 从环境变量读取，或使用默认值
    "wlan_user_ip": "10.21.102.241",
    "wlan_user_ipv6": "",
    "wlan_user_mac": your_mac,
    "wlan_ac_ip": "10.17.4.1",
    "wlan_ac_name": "",
    "jsVersion": "4.1.3",
    "terminal_type": "1",
    "lang": "zh-cn",
    "v": "6415",
    "lang": "zh"
}

for i in range(max_retries):
    try:
        # 发送GET请求
        response = requests.get(url, params=params)
        code = response.status_code
        
        # 打印响应内容
        print("Response status code:", code)
        print("Response text:", response.text)
        
        # 如果连接成功，退出循环
        if code == 200:
            print("请求发出成功!")
            break

    except requests.RequestException as e:
        print(f"请求发生错误: {e}")
    except Exception as e:
        print(f"未知错误: {e}")

if code != 200:
    print("连接失败!!")
