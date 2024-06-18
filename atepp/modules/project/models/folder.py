from typing import Optional
from pydantic import BaseModel, Field
from configs.configs import meta
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import String,DateTime,JSON

class Folder(BaseModel):
    id: str = Field(..., min_length=36, max_length=36)
    project_id: str = Field(..., min_length=36, max_length=36)
    folder_slug: str = Field(..., max_length=46)
    folder_name: str = Field(..., max_length=36)
    folder_pin_code: Optional[str] = Field(None, min_length=6, max_length=6)
    folder_desc: Optional[str] = Field(None, max_length=144)

    # Props
    created_at: str
    created_by: str = Field(..., max_length=36)
    updated_at: Optional[str] = None
    updated_by: Optional[str] = None
    deleted_at: Optional[str] = None
    deleted_by: Optional[str] = None

model_all_folder=Table(
    'folder',meta,
    Column('id',String(36),primary_key=True),
    Column('project_id',String(36)),
    Column('folder_slug',String(46)),
    Column('folder_name',String(36)),
    Column('folder_pin_code',String(36),nullable=True),
    Column('folder_desc',String(144),nullable=True),

    # Props
    Column('created_at',DateTime),
    Column('created_by',String(36)),
)