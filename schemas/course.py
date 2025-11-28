from typing import Optional

from pydantic import BaseModel as SchemaBaseModel

class CourseSchema(SchemaBaseModel):
    id: Optional[int]
    title: str
    classes: int
    hours: int

    class Config:
        orm_mode = True
