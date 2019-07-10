"""第一次迁移

Revision ID: 79c9cf29b574
Revises: 
Create Date: 2019-07-09 16:50:01.554648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79c9cf29b574'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sc_users',
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('create_time', sa.DATETIME(), nullable=True),
    sa.Column('update_time', sa.DATETIME(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=11), nullable=False),
    sa.Column('ID_card', sa.String(length=18), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sc_users')
    # ### end Alembic commands ###
