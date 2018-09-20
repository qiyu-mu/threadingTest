# threadingTest

开启多线程对服务器进行压力测试

threading-ceshi.py 中：

使用requests.post()发送post请求

request.post(url, data=None, json=None)中 data 和 json 都是用来提交数据的，不能同时使用，data 为 dict 格式，json 用来提交 json 格式数据
    如果碰到 payload 报文，使用 json 提交报文。
    
threading-tcp-ceshi.py 中：

使用 socket 通信基于 tcp 协议进行服务器收发报文进行压力测试

socket 分为’服务器端‘和’客户端‘，我这是用来测试服务器的，只用写’客户端‘即可

socket.connect()    :   用来连接服务器，链接成功返回None，不成功返回SOCKET_ERROR
socket.send()       :   用来向服务器发送报文，我用的是 xml 格式的报文数据， 发送成功返回发送过去的报文字节数，不成功返回SOCKET_ERROR
socket.sendall()    :   和 send 一样，发送成功后返回None
socket.recv()       :   用来接受数据

用以记录初始 socket


