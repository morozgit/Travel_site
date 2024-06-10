import datetime
from typing import Annotated

from sqlalchemy import ForeignKey, text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

URL_DATABASE = 'postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/postgres'
engine = create_async_engine(URL_DATABASE, echo=True)
new_session = async_sessionmaker(engine, expire_on_commit=False)

created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
                        server_default=text("TIMEZONE('utc', now())"),
                        onupdate=datetime.datetime.now(),
                      )]

class Base(DeclarativeBase):
    pass


class LocationOrm(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]
    image: Mapped[str | None]
    track: Mapped[list["TrackOrm"]] = relationship(
        back_populates="location",
    )


class TrackOrm(Base):
    __tablename__ = "tracks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]
    image: Mapped[str | None]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    location_id: Mapped[int] = mapped_column(ForeignKey("locations.id", ondelete="CASCADE"))
    location: Mapped["LocationOrm"] = relationship(
        back_populates="track",
    )


