from typing import Any
from decimal import Decimal
from sqlalchemy import Boolean, DECIMAL, String
from sqlalchemy.orm import Mapped, mapped_column

from .extensions import db
class Stops(db.Model):
    __tablename__: str = "stops"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    lines: Mapped[str] = mapped_column(String(128), nullable=False, default="")
    is_transfer: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    transfer_lines: Mapped[str] = mapped_column(String(128), nullable=False, default="")
    x: Mapped[Decimal | None] = mapped_column(DECIMAL(10, 6), nullable=True)
    y: Mapped[Decimal | None] = mapped_column(DECIMAL(10, 6), nullable=True)
    wheelchair_accessible: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    has_shelter: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    has_bench: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    has_ticket_machine: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    has_display: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    image_url: Mapped[str | None] = mapped_column(String(255), nullable=True)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "lines": self.lines,
            "is_transfer": self.is_transfer,
            "transfer_lines": self.transfer_lines,
            "x": float(self.x) if self.x is not None else None,
            "y": float(self.y) if self.y is not None else None,
            "wheelchair_accessible": self.wheelchair_accessible,
            "has_shelter": self.has_shelter,
            "has_bench": self.has_bench,
            "has_ticket_machine": self.has_ticket_machine,
            "has_display": self.has_display,
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
