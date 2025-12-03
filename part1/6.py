# 装饰器

def outer(func):
    def inner():
        print("我要开始睡觉了")
        func()
        print("我睡醒了")
    return inner

@outer
def sleep():
    import random
    import time
    print("睡着了")
    time.sleep(random.randint(1,5))

sleep()


import time
def logger(msg):
    def time_master(func):
        def call_func():
            start = time.time()
            func()
            stop = time.time()
            print(f"[{msg}]一共耗费了{(stop-start):.2f}")
        return call_func
    return time_master
@logger(msg="A")
def funcA():
    time.sleep(1)
    print("正在调用funcA...")
@logger(msg="B")
def funcB():
    time.sleep(1)
    print("正在调用funcA...")

funcA()
funcB()