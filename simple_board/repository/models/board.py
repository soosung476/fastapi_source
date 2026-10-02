from repository.database import Base
from sqlalchemy import String, Identity, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime

# id :pk
# title:
# text
# user_info
# created_date
# modified_date


class Board(Base):

    __tablename__ = "boards"
    id: Mapped[int] = mapped_column(Identity(start=1, increment=1), primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    contents: Mapped[str] = mapped_column(String(2000), nullable=False)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("board_users.user_id"), nullable=False
    )

    # 컬럼의 개념 아님(파이썬 객체간 연결)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now
    )
    user: Mapped["User"] = relationship(back_populates="boards")
    comments: Mapped[list["Comment"]] = relationship(back_populates="board")
