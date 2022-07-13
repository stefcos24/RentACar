"""added int on price

Revision ID: 2339fdc3a080
Revises: cf3604df99ea
Create Date: 2022-06-24 16:06:45.577098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2339fdc3a080'
down_revision = 'cf3604df99ea'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'role',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'role',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
