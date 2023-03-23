"""create_state_table

Revision ID: fe38f8ae5062
Revises: c2c99a5bf0ed
Create Date: 2023-03-20 12:06:40.887534

"""
from alembic import op
import sqlalchemy as sa
import uuid


# revision identifiers, used by Alembic.
revision = 'fe38f8ae5062'
down_revision = 'c2c99a5bf0ed'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'state',
        sa.Column('id', sa.UUID, primary_key=True, default=uuid.uuid4),
        sa.Column('state', sa.VARCHAR(25), nullable=True),
        sa.Column('country_id', sa.UUID, sa.ForeignKey('country.id'), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('state')
