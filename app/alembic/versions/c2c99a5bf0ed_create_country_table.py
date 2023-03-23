"""create_country_table

Revision ID: c2c99a5bf0ed
Revises: 
Create Date: 2023-03-20 11:59:13.163437

"""
from alembic import op
import sqlalchemy as sa
import uuid


# revision identifiers, used by Alembic.
revision = 'c2c99a5bf0ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'country',
        sa.Column('id', sa.UUID, primary_key=True, default=uuid.uuid4),
        sa.Column('country', sa.VARCHAR(25), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('country')
