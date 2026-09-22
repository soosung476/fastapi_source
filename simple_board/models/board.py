# 게시글 삽입: userId, title, body
# 게시글 조회: userId, title, body, id

"""
"userId": 1,
"id": 1,
"title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
"body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",

"""

from pydantic import BaseModel


class BoardInsert(BaseModel):
    userId: int
    title: str
    body: str


class Board(BoardInsert):
    id: int


class Comment(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str
