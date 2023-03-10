"""added background pic

Revision ID: 5d36b3a454c4
Revises: 426ec5edf22d
Create Date: 2023-01-14 20:02:24.815096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d36b3a454c4'
down_revision = '426ec5edf22d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('profile_background', sa.String(length=300), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('profile_background')

    # ### end Alembic commands ###
