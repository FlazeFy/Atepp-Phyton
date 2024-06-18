from configs.configs import meta
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import String,DateTime,SmallInteger

model_all_endpoint=Table(
    'endpoint',meta,
    Column('id',String(36),primary_key=True),
    Column('project_id',String(36)),

    # Props
    Column('created_at',DateTime),
    Column('created_by',String(36)),
)