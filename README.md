# threadingTest

开启多线程对服务器进行压力测试

使用requests.post()发送post请求

request.post(url, data=None, json=None)中 data 和 json 都是用来提交数据的，不能同时使用，data 为 dict 格式，json 用来提交 json 格式数据
    如果碰到 payload 报文，使用 json 提交报文。
