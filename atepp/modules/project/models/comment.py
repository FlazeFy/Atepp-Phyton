from configs.configs import meta
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import String,DateTime,JSON

model_all_comment=Table(
    'comment',meta,
    Column('id',String(36),primary_key=True),
    Column('endpoint_id',String(36)),
    Column('comment_context',String(36)),
    Column('comment_body',String(255)),
    Column('comment_attachment',JSON,nullable=True),

    # Props
    Column('created_at',DateTime),
    Column('created_by',String(36)),
)