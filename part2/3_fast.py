from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}


@app.get("/items")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]
# http://127.0.0.1:8000/items/?skip=0&limit=2

@app.get("/items/{item_id}")
async def read_item_by_id(item_id: str, q: str|None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item["q"] = q
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item
#必选查询参数 needy
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item