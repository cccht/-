# 青科科技大学 今日校园

请注意：**此脚本目前仅适用于青岛科技大学崂山校区信息学院研究生表单（具体的表单不同所使用的脚本不同）**

# 禁止任何人使用此项目提供付费的代挂服务

#### 今日校园每日自动提交疫情上报py脚本，支持server酱推送提交结果消息

#### 使用了此脚本或者参考了这个项目，请自觉给项目点个star

#### 本项目仅供学习交流使用，如作他用所承受的任何直接、间接法律责任一概与作者无关

#### 如果此项目侵犯了您或者您公司的权益，请立即联系我删除

#### 99%的问题都可以通过仔细阅读readme（使用说明，也叫项目说明）解决

#### 如有问题也可直接联系我

#### 此外通过此处 [密码测试](https://qust.campusphere.net/) 测试学号及使用密码是否正确

# 项目说明

- `定时版.py` 使用 `schedule` 模块进行定时执行，具体情况请测试之

- `手动修改文件版本.py` 打开 `py` 文件手动填写账户密码等即可使用

- `配置文件版.py` 打开后运行会在同目录生成 `today.json` 打开修改其中参数即可使用

- `Releases` 中添加的 `exe` 文件即为配置文件版，便于更多人使用，当然可以自动打包另外两项

  打包推荐命令 `pyinstaller --noconsole -F -w --icon=此处为图标.ico 今日校园-定时版.py`

# 使用方式

1. **下载**
2. **安装模块（requests、schedule）**
3. **填写相关信息（学号、密码）**
4. **运行**
5. **完成今日校园表单填写**

# 说明

1. 再次声明 **此项目仅适用青岛科技大学**
2. 此项目依赖 `Python3.8` 如没有请自行安装，或者下载 `Releases` 中 `exe` 文件直接使用
3. Linux请安装相关环境
4. 此项目依赖 `requests schedule json` 等Python库，如没有，请自行安装之（本来打算生成`requirements.txt`，因为项目中还有别的库懒得删了）
5. **此项目默认提交全部正常的情况，如果有其他情况，请自行在今日校园APP上提交，项目目的仅为方便正常情况同学，严禁使用此项目伪造数据。疫情防疫严峻时刻请恪守学校要求**

# 设计思路

1. 模拟登陆

2. 获取表单

3. 填充表单

4. 提交表单

5. 推送消息（通过server酱）

   **使用模拟的方式均为正常模拟，无攻击及其他违法行为，如有违反其他规定，请联系必删除之**

# 更新日志

- 2021-10-7 发布青岛科技大学今日校园模拟登陆

# 参考链接

在此项目中主要参考其他类似项目综合写成，可以说在思想上大体与别的提交脚本并无区别，但特针对青科大编写。此处为参考的链接：

[ZimoLoveShuang/auto-submit: 今日校园自动提交疫情上报，通用 (github.com)](https://github.com/ZimoLoveShuang/auto-submit)

[今日校园自动提交信息表单抓包分析【支持教务统一验证】_、moddemod-CSDN博客](https://blog.csdn.net/weixin_43833642/article/details/109583039?utm_medium=distribute.pc_feed_404.none-task-blog-2~default~BlogCommendFromMachineLearnPai2~default-6.control404&depth_1-utm_source=distribute.pc_feed_404.none-task-blog-2~default~BlogCommendFromMachineLearnPai2~default-6.control40)

[纯python模拟登录今日校园云端获取cookie,用于实现自动签到_子滨的博客-CSDN博客](https://blog.csdn.net/weixin_46079657/article/details/108927344)

[今日校园app协议分析(自动提交问卷，自动打卡等等) – 沉沦云博客 (clwl.online)](https://www.clwl.online/cpdaily/#!)

以上为全部参考，供读者继续参考之

# 此外

我对于代码的规范上不是很懂，只是略微学过一点Python，如果有大能可以帮助完善只能是感激不尽

# 请作者喝杯奶茶？

如果你觉得对你有帮助也可以稍微微来杯奶茶~

![支付宝](http://52.175.18.202:8888/down/iGicPQgzMdG2)
