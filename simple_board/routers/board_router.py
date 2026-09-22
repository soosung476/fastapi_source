from fastapi import APIRouter, HTTPException, status

from models.board import Board, BoardInsert, Comment

board_router = APIRouter()

# 전체 조회 + GET: http://localhost:8000/boards
# 하나 조회 + GET: http://localhost:8000/boards/1
# 하나 수정 + PUT: http://localhost:8000/boards/1 + 수정데이터
# 하나 삭제 + DELETE: http://localhost:8000/boards/1
# 댓글 조회 + http://localhost:8000/boards/1/comments

datas = [
    {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
    },
    {
        "userId": 1,
        "id": 2,
        "title": "qui est esse",
        "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla",
    },
    {
        "userId": 1,
        "id": 3,
        "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
        "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut",
    },
    {
        "userId": 1,
        "id": 4,
        "title": "eum et est occaecati",
        "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit",
    },
    {
        "userId": 1,
        "id": 5,
        "title": "nesciunt quas odio",
        "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque",
    },
    {
        "userId": 1,
        "id": 6,
        "title": "dolorem eum magni eos aperiam quia",
        "body": "ut aspernatur corporis harum nihil quis provident sequi\nmollitia nobis aliquid molestiae\nperspiciatis et ea nemo ab reprehenderit accusantium quas\nvoluptate dolores velit et doloremque molestiae",
    },
    {
        "userId": 1,
        "id": 7,
        "title": "magnam facilis autem",
        "body": "dolore placeat quibusdam ea quo vitae\nmagni quis enim qui quis quo nemo aut saepe\nquidem repellat excepturi ut quia\nsunt ut sequi eos ea sed quas",
    },
    {
        "userId": 1,
        "id": 8,
        "title": "dolorem dolore est ipsam",
        "body": "dignissimos aperiam dolorem qui eum\nfacilis quibusdam animi sint suscipit qui sint possimus cum\nquaerat magni maiores excepturi\nipsam ut commodi dolor voluptatum modi aut vitae",
    },
    {
        "userId": 1,
        "id": 9,
        "title": "nesciunt iure omnis dolorem tempora et accusantium",
        "body": "consectetur animi nesciunt iure dolore\nenim quia ad\nveniam autem ut quam aut nobis\net est aut quod aut provident voluptas autem voluptas",
    },
    {
        "userId": 1,
        "id": 10,
        "title": "optio molestias id quia eum",
        "body": "quo et expedita modi cum officia vel magni\ndoloribus qui repudiandae\nvero nisi sit\nquos veniam quod sed accusamus veritatis error",
    },
]

comment_data = []

boards = [Board(**board) for board in datas]
comments = [Comment(**comment) for comment in comment_data]


@board_router.get("", response_model=list[Board])
async def get_boards():
    return boards


@board_router.get("/{id}", response_model=Board)
async def get_board(id: int):
    for board in boards:
        if board.id == id:
            return board
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="해당 board를 찾을 수 없습니다."
    )


@board_router.put("/{id}", response_model=Board)
async def put_board(id: int, update_board: Board):
    for board in boards:
        if board.id == id:
            board.title = update_board.title
            board.body = update_board.body

            return board
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="해당 board를 찾을 수 없습니다."
    )


@board_router.delete("/{id}", response_model=list[Board])
async def delete_board(id: int):
    for board in boards:
        if board.id == id:
            boards.remove(board)
            return boards
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="해당 board를 찾을 수 없습니다."
    )


@board_router.post("", response_model=Board)
async def post_board(data: BoardInsert):
    new_id = max(board.id for board in boards) + 1
    board = Board(userId=data.userId, title=data.title, body=data.body, id=new_id)
    boards.append(board)
    return board

    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="서버 오류가 발생했습니다 잠시 후에 시도해주세요.",
    )


@board_router.get("/{id}/comments", response_model=list[Comment])
async def get_board_comments(id: int):
    return []
