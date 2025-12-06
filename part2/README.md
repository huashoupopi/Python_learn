# **

这部分主要是对fastapi的学习

## part1

首先学习了uv  详细命令见手册和ai给出

```
# 忽略虚拟环境 (uv 创建的)
.venv/
venv/
web/

# 忽略 Python 编译缓存 (自动生成的垃圾文件)
__pycache__/
*.pyc

# 忽略环境变量 (里面可能有密码)
.env

# 忽略系统文件
.DS_Store
```

创建.gitignore(与main.py同级)

uv的一些命令:

- 创建环境 `uv venv --python=3.10`  默认名字为`.venv` 不建议改 很麻烦
- 激活 `source .venv/bin/activate` windows下另一个命令....
- 初始化项目 `uv init`
- 添加包  初始化项目后`uv add`  未初始化 `uv pip install`
- 固定python版本 `uv python pin 3.11`

vscode可能找不到解释器 手动添加 或者创建文件夹`.vscode` 新建文件`settings.json`

```
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.terminal.activateEnvironment": true
}
```

