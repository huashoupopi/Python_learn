from typing import Any
from pydantic import BaseModel

def add(x: int, y:int) -> int:
    return x + y

result: int = add(5, 10)
print(f"5 + 10 = {result}")

student_scores: dict[str, list[int]] = {
    "Alice": [95, 88, 92],
    "Bob": [78, 85, 80]
}

def analyze_scores(data: dict[str, list[int]]) -> None:
    for name, scores in data.items():
        avg: float = sum(scores) / len(scores)
        print(f"{name} 的平均分是 {avg:.2f}")

analyze_scores(student_scores)

def find_user(user_id: int|str, email: str|None = None) -> str:
    msg = f"正在查找 ID: {user_id} (类型: {type(user_id).__name__})"
    if email:
        msg += f"，邮箱: {email}"
    else:
        msg += "，未提供邮箱"
    return msg
print(find_user(1010))
print(find_user("user_2020", "user2020@example.com"))

class Detection_Result(BaseModel):
    label: str
    conf: float
    bbox: list[float]  # [x_min, y_min, x_max, y_max]

yolo_output: list[dict[str, Any]] = [
    {"label": "person", "conf": 0.98, "bbox": [34.0, 50.0, 200.0, 400.0]},
    {"label": "bicycle", "conf": 0.85, "bbox": [100.0, 150.0, 300.0, 350.0]},
]

def filter_results(results: list[Detection_Result]):
    for res in results:
        if res.conf > 0.9:
            print(f"高置信度检测: {res.label} (置信度: {res.conf}, 位置: {res.bbox})")

model_results = [Detection_Result(**item) for item in yolo_output]
filter_results(model_results)