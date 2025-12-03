
def outer(logo: str):
    def inner(text: str):
        print(f"{logo} {text} {logo}")
    return inner

fn1 = outer("有大病")  #outer 返回 inner  而fn1 接收返回
fn1("麦丁华")
fn1("麦丁华的哥哥麦顶针")

fn2 = outer("确实有病")
fn2("麦当当")


# 需要用nonlocal 来修改外层函数的变量
def account_create(initial_amount=0):
    def atm(num,deposit = True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存入：{num},余额为:{initial_amount}")
        else:
            initial_amount -= num
            print(f"取出:{num},余额为:{initial_amount}")

    return atm

atm = account_create()
atm(100)
atm(200)
atm(100,False)

