# 解析文件名
from pathlib import Path

# 假设这是上传的文件路径
p = Path("static/uploads/blade_2023_v1.jpg")

print(f"完整文件名: {p.name}")      # blade_2023_v1.jpg
print(f"文件后缀:   {p.suffix}")    # .jpg
print(f"纯文件名:   {p.stem}")      # blade_2023_v1 (没有后缀)
print(f"父级目录:   {p.parent}")    # static\uploads

# 换个后缀 (比如把 .jpg 换成 .json 用来存结果)
json_path = p.with_suffix(".json")
print(f"对应的JSON路径: {json_path}") # static\uploads\blade_2023_v1.json


#批量检测
# 遍历 static/uploads 目录下所有的 .jpg 图片
image_dir = Path("static/uploads")

# glob 方法支持通配符
# *.jpg 表示所有 jpg 文件
# **/*.jpg 表示递归查找所有子文件夹里的 jpg (非常强大)
print("\n--- 扫描图片 ---")
for img_file in image_dir.glob("*.jpg"):
    print(f"发现图片: {img_file.name}")