"""empty message

Revision ID: af90835b833d
Revises: 
Create Date: 2020-08-17 15:28:21.629394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "af90835b833d"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", sa.Column("is_demo", sa.Boolean(), nullable=False))


def downgrade():
    op.drop_column("users", "is_demo")
