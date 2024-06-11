
from pydantic import BaseModel, ConfigDict, Field


class SLocationAdd(BaseModel):
    name: str = Field(..., description='Название локации')
    description: str = Field(..., description='Краткое описание локации')
    image: str = Field(..., description='Изображение локации')


class SLocation(SLocationAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SLocationId(BaseModel):
    ok: bool = True
    location_id: int


