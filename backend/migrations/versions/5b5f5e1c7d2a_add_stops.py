"""add stops

Revision ID: 5b5f5e1c7d2a
Revises: ead49d961fa9
Create Date: 2026-11-09 19:20:00.000000
"""

from alembic import op
import sqlalchemy as sa


revision = "5b5f5e1c7d2a"
down_revision = "ead49d961fa9"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "stops",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=128), nullable=False),
        sa.Column("wheelchair_accessible", sa.Boolean(), nullable=False),
        sa.Column("has_shelter", sa.Boolean(), nullable=False),
        sa.Column("has_ticket_machine", sa.Boolean(), nullable=False),
        sa.Column("image_url", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("stops")
