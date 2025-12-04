#pathlib的学习
from pathlib import Path

#获取当前脚本的绝对路径
#.resolve()方法可以将相对路径转换为绝对路径
current_file = Path(__file__).resolve()
print(f"当前脚本的绝对路径: {current_file}")

#获取父目录
project_root = current_file.parent
print(f"项目根目录: {project_root}")

#拼接模型路径 
model_path = project_root / "models" / "my_model.pkl"
print(f"模型文件路径: {model_path}")

#检查路径是否存在
if model_path.exists():
    print("模型文件存在。")
else:
    print("模型文件不存在。")

# 自动创建上传目录
upload_dir = project_root / "uploads"
# 创建目录
# parents=True: 如果 static 不存在，也顺便创建 (类似 mkdir -p)
# exist_ok=True: 如果目录已经存在，不要报错，啥也不做
upload_dir.mkdir(parents=True, exist_ok=True)

print(f"✅ 上传目录已就绪: {upload_dir}")

# 模拟保存文件
file_path = upload_dir / "blade_01.jpg"
print(f"准备保存到: {file_path}")

# pathlib 可以直接打开文件 (替代 open(path, 'w'))
# write_text / write_bytes 是 pathlib 的快捷方法
file_path.write_text("模拟图片数据") 
print("写入成功！")