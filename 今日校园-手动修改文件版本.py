# -*- coding: utf-8 -*-
# @Author  : cccht
# @Time    : 2021/10/7 18:33
# @Github  : https://github.com/cccht
import hashlib
import json
import requests
from Crypto.Cipher import AES
import base64

# 此处填写用户名 即学号
import pyaes

username = ""
# 此处填写相应密码
password = ""
# 此处可填写server酱用于接收微信通知
server_key = ""
# 此处填写设备 Id（即手机id）
deviceId = ""


#######################################
# 以下不需修改直接运行即可
# 再次注意：此版本仅用作青岛科技大学崂山校区信息学院雷老师发布表单，如需作他用请注意表单内容是否一致或对代码进行二次修改
# 如果青科人进行二次修改，可修改解析表单中信息 即 def parse_form() 函数即可修改相应表单填写内容
# 一定注意：此脚本仅用于与真实信息一致时一键填写，如与正常表单不一致时请自行填写今日校园！！！
ApiUrl = "https://qust.campusphere.net"
DESKEY = 'b3L26XNL'
AESKEY = 'ytUQ7l2ZZu8mLvJZ'
APPVERSION = '9.0.12'

# 解析表单
def parse_form(text: str):
    form = []
    j_data = json.loads(text)
    datas = j_data['datas']
    question_number = datas['totalSize']  # 问题总数
    question_list = datas['rows']  # 问题列表

    # print('共计{}个问题...'.format(question_number))

    # 处理地理位置选择
    def handle_area(idx):
        area = '青岛科技大学'
        question_detail = question_list[idx]
        title = question_detail['title']
        # print(title)
        question_detail['value'] = '山东省/青岛市/崂山区/' + area
        question_detail['area1'] = '山东省'
        question_detail['area2'] = '青岛市'
        question_detail['area3'] = '崂山区'
        question_detail['area3'] = area
        form.append(question_detail)

    handle_area(0)
    # 对其余单选进行选择
    for i in range(1, 3):
        question_detail = question_list[i]
        title = question_detail['title']
        # print(title)
        question_detail['fieldItems'][0]['isSelected'] = 1
        del question_detail['fieldItems'][1:]
        form.append(question_detail)
    for i in range(3, 7):
        question_detail = question_list[i]
        title = question_detail['title']
        # print(title)
        question_detail['fieldItems'][1]['isSelected'] = 1
        del question_detail['fieldItems'][0]
        form.append(question_detail)
    for i in range(7, 9):
        question_detail = question_list[i]
        title = question_detail['title']
        # print(title)
        question_detail['fieldItems'][0]['isSelected'] = 1
        del question_detail['fieldItems'][1:]
        form.append(question_detail)
    return form


def AESEncrypt(s, key, iv=b'\x01\x02\x03\x04\x05\x06\x07\x08\t\x01\x02\x03\x04\x05\x06\x07'):
    Encrypter = pyaes.Encrypter(pyaes.AESModeOfOperationCBC(key.encode('utf-8'), iv))
    Encrypted = Encrypter.feed(s)
    Encrypted += Encrypter.feed()
    return base64.b64encode(Encrypted).decode()


def GenBodyString(form):
    return AESEncrypt(json.dumps(form), AESKEY)


def SignForm(bodyString):
    tosign = {
        "appVersion": '9.0.12',
        "bodyString": bodyString,
        "deviceId": deviceId,
        "lat": 36.12802101,
        "lon": 120.4913785279999,
        "model": "MI 6",
        "systemName": "android",
        "systemVersion": "7.1.1",
        "userId": username,
    }
    signStr = ""
    for i in tosign:
        if signStr:
            signStr += "&"
        signStr += "{}={}".format(i, tosign[i])
    signStr += "&{}".format(AESKEY)
    return hashlib.md5(signStr.encode()).hexdigest()


# 自动提交
def auto_submit(data, headers, formWid, collectWid, schoolTaskWid,instanceWid):
    url = ApiUrl + '/wec-counselor-collector-apps/stu/collector/submitForm'
    headers["Content-Type"] = "application/json"
    headers["User-Agent"] = '今日校园/1 CFNetwork/1128.0.1 Darwin/19.6.0'.encode('utf-8')
    headers["Cpdaily-Extension"] = '64JITpWPkKteVjjbeN0fQ9itX23mYPTHqi0iNh2pmNCzQ3mXksu9HByXtcsD Evb31xHlfIR2UZoyE8Dp8/OFKKFps2/IpzfvB9n6jGcKj3EDK+VxkEij1Qbn wzQ2MuwienqC7vlMCAbTKssxnzWsnHvS/RRMJqENe+9azpS7yimfaivrCEqf Kxivn4EGaY0c8Hkkesf5BZHgv9K+p7r94bkEotuO+b6/+y1P6KsS4bgwb/0D xNmgn8tsBZ+D3MZ43ns2TK+OLlBtI1/J3PNptw=='  # 这里如果不添加会提示今日校园版本过低
    form = {
        "formWid": formWid,
        "address": '山东省青岛市崂山区松岭路',
        "collectWid": collectWid,
        "schoolTaskWid": schoolTaskWid,
        "form": data,
        "uaIsCpadaily": True,
        "latitude": 36.12802100890081,
        "longitude": 120.4913785279999,
        'instanceWid': instanceWid
    }
    bodyString = GenBodyString(form)
    # 解码！！！
    # aes = AES.new("ytUQ7l2ZZu8mLvJZ".encode("UTF-8"), AES.MODE_CBC,
    #               b'\x01\x02\x03\x04\x05\x06\x07\x08\t\x01\x02\x03\x04\x05\x06\x07')
    # res = aes.decrypt(base64.b64decode(bodyString))
    # print(res)
    params = {
        "lon": "120.49137853",
        "version": "first_v2",
        "calVersion": "firstv",
        "deviceId": deviceId,
        "userId": username,
        "systemName": "android",
        "lat": "36.12802101",
        "systemVersion": "7.1.1",
        "appVersion": "9.0.12",
        "model": "MI 6",
        "sign": SignForm(bodyString),
        "bodyString": bodyString
    }
    response = requests.post(url=url, headers=headers, data=json.dumps(params))
    j_data = json.loads(response.text)
    code = j_data['code']
    message = j_data['message']
    if code == 0 or message == 'SUCCESS':
        if server_key != "此处填写你的server酱key":
            send_message('恭喜，提交成功啦，打开今日校园app看看惊喜吧！！！')
        print('恭喜，提交成功啦，打开今日校园app看看惊喜吧！！！')
        return True
    else:
        if server_key != "此处填写你的server酱key":
            send_message('提交失败，呜呜呜~_~')
        print("提交失败 >_<")
    print(message)
    return True


def index():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31',
    }
    req = requests.get("https://qust.campusphere.net/iap/login", headers=headers, allow_redirects=False)
    Referer = req.headers['Location']
    CONVERSATION = req.headers['Set-Cookie'].split('; path=/, ')[2].split('; Path=/iap;')[0]
    HWWAFSESID = req.headers['Set-Cookie'].split('; path=/, ')[0]
    HWWAFSESTIME = req.headers['Set-Cookie'].split('; path=/, ')[1]
    cookie = CONVERSATION + "; " + HWWAFSESID + "; " + HWWAFSESTIME
    lt = req.headers['Location'].split("=")[1]
    # 此处可以删减多余的键值，懒得测试所以没有修改
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31',
        'Host': 'qust.campusphere.net',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cookie': cookie,
        'Referer': Referer,
        'sec-ch-ua': '"Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
    }
    # 同上headers
    data = {
        'username': username,
        'password': password,
        'mobile': '',
        'dllt': '',
        'captcha': "",
        'rememberMe': 'false',
        'lt': lt,
    }
    # 此处为登陆
    doLogin = requests.post(ApiUrl + "/iap/doLogin", data, headers=headers, allow_redirects=False)
    CASTGC = doLogin.headers['Set-Cookie'].split('; Path=/iap')[0]
    cookie = cookie + "; " + CASTGC
    headers['Cookie'] = cookie
    headers['Referer'] = ApiUrl + "/iap/login/mobile.html"
    getTicker = requests.get(
        "https://qust.campusphere.net/iap/login?service=https%3A%2F%2Fqust.campusphere.net%2Fportal%2Flogin",
        headers=headers, allow_redirects=False)
    TickerUrl = getTicker.headers['Location']
    getCookie = requests.get(TickerUrl, headers=headers, allow_redirects=False)
    MOD_AUTH_CAS = getCookie.headers['Set-Cookie'].split('; path=/')[0]
    headers['Cookie'] = headers['Cookie'] + "; " + MOD_AUTH_CAS
    print("登陆成功!!!")
    # 获取当前正在填写的表单
    form_url = ApiUrl + '/wec-counselor-collector-apps/stu/collector/queryCollectorProcessingList'
    data = {
        "pageSize": 99999,
        "pageNumber": 1
    }
    headers['X-Requested-With'] = 'XMLHttpRequest'
    headers['Content-Type'] = 'application/json;charset=utf-8'
    data = json.dumps(data)
    get_form = requests.post(form_url, data, headers=headers, allow_redirects=False)
    j_data = json.loads(get_form.text)
    datas = j_data['datas']
    data_number = datas['totalSize']
    if data_number == 0:
        print("当前无未填写表单。")
    rows = datas['rows'][0]
    collectWid = rows['wid']
    formWid = rows['formWid']
    instanceWid = rows['instanceWid']
    # 获取表单详情
    detail_url = ApiUrl + '/wec-counselor-collector-apps/stu/collector/detailCollector'
    get_form = requests.post(detail_url, data=json.dumps({'collectorWid': collectWid,'instanceWid':instanceWid}), headers=headers,
                             allow_redirects=False)
    j_data = json.loads(get_form.text)
    datas = j_data['datas']
    schoolTaskWid = datas['collector']['schoolTaskWid']
    # 获取表单问题
    url = ApiUrl + '/wec-counselor-collector-apps/stu/collector/getFormFields'
    data = {
        'pageNumber': 1,
        'pageSize': 20,
        'formWid': rows['formWid'],
        'collectorWid': rows['wid'],
        'instanceWid': instanceWid
    }
    data = json.dumps(data)
    response = requests.post(url=url, headers=headers, data=data)
    # 解析表单问题并填写
    form_data = parse_form(response.text)
    # 自动提交表单问题
    auto_submit(form_data, headers, formWid, collectWid, schoolTaskWid, instanceWid)
    return None


# 发送server酱信息于微信
def send_message(message):
    header = {
        'Content-type': 'application/x-www-form-urlencoded',
    }
    data = {
        'title': '今日校园填写情况',
        'desp': message,
    }
    send_url = 'https://sctapi.ftqq.com/' + server_key + '.send'
    requests.post(send_url, data, headers=header)


index()
