# 进程间通信
# 会出现资源竞争问题,加锁解决
from multiprocessing import Process,Queue
import time

# def func(q):
#     q.put([1,2,3])

# q = Queue()
# pro = Process(target = func, args = (q,))
# pro.start()
# print(q.get())
# pro.join()


q = Queue()
def write(q, num):
    count = 0
    for i in range(5):
        time.sleep(1*num)
        count += num
        q.put(count)

def read(q):
    while True:
        res = q.get()
        print('read 进程拿到数据:',res)

pw = Process(target = write, args = (q,1))
pw1 = Process(target = write, args = (q,3))
pr = Process(target = read, args = (q,))

pw.start()
pw1.start()
pr.start()

pw.join()
pw1.join()

# pr.join()  # pr一直会阻塞等待队列中的数据,子进程不会结束
pr.terminate()
print('父进程结束')
