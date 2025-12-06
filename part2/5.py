from fastapi import FastAPI, Query

app = FastAPI()
# 使用 Query 来声明更多的查询参数信息
# @app.get("/items/")
# async def read_items(q: str|None = Query(default=None, max_length=50, min_length=3, pattern="^fixedprefix$")):
#     result: dict = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         result.update({"q": q})
#     return result
# 带默认值的查询参数
# @app.get("/items/")
# async def read_items(q: str|None = Query(default="fixedprefix", max_length=50, min_length=3)):
#     result: dict = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         result.update({"q": q})
#     return result

# 必选查询参数
# @app.get("/items/")
# async def read_items(q: str|None = Query(max_length=50, min_length=3)):
#     result: dict = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         result.update({"q": q})
#     return result

# 查询参数列表 / 多个值 以及其他参数 弃用参数之类的
# @app.get("/items/")
# async def read_items(q: list[str]|None = Query(
#     default=None,
#     title="Query string1231231223",
#     description="Multiple query strings can be passed",
#     min_length=3,
#     deprecated=True
#     )):
#     result: dict = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         result.update({"q": q})
#     return result

# 别名参数 http://127.0.0.1:8000/items/?item-query=somevalue  python关键字不能有-号
@app.get("/items/")
async def read_items(q: str|None = Query(default=None, alias="item-query")):
    result: dict = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result