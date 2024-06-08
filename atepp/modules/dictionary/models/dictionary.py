from typing import Optional
from pydantic import BaseModel, Field

class Dictionary(BaseModel):
    id: str = Field(..., min_length=36, max_length=36)
    dictionary_type: str = Field(..., max_length=36)
    dictionary_name: str = Field(..., max_length=75)
    dictionary_value: Optional[str] = Field(None, max_length=500)

    # Props
    created_at: str
    created_by: str = Field(..., max_length=36)
    updated_at: Optional[str] = None
