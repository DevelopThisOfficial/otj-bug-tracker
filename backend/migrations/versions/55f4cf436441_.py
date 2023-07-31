"""empty message

Revision ID: 55f4cf436441
Revises: 
Create Date: 2023-07-28 00:24:24.367151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "55f4cf436441"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "status",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_status_id"), "status", ["id"], unique=False)
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )
    op.create_index(op.f("ix_user_id"), "user", ["id"], unique=False)
    op.create_table(
        "ticket",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("start_date", sa.DateTime(), nullable=True),
        sa.Column("completed_date", sa.DateTime(), nullable=True),
        sa.Column("status_id", sa.Integer(), nullable=True),
        sa.Column("story_points", sa.Integer(), nullable=True),
        sa.Column("creator", sa.Integer(), nullable=True),
        sa.Column("created_date", sa.DateTime(), nullable=True),
        sa.Column("last_update", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["creator"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["status_id"],
            ["status.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_ticket_id"), "ticket", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_ticket_id"), table_name="ticket")
    op.drop_table("ticket")
    op.drop_index(op.f("ix_user_id"), table_name="user")
    op.drop_table("user")
    op.drop_index(op.f("ix_status_id"), table_name="status")
    op.drop_table("status")
    # ### end Alembic commands ###