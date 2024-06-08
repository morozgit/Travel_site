from db import LocationOrm, new_session
from fastapi import Depends
from schema_location import SLocation, SLocationAdd
from sqlalchemy import select
from sqlalchemy.orm import Session


class LocationRepository:
    @classmethod
    async def add_one_location(cls, data: SLocationAdd) -> int:
        async with new_session() as session:
            location_dict = data.model_dump()
            
            location = LocationOrm(**location_dict)
            session.add(location)
            await session.flush()
            await session.commit()
            return location.id

    @classmethod
    async def find_all(cls) -> list[SLocation]:
        async with new_session() as session:
            query = select(LocationOrm)
            result = await session.execute(query)
            location_models = result.scalars().all()
            location_schemas = [SLocation.model_validate(location_model) for location_model in location_models]
            return location_schemas
       
    @classmethod
    async def delete_all(cls) -> list[SLocation]:
        async with new_session() as session:
            query = select(LocationOrm)
            result = await session.execute(query)
            location_models = result.scalars().all()
            for location_model in location_models:
                await session.delete(location_model)
            await session.commit()
            location_schemas = [SLocation.model_validate(location_model) for location_model in location_models]
            return location_schemas

