from db import LocationOrm, TrackOrm, new_session
from fastapi import Depends
from schema_track import STrack, STrackAdd
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload


class TrackRepository:
    @classmethod
    async def add_one_track(cls, data: STrackAdd) -> int:
        async with new_session() as session:
            track_dict = data.model_dump()            
            location = await session.get(LocationOrm, track_dict['location_id'])
            if not location:
                print(f"Location with id {track_dict['location_id']} does not exist.")
                raise ValueError(f"Location with id {track_dict['location_id']} does not exist.")
            
            track = TrackOrm(**track_dict)
            session.add(track)
            await session.flush()
            await session.commit()
            return track.id


    @classmethod
    async def get_location_tracks(cls, location_id: int) -> list[STrack]:
        async with new_session() as session:
            query = select(TrackOrm).filter(TrackOrm.location_id == location_id)
            result = await session.execute(query)
            track_models = result.scalars().all()
            track_schemas = [STrack.model_validate(track_model) for track_model in track_models]
            return track_schemas
