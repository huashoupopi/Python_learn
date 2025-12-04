# 序列化和反序列化
import json

with open("username.json","w") as f:
    list_user = ["lcx","lcy","lcz"]
    name = json.dumps(list_user)
    f.write(name)

with open("username.json","r") as f:
    name = f.read()
    list_user = json.loads(name)
    print(type(list_user))
    print(list_user)
    print("Welcome back "+list_user[0])

data = [{"name":"张大山","age":11},{"name":"王大锤","age":12},{"name":"赵小虎","age":16}]
json_str = json.dumps(data,ensure_ascii=False)
print(json_str)

## 进阶

class Student:
    def __init__(self, name: str, age: int, score: float):
        self.name = name
        self.age = age
        self.score = score
    
s: Student = Student("小明", 20, 88.5)

def student2dict(std: Student):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print(json.dumps(s, default=student2dict, ensure_ascii=False))
print(json.dumps(s, default=lambda obj: obj.__dict__, ensure_ascii=False))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"name": "小明", "age": 20, "score": 88.5}'
print(json.loads(json_str, object_hook=dict2student))