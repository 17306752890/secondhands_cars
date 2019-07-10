"""empty message

Revision ID: de8922a7f535
Revises: 8a4c58f66b4b
Create Date: 2019-07-10 16:01:10.146690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de8922a7f535'
down_revision = '8a4c58f66b4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sc_order',
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('create_time', sa.DATETIME(), nullable=True),
    sa.Column('update_time', sa.DATETIME(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('sc_users_id', sa.Integer(), nullable=True),
    sa.Column('car_name', sa.Integer(), nullable=True),
    sa.Column('order_time', sa.DateTime(), nullable=True),
    sa.Column('car_price', sa.Float(), nullable=True),
    sa.Column('service_charge', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['car_name'], ['sc_car.id'], ),
    sa.ForeignKeyConstraint(['sc_users_id'], ['sc_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sc_order')
    # ### end Alembic commands ###
