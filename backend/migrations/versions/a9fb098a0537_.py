"""empty message

Revision ID: a9fb098a0537
Revises: ed8c61c84c34
Create Date: 2021-10-05 12:08:02.237624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9fb098a0537'
down_revision = 'ed8c61c84c34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('menus', sa.Column('proeprties', sa.String(length=150), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('menus', 'proeprties')
    # ### end Alembic commands ###