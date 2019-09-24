import os
import time
import random
import queue
from multiprocessing import Process, Queue


# 写数据进程执行的代码:
def make_cook(q):
    print('开始制餐: %s' % os.getpid())
    for value in ['红烧猪蹄', '土豆牛肉', '大闸蟹', '牡丹虾刺身']:
        print('制作%s中...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def get_cook(q):
    print('开始取餐: %s' % os.getpid())
    while True:
        # 这里实际应用场景应该写成死循环
        try:
            value = q.get(timeout=2)
        except queue.Empty as err:
            break
        else:
            print('取出%s.' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=make_cook, args=(q,))
    pr = Process(target=get_cook, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    # pr.terminate()
    pr.join()