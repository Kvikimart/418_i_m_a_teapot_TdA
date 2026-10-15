from typing import Any
from decimal import Decimal
from sqlalchemy import Boolean, DECIMAL, String
from sqlalchemy.orm import Mapped, mapped_column

from .extensions import db
class Stops(db.Model):
    __tablename__: str = "stops"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    lines: Mapped[str] = mapped_column(String(128), nullable=False)
    is_transfer: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    transfer_lines: Mapped[str] = mapped_column(String(128), nullable=False, default="")
    x: Mapped[Decimal] = mapped_column(DECIMAL(10, 6), nullable=False)
    y: Mapped[Decimal] = mapped_column(DECIMAL(10, 6), nullable=False)
    wheelchair_accessible: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    has_shelter: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    has_bench: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    has_ticket_machine: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    has_display: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    image_url: Mapped[str] = mapped_column(String(255), nullable=False, default="")
    
class Team(db.Model):
    __tablename__: str = "team"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    members: Mapped[str] = mapped_column(String(255), nullable=False)

    def to_dict(self) -> dict[str, Any]:
        return {"id": self.id, "name": self.name, "members": self.members}

