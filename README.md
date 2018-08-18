# zhihu_user_api

每个用户的粉丝列表
https://www.zhihu.com/api/v4/members/{url_token}/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20

<\br>

url_token:"liu-ceng-lou"
url_token:"ha-ha-13-11"

<\br>

判断是否有下一页并进入
paging:
{is_end: false, totals: 56,…}
is_end:false
is_start:true
next:
"http://www.zhihu.com/api/v4/members/godaye/followees?include=data%5B%2A%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=20"
previous:""
totals:56

<\br>


每个用户的详细信息(鼠标放在名称上加载)
https://www.zhihu.com/api/v4/members/{url_token}?include=allow_message%2Cis_followed%2Cis_following%2Cis_org%2Cis_blocking%2Cemployments%2Canswer_count%2Cfollower_count%2Carticles_count%2Cgender%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics

<\br>

https://www.zhihu.com/api/v4/members/liu-ceng-lou/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20

<\br>

HEADERS={
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
"cookie": "",
"pragma": "no-cache",
"upgrade-insecure-requests": "1",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
}

<\br>


爬了不到1000个用户被403, 浏览器还能正常访问
挂了代理, 换了UA, 换了端口, 还是被403
requests写个同个url的另一个爬虫可以访问
排除请求头有问题, 不知道知乎怎么分辨的

















