"""adding r/ship

Revision ID: b6697a9006b0
Revises: 98dbac25cacc
Create Date: 2018-04-23 13:01:47.283405

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b6697a9006b0'
down_revision = '98dbac25cacc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('subtitle', sa.String(length=50), nullable=True),
    sa.Column('author', sa.String(length=20), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.String(length=20), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('comments')
    op.drop_table('posts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('posts_id_seq'::regclass)"), nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('subtitle', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('author', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('date_posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('content', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='posts_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('comments',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('author', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('date_posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('comment', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name='comments_post_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='comments_pkey')
    )
    op.drop_table('comment')
    op.drop_table('post')
    # ### end Alembic commands ###