from configs.configs import meta
from sqlalchemy import Table,Column,JSON
from sqlalchemy.sql.sqltypes import String,DateTime,Boolean

user=Table(
    'user',meta,
    Column('id',String(36),primary_key=True),
    Column('username',String(36)),
    Column('email',String(144)),
    Column('company',String(75), nullable=True),
    Column('social_media',JSON, nullable=True),
    Column('job',String(75)),
    Column('phone',String(18), nullable=True),
    
    Column('created_at',DateTime),
    Column('updated_at',DateTime, nullable=True),
)