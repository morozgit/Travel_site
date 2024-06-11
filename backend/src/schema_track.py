import datetime

from pydantic import BaseModel, ConfigDict, Field
from schema_location import SLocation


class STrackAdd(BaseModel):
    name: str = Field(..., description='Название маршрута')
    description: str = Field(..., description='Краткое описание маршрута')
    image: str = Field(..., description='Изображение маршрута')
    # created_at: str = Field(default=str(datetime.datetime.now), description='Дата время создания маршрута')
    # updated_at: str = Field(default=str(datetime.datetime.now), description='Дата время обновления маршрута')
    location_id: int = Field(..., description='Название локации')

    # class Config:
    #     arbitrary_types_allowed = True


class STrack(STrackAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STrackId(BaseModel):
    ok: bool = True
    track_id: int
