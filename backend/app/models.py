from typing import Any
from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from .extensions import db
class Stops(db.Model):
    __tablename__: str = "stops"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    wheelchair_accessible: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    has_shelter: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    has_ticket_machine: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    image_url: Mapped[str | None] = mapped_column(String(255), nullable=True)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "wheelchair_accessible": self.wheelchair_accessible,
            "has_shelter": self.has_shelter,
            "has_ticket_machine": self.has_ticket_machine,
            "image_url": self.image_url or None,
        }

class Team(db.Model):
    __tablename__: str = "team"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    members: Mapped[str] = mapped_column(String(255), nullable=False)

    def to_dict(self) -> dict[str, Any]:
        return {"id": self.id, "name": self.name, "members": self.members}



def create_missing_tables() -> None:
    db.create_all()
