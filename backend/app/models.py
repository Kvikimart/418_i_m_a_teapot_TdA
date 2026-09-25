from typing import Any
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .extensions import db
class Stops(db.Model):
    __tablename__: str = "stops"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128),nullable=False)
    imageURL: Mapped[str] = mapped_column(String(128),nullable=False)
    x: Mapped[float] = mapped_column(DECIMAL(10,6),nullable=False)
    y: Mapped[float] = mapped_column(DECIMAL(10,6),nullable=False)
    transfer: Mapped[bool] = mapped_column(Boolean,nullable=False, default=False)
    wheelAccessible: Mapped[bool] = mapped_column(Boolean,nullable=False, default=False)
    ticketMachine: Mapped[bool]  = mapped_column(Boolean,nullable=False, default=False)
    shelter: Mapped[bool] = mapped_column(Boolean,nullable=False, default=False)
    bench: Mapped[bool] = mapped_column(Boolean,nullable=False, default=False)
    display: Mapped[bool] = mapped_column(Boolean,nullable=False, default=False)
    
class Team(db.Model):
    __tablename__: str = "team"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    members: Mapped[str] = mapped_column(String(255), nullable=False)

    def to_dict(self) -> dict[str, Any]:
        return {"id": self.id, "name": self.name, "members": self.members}

