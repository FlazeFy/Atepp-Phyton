from typing import Optional
from pydantic import BaseModel, Field

class Project(BaseModel):
    id: str = Field(..., min_length=36, max_length=36)
    project_slug: str = Field(..., max_length=85)
    project_title: str = Field(..., max_length=75)
    project_category: str = Field(..., max_length=36)
    project_type: str = Field(..., max_length=14)
    project_desc: Optional[str] = Field(None, max_length=1000)
    project_main_lang: Optional[str] = Field(None, max_length=36)
    project_pin_code: Optional[str] = Field(None, min_length=6, max_length=6)

    # Props
    created_at: str
    created_by: str = Field(..., max_length=36)
    updated_at: Optional[str] = None
    updated_by: Optional[str] = None
    deleted_at: Optional[str] = None
    deleted_by: Optional[str] = None
