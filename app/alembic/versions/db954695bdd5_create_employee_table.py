"""create_employee_table

Revision ID: db954695bdd5
Revises: e211d4884c2d
Create Date: 2023-03-23 11:36:27.707660

"""
from alembic import op
import sqlalchemy as sa
import uuid


# revision identifiers, used by Alembic.
revision = 'db954695bdd5'
down_revision = 'e211d4884c2d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'employee',
        sa.Column('id', sa.UUID, primary_key=True, default=uuid.uuid4),
        sa.Column('first_name', sa.VARCHAR(25), nullable=True),
        sa.Column('last_name', sa.VARCHAR(25), nullable=True),
        sa.Column('email', sa.VARCHAR(60), nullable=True),
        sa.Column('department_id', sa.UUID, sa.ForeignKey('department.id'), nullable=True),
        sa.Column('address_id', sa.UUID, sa.ForeignKey('address.id'), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('employee')
