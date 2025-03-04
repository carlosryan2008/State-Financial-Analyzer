"""initial migration

Revision ID: f9e7fa88789d
Revises: 
Create Date: 2025-02-12 10:28:09.654147

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f9e7fa88789d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agreements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contracts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('accountability',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('agreement_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['agreement_id'], ['agreements.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('administrative_processes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contract_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contract_id'], ['contracts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('agreement_dates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('agreement_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['agreement_id'], ['agreements.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('agreement_values',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('agreement_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['agreement_id'], ['agreements.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contract_dates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contract_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contract_id'], ['contracts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contract_values',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contract_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contract_id'], ['contracts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contract_values')
    op.drop_table('contract_dates')
    op.drop_table('agreement_values')
    op.drop_table('agreement_dates')
    op.drop_table('administrative_processes')
    op.drop_table('accountability')
    op.drop_table('contracts')
    op.drop_table('agreements')
    # ### end Alembic commands ###
