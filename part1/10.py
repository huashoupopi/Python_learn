# 协程yield实现生产者消费者模式

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)

"""
yield r 的双重角色
作为产出：当执行到 yield r 时，生成器暂停，把 r 返回给外部调用者（此处是 produce）。
作为输入点：下一次外部调用 send(value) 恢复生成器时，yield 表达式的值就是 value。因此把 yield r 写成 n = yield r，就能捕获外部传来的值并赋给 n。
send(n) 为什么能给 n 赋值
首次 c.send(None) 只是预激活，生成器停在 yield r，并把初始 r 返回给外部。
之后每次 c.send(n)：
将 n 作为 yield 表达式的结果返回给生成器，所以 n = yield r 中的右侧 yield r 此刻等于传入的 n。
生成器继续往下执行，此时 n 就是外部传入的数字。
总结：n = yield r 让生成器既能“出”数据（r）又能“收”数据（n）；send(n) 恰好把值送回同一个挂起点，让 n 获得外部传来的内容。
"""