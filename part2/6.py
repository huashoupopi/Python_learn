from fastapi import FastAPI, Path, Query

app = FastAPI()

# 结合 Path 和 Query 来声明路径参数和查询参数的更多信息
# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: int = Path(title="The ID of the item to get"),
#     q: str|None = Query(default=None, max_length=50, alias="item-query")
# ):
#     results: dict = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


# 顺序  可以用*号  
#ge 大于等于 ge=1 大于等于1  gt 大于 le 小于等于 lt 小于 
#/items/100?item-query=foobaritems&q=swa&size=0.5
@app.get("/items/{item_id}")
async def read_items(*,
                    item_id: int = Path(title="The ID of the item to get", ge=1, le=1000), 
                    q: str,
                    size: float = Query(gt=0, lt=1)
                    ):
    results: dict = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results