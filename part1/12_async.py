import asyncio
import time


async def fake_io(name: str, delay: float) -> None:
    # 模拟一次耗时的异步任务
    print(f"开始 {name}")
    await asyncio.sleep(delay)
    print(f"结束 {name}")


async def run_sequential() -> None:
    # 顺序等待两个任务，演示串行耗时
    start = time.perf_counter()
    await fake_io("任务一", 1)
    await fake_io("任务二", 1)
    duration = time.perf_counter() - start
    print(f"串行完成耗时 {duration:.2f} 秒\n")


async def run_concurrent() -> None:
    # 并发等待两个任务，演示协程带来的速度提升
    start = time.perf_counter()
    await asyncio.gather(fake_io("任务一", 1), fake_io("任务二", 1))
    duration = time.perf_counter() - start
    print(f"并发完成耗时 {duration:.2f} 秒\n")


async def main() -> None:
    print("=== 串行等待演示 ===")
    await run_sequential()
    print("=== 并发等待演示 ===")
    await run_concurrent()


if __name__ == "__main__":
    asyncio.run(main())


"""
asyncio提供了完善的异步IO支持，用asyncio.run()调度一个coroutine；
在一个async函数内部，通过await可以调用另一个async函数，这个调用看起来是串行执行的，
但实际上是由asyncio内部的消息循环控制；
在一个async函数内部，通过await asyncio.gather()可以并发执行若干个async函数。
"""