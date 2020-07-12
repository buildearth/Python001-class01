import os
import time
from multiprocessing import Process, Queue, cpu_count

# fork 使用
# res = os.fork()  # 一旦运行fork()就会产生一个子进程, 执行后续代码,父进程也会执行一边后续代码
'''
 在子进程中这个方法会返回0(res = 0)；在父进程内，这个方法会返回子进程的编号PID。
 子进程拷贝了父进程的资源,两个进程资源是独立的,互相不影响
'''
# if res == 0:
#     print('我是子进程: %s, 父进程: %s'%(os.getpid(), os.getppid()))
# else:
#     print('我是父进程:%s'%os.getpid())


# multiprocessing
'''
# 函数式创建子进程
q = Queue()
# 多进程完成多个任务,有多个函数,给不同的子进程触发执行
def f(x):
    q.put(x)
    # time.sleep(3)
    print("子进程")

# target 参数需要传需可调用对象, name 为进程添加一个别名 , args 将参数传递给可调用对象
p = Process(target = f, args = (1,))  # 创建一个进程
p.start()  # 执行进程
print(p.join(timeout = 1))  # 如果加上timeout(可选参数)父进程就不会等待子进程结束在结束,最多会阻塞指定时间
print('父进程',q.get())
print(cpu_count())  # 当前机器cpu数量
'''

# 类方式创建子进程
# 不给Process制定target的话,会自动调用类中的run方法
class NewProcess(Process):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):  # 必须重写父类中的run方法,来让子进程做事情
        while True:
            print('我就是子进程:{}, pid:{}'.format(self.num, os.getpid()))
            time.sleep(1)

for i in range(5):
    p = NewProcess(i)
    p.start()
