from typing import Annotated

from fastapi import APIRouter, Depends
from repository_location import LocationRepository
from repository_track import TrackRepository
from schema_location import SLocation, SLocationAdd, SLocationId

location_router = APIRouter(
    prefix="/location",
    tags=["Локации"],
)

@location_router.post("")
async def add_location(
        location: Annotated[SLocationAdd, Depends()],
) -> SLocationId:
    location_id = await LocationRepository.add_one_location(location)
    
    return {"ok": True, "location_id": location_id}


@location_router.get("/all_location")
async def get_locations() -> list[SLocation]:
    locations = await LocationRepository.find_all()
    return locations


@location_router.get("/{location}")
async def get_location(location: int):
    locations = await TrackRepository.get_location_tracks()
    print('locations', location)
    # return tracks

@location_router.post("/delete_location")
async def delete_all_location() -> list[SLocation]:
    locations = await LocationRepository.delete_all()
    return locations

