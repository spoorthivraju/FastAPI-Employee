"""create_department_table

Revision ID: cd38512065af
Revises: fe38f8ae5062
Create Date: 2023-03-20 12:18:56.464930

"""
from alembic import op
import sqlalchemy as sa
import uuid


# revision identifiers, used by Alembic.
revision = 'cd38512065af'
down_revision = 'fe38f8ae5062'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'department',
        sa.Column('id', sa.UUID, primary_key=True, default=uuid.uuid4),
        sa.Column('department', sa.VARCHAR(25), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('department')
