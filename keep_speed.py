import threading
import pystray
from PIL import Image
from pystray import MenuItem
import datetime
import logging
import json
import requests
import time

logging.basicConfig(filename="log.txt", format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)

class GetUrlThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self._running = False

    def run(self):
        self._running = True
        while self._running:
            now = datetime.datetime.now()
            # 判断是否在7:00至23:50之间
            if now.hour >= 7 and (now.hour < 23 or (now.hour == 23 and now.minute <= 50)):
                with open("config.txt") as f:
                    # 读取第一行作为url
                    url = f.readline().strip()
                    # 读取剩余的行作为params
                    params = {}
                    for line in f:
                        # 分割每一行为键值对
                        key, value = line.strip().split(": ")
                        # 添加到params字典中
                        params[key] = value
                # 发送get请求并打印响应内容
                try:
                    response = requests.get(url, params=params)
                    # print(response.text)
                    # logging.info("Program started get")
                    # 记录成功的请求信息
                    logging.info(f"Sent get request to speedtest")
                    # 解析响应内容为JSON对象
                    data = json.loads(response.text)
                    # 获取code的值
                    code = data["code"]
                    # 根据code的值进行处理
                    if code == 0:
                        # 请求成功，打印或处理data中的其他信息
                        # print("Request succeeded")
                        # print(data["data"])
                        logging.info("up-speed succeeded!!!")
                    elif code == 10002:
                        # # 请求失败，打印或处理错误信息
                        # print("Request failed")
                        # print(data["msg"])
                        # 记录失败的原因
                        logging.error(f"Request failed with code: {code}, msg: to busy")
                    else:
                        # 请求失败，打印或处理未知错误信息
                        # print("Request failed")
                        # print(data["errors"])
                        # 记录失败的原因
                        logging.error(f"Request failed with code: {code}, errors: {data['errors']}")
                except Exception as e:
                    # 记录异常信息
                    logging.exception(f"Error occurred while sending get request to {url}")
            time.sleep(600)

    def stop(self):
        self._running = False


def on_exit(icon, item):
    icon.visible = False
    geturl_thread.stop()
    icon.stop()


menu = (
    MenuItem(text='退出', action=on_exit),
)

geturl_thread = GetUrlThread()
geturl_thread.start()

image = Image.open("icon.png")
icon = pystray.Icon("name", image, "提速服务", menu)
icon.run()
