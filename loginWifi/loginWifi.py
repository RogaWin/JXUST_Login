import requests
import os

code = 500
max_retries = 5

import socket

def get_local_ip():
    # 创建一个socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # 连接到一个公共的外部地址
        s.connect(('8.8.8.8', 80))
        # 获取本地IP地址
        local_ip = s.getsockname()[0]
    except Exception as e:
        print(f"获取本地IP时出错: {e}")
        local_ip = '127.0.0.1'  # 返回本地主机地址作为默认
    finally:
        # 关闭socket连接
        s.close()

    return local_ip

# 获取并打印本地IP地址
ip_address = get_local_ip()
print(f"本地IP地址: {ip_address}")

#配置账号和密码
your_account="你的账号";
your_password="你的密码";
<<<<<<< HEAD
your_mac="mac"
=======
your_mac="你的mac值可以在请求参数看 或者不代这个参数 浏览器会自动帮你填入"
>>>>>>> 122b2064390f6558d09cf92057f0487b9fa9b359

# 定义请求的URL和参数
url = "http://10.17.8.18:801/eportal/portal/login"
params = {
    "callback": "dr1003",
    "login_method": "1",
    "user_account": os.getenv("USER_ACCOUNT", your_account+"@telecom"),  # 从环境变量读取，或使用默认值
    "user_password": os.getenv("USER_PASSWORD", your_password),  # 从环境变量读取，或使用默认值
    "wlan_user_ip": ip_address,
    "wlan_user_ipv6": "",
    "wlan_user_mac": your_mac,
    "wlan_ac_ip": "10.17.4.1",
    "wlan_ac_name": "",
    "jsVersion": "4.1.3",
    "terminal_type": "1",
    "lang": "zh-cn",
    "v": "10234",
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
