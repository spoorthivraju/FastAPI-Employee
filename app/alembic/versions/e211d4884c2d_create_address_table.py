"""create_address_table

Revision ID: e211d4884c2d
Revises: cd38512065af
Create Date: 2023-03-23 11:35:06.816016

"""
from alembic import op
import sqlalchemy as sa
import uuid


# revision identifiers, used by Alembic.
revision = 'e211d4884c2d'
down_revision = 'cd38512065af'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'address',
        sa.Column('id', sa.UUID, primary_key=True, default=uuid.uuid4),
        sa.Column('address', sa.VARCHAR(125), nullable=True),
        sa.Column('city', sa.VARCHAR(25), nullable=True),
        sa.Column('state_id', sa.UUID, sa.ForeignKey('state.id'), nullable=True),
        sa.Column('country_id', sa.UUID, sa.ForeignKey('country.id'), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('address')
