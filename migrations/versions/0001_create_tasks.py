"""create tasks table

Revision ID: 0001
Revises:
"""
import sqlalchemy as sa
from alembic import op

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column(
            "status",
            sa.Enum("draft", "progress", "finish", "deployed", name="taskstatus"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_table("tasks")
    sa.Enum(name="taskstatus").drop(op.get_bind(), checkfirst=True)
