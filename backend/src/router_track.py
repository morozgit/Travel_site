from typing import Annotated

from fastapi import APIRouter, Depends
from repository_track import TrackRepository
from schema_track import STrack, STrackAdd, STrackId

track_router = APIRouter(
    prefix="/track",
    tags=['Маршруты'],
)


@track_router.post("")
async def add_track(
        track: Annotated[STrackAdd, Depends()],
) -> STrackId:
    track_id = await TrackRepository.add_one_track(track)
    
    return {"ok": True, "track_id": track_id}


@track_router.get("/location/{location_id}")
async def get_tracks(location_id: int) -> list[STrack]:
    tracks = await TrackRepository.get_location_tracks(location_id)
    return tracks
