# pydantic的学习
import pydantic
from pydantic import BaseModel, ValidationError
from typing import Any

class User(BaseModel):
    id: int 
    name: str
    is_active: bool = True

class Defect(BaseModel):
    label: str
    box: list[float]  # [x_min, y_min, x_max, y_max]
    conf: float

class Inage_Resule(BaseModel):
    file_name: str
    detections: list[Defect]

external_data: dict[str, Any] = {
    "id": "123",
    "name": "Alice",
}

bad_data: dict[str, Any] = {
    "id": "not_an_int",
    "name": "Bob",
}

complex_data: dict[str, Any] = {
    "file_name": "image1.jpg",
    "detections": [
        {
            "label": "cat",
            "box": [10.0, 20.0, 50.0, 80.0],
            "conf": 0.95
        },
        {
            "label": "dog",
            "box": [15.0, 25.0, 55.0, 85.0],
            "conf": 0.90
        }
    ]
}

user = User(**external_data)
print(f"type of user:{type(user)}  , user:{user}")
print(user.id)
print(type(user.id))

try:
    User(**bad_data)
except ValidationError as e:
    print("验证错误:")
    print(e.json())

result = Inage_Resule(**complex_data)
print(f"文件名: {result.file_name}")
print("检测结果:")
for detection in result.detections:
    print(f"标签: {detection.label}, 位置: {detection.box}, 置信度: {detection.conf}")

# 把对象转换为字典
data_dict = result.model_dump()
print(data_dict)
# 把对象直接变成JSON字符串
json_str = result.model_dump_json()
print(json_str)


print(f"111:{result}")

"""
杀手锏二：@field_validator (自定义逻辑)
痛点： 有些规则很复杂。比如，文件名必须以 .jpg 或 .png 结尾。这靠 Field 是搞不定的。

解决方案： 写一个自定义验证函数，挂到字段上。

实战代码：

Python

from pydantic import BaseModel, field_validator

class ImageUpload(BaseModel):
    filename: str

    # 自定义规则：检查文件名后缀
    @field_validator('filename')
    def check_extension(cls, v):
        if not v.endswith(('.jpg', '.png')):
            raise ValueError('只支持 JPG 或 PNG 图片')
        return v

# 测试
try:
    img = ImageUpload(filename="report.pdf")
except Exception as e:
    print(f"拦截成功：{e}")
3. 杀手锏三：BaseSettings (管理密码配置)
痛点： 还记得我们连接数据库的 URL 吗？ postgresql://postgres:admin@localhost/wind_db 千万不要把它直接写死在代码里（Hardcode）。如果你把代码上传到 GitHub，密码就泄露了。

解决方案： Pydantic 提供了一个专门管理配置的神器 pydantic-settings。它会自动读取 .env 文件里的配置。

实战步骤：

安装：pip install pydantic-settings

在项目根目录新建一个文件 .env（里面写密码）：

代码段

DB_URL=postgresql://postgres:admin@localhost/wind_db
SECRET_KEY=my_super_secret_key
写代码读取它：

Python

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_url: str
    secret_key: str

    class Config:
        # 告诉它去读哪个文件
        env_file = ".env"

# 实例化配置
settings = Settings()

# 直接使用！
print(f"正在连接数据库: {settings.db_url}")
"""