from typing import Any


# 类型注解的练习
def process(name, age):
    return name + str(age)

def process_annotated(name: str, age: int) -> str:
    return name + str(age)



if __name__ == "__main__":
    print(process("Alice", 30))
    print(process_annotated("Bob", 25))
    name: str = "xsq"
    age: int = 28
    height: float = 1.50
    is_student: bool = True
    print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}")
    # 容器类型注解
    scores: list[int] = [98, 99, 100]
    prices: dict[str, float] = {"apple": 0.99, "banana": 0.59}
    users: list[dict[str, str]] = [{"name": "Alice"}, {"name": "Bob"}]
    # 处理不确定性
    def get_user(user_id: int|str):
        print(f"查用户: {user_id}")

    def send_email(email: str|None):
        if email:
            print(f"发送邮件到: {email}")
        else:
            print("没有提供邮箱地址")    
    
    def print_anything(data: Any):
        print(f"打印数据: {data}")
    
    get_user(123)    
    get_user("abc")
    send_email("user@example.com")
    send_email(None)
    print_anything([1, "two", 3.0, {"four": 4}])