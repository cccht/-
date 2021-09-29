
大学列表URL https://static.campushoy.com/apicache/tenantListSort
{"id":"qust","name":"青岛科技大学","img":"http://res.campushoy.com/schoolIcon/10426.jpg"}
学校信息 https://mobile.campushoy.com/v6/config/guest/tenant/info?ids=qust
登陆接口 https://qust.campusphere.net/iap/login/mobile.html
ipa 登陆 https://qust.campusphere.net/iap/doLogin
GET lt值 https://qust.campusphere.net/iap/login?service=https://qust.campusphere.net/portal/login
Location: https://qust.campusphere.net/iap/login/pc.html?_2lBepC=bcf080ffaf384b6d99c297911db9cda5

1. 访问 https://qust.campusphere.net/iap/login 重定向获得lt set-cookie HWWAFSESID HWWAFSESTIME CONVERSATION
2. https://qust.campusphere.net/iap/login/pc.html?_2lBepC=67078446365349b2b54ffb6b0b59d0ea 携带cookie 
Cookie: CONVERSATION=iap-1018615895163461-CONV-a0209681-8985-4967-bc92-efabe277d9fd; HWWAFSESID=5d2b373a58e889f614; HWWAFSESTIME=1632889501950
3. lt  https://qust.campusphere.net/iap/security/lt 获取加密cookie同上
4. https://qust.campusphere.net/iap/doLogin 登陆
Set-Cookie: CASTGC=iap-1018615895163461-TGT-071fe84b-a120-44e2-815e-d2636680408b; Path=/iap; HttpOnly
5. https://qust.campusphere.net/iap/login?service=https%3A%2F%2Fqust.campusphere.net%2Fportal%2Flogin cookie + castgc
6. 获得 https://qust.campusphere.net/portal/login?ticket=ST-iap:1018615895163461:ST:1124eb72-3e11-47f0-8454-f89308b8093e:20210929123311
ticket
MOD_AUTH_CAS=ST-iap:1018615895163461:ST:1124eb72-3e11-47f0-8454-f89308b8093e:20210929123311
