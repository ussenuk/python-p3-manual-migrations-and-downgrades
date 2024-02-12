"""Renaming students to scholars

Revision ID: be6e74d8d473
Revises: 791279dd0760
Create Date: 2024-02-12 10:34:20.995389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be6e74d8d473'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
