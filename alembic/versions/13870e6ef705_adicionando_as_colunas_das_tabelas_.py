"""Adicionando as colunas das tabelas Agreemments e Agreement_values

Revision ID: 13870e6ef705
Revises: f9e7fa88789d
Create Date: 2025-02-25 02:36:39.910578

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '13870e6ef705'
down_revision: Union[str, None] = 'f9e7fa88789d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('agreement_values', sa.Column('valor_inicial_total', sa.Float(), nullable=False))
    op.add_column('agreement_values', sa.Column('valor_inicial_repasse_concedente', sa.Float(), nullable=False))
    op.add_column('agreement_values', sa.Column('valor_inicial_contrapartida_convenente', sa.Float(), nullable=False))
    op.add_column('agreement_values', sa.Column('valor_atualizado_total', sa.Float(), nullable=False))
    op.add_column('agreement_values', sa.Column('valor_pago', sa.Float(), nullable=False))
    op.add_column('agreements', sa.Column('codigo_plano_trabalho', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('agreements', sa.Column('concedente', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('agreements', sa.Column('convenente', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('agreements', sa.Column('objeto', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.create_foreign_key(
        'fk_agreement_values_agreement_id', 
        'agreement_values', 
        'agreements', 
        ['agreement_id'], 
        ['id'], 
        ondelete='CASCADE'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_agreement_values_agreement_id', 'agreement_values', type_='foreignkey')
    op.drop_column('agreements', 'objeto')
    op.drop_column('agreements', 'convenente')
    op.drop_column('agreements', 'concedente')
    op.drop_column('agreements', 'codigo_plano_trabalho')
    op.drop_column('agreement_values', 'valor_pago')
    op.drop_column('agreement_values', 'valor_atualizado_total')
    op.drop_column('agreement_values', 'valor_inicial_contrapartida_convenente')
    op.drop_column('agreement_values', 'valor_inicial_repasse_concedente')
    op.drop_column('agreement_values', 'valor_inicial_total')
    # ### end Alembic commands ###
