from typing import Optional
from pydantic import BaseModel, Field

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
