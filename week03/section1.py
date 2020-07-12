# twisted 异步IO框架
from twisted.internet import defer
from twisted.web.client import getPage
from twisted.internet import reactor

def response(*args, **kwargs):  # 网页内容
    print('返回网页的内容')
    return 'hh'

def callback(*args):  # defer有结果了会执行回调函数
    print('执行了一个回调', args)

# response 和callback分别在什么时候会调用? 先会调用第一个回调函数,然后以地一个回调函数的返回值,作为参数调用第二个回调函数

@defer.inlineCallbacks
def start(url):
    d = getPage(url.encode('utf-8'))
    d.addCallback(response)
    d.addCallback(callback)

    yield d

def stop(*args, **wargs):
    reactor.stop()

urls = [r'https://www.baidu.com/', r'https://www.sogou.com/']
li = []
for url in urls:
    ret = start(url)  # 执行start 返回一个生成器对象
    li.append(ret)

d = defer.DeferredList(li)  # 将要执行的代码加入到循环当中,有两个事件在循环中运行
d.addBoth(stop)
reactor.run()  # 启动循环
