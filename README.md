# 测速网提速保持程序

## 这是什么

一个针对测速网（[测速网 - 专业测网速, 网速测试, 宽带提速, 游戏测速, 直播测速, 5G测速, 物联网监测 - SpeedTest.cn](https://www.speedtest.cn/)）提速服务的保持程序，将会定时向测速网发送提速请求来保证提速服务的正常运行。

## 如何使用

### 配置请求头

- 打开任意浏览器，如edge，访问认证网址(https://www.speedtest.cn/jiasu),点击F12键进入开发者模式，选择网络

![image-20230628182431282](https://cdn.jsdelivr.net/gh/xywml/picgo_img@main/202306281837459.png)

- F5刷新界面，找到reopen?source=www，下面有个请求标头，点击原始，然后把它全部复制下来。

![image-20230628182935950](https://cdn.jsdelivr.net/gh/xywml/picgo_img@main/202306281835083.png)

- 找到解压目录的config.txt,复制过去，注意删除GET这一行，复制后的config.txt的前几行应该是这样的：

  ```
  https://tisu-api.speedtest.cn/api/v2/speedup/reopen?source=www
  Accept: application/json, text/plain, */*
  Accept-Encoding: gzip, deflate, br
  Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
  ```

- 双击exe文件运行

## 其他内容

程序默认600秒发送一次请求，运行时右下角会有一个托盘图标，点击可以退出程序。
