# 进程池
from multiprocessing.pool import Pool
import multiprocessing
import time
import os
import random


'''
def run(name):
    print('{}子进程开始运行, 进程id是{}'.format(name, os.getpid()))
    start_time = time.time()
    time.sleep(random.choice([1,2,3,4]))
    stop_time = time.time()
    print('{}子进程结束, 进程id是{},运行时间:{}'.format(name, os.getpid(), stop_time - start_time))


cpu_num = multiprocessing.cpu_count()
print(cpu_num)
p = Pool(cpu_num)
for i in range(10):
    p.apply_async(run, args = (i,))


# close关闭进程池,关闭之后不能在添加进程
p.close() # 温柔结束进程,会等待进程池中的任务结束
# 对于进程池,在join之前一定要先close
p.join()  # 进程池对象调用join,,会等待进程池中所有的进程结束
p.terminate()  # 强制结束进程
'''

# 获取进程返回值
def f(n):
    print(n)
    return n**2
l = []
with Pool(processes = 4) as pool:
    res = pool.apply_async(f, args = (2,))
    l.append(res)
    print(res.get())  # 只能在启动进程后在其后阻塞等待?

    res = pool.apply_async(time.sleep, args = (3,))
    # print(res.get())
    l.append(res)

