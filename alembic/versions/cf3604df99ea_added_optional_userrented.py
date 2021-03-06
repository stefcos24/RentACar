"""Added Optional userrented

Revision ID: cf3604df99ea
Revises: d1f9ce97b4e4
Create Date: 2022-06-24 15:45:16.399285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf3604df99ea'
down_revision = 'd1f9ce97b4e4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cars', 'user_rented_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('users', 'role',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'role',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('cars', 'user_rented_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
