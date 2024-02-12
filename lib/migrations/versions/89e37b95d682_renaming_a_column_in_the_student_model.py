"""Renaming a column in the Student model

Revision ID: 89e37b95d682
Revises: be6e74d8d473
Create Date: 2024-02-12 10:48:20.031282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89e37b95d682'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(table_name='students', 
                    column_name='birthday',
                    new_column_name='birthday_date'
                    )


def downgrade() -> None:
    op.alter_column(table_name='students', 
                    column_name='birthday_date',
                    new_column_name='birthday'
                    )
