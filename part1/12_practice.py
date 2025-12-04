import asyncio
import time

async def fake_io(name: str, delay: float) -> None:
    print(f"开始 {name}")
    await asyncio.sleep(delay)
    print(f"结束 {name}")

async def run_sequential() -> None:
    start = time.perf_counter()
    await fake_io("任务一", 1)
    await fake_io("任务二", 1)
    duration = time.perf_counter() - start
    print(f"串行完成耗时 {duration:.2f} 秒\n")

async def run_con() -> None:
    start = time.perf_counter()
    await asyncio.gather(fake_io("任务一", 1), fake_io("任务二", 1))
    duration = time.perf_counter() - start
    print(f"并发完成耗时 {duration:.2f} 秒\n")

async def main() -> None:
    print("=== 串行等待演示 ===")
    await run_sequential()
    print("=== 并发等待演示 ===")
    await run_con()

if __name__ == "__main__":
    asyncio.run(main())