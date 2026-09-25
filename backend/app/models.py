from typing import Any
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .extensions import db
class Stops(db.Model):
    __tablename__: str = "stops"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(128),nullable=False)
    imageURL = mapped_column(String(128),nullable=False)
    x = mapped_column(DECIMAL(10,6),nullable=False)
    y = mapped_column(DECIMAL(10,6),nullable=False)
    transfer = mapped_column(Boolean,nullable=False, default=False)
    wheelAccessible = mapped_column(Boolean,nullable=False, default=False)
    ticketMachine = mapped_column(Boolean,nullable=False, default=False)
    shelter = mapped_column(Boolean,nullable=False, default=False)
    bench = mapped_column(Boolean,nullable=False, default=False)
    display = mapped_column(Boolean,nullable=False, default=False)
    
class Team(db.Model):
    __tablename__: str = "team"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    members: Mapped[str] = mapped_column(String(255), nullable=False)

    def to_dict(self) -> dict[str, Any]:
        return {"id": self.id, "name": self.name, "members": self.members}

