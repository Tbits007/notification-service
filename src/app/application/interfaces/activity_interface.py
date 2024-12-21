from abc import abstractmethod
from typing import Protocol

from app.domain.entities.activity_entity import ActivityDM


class ActivitySaver(Protocol):
    @abstractmethod
    async def save(self, activity: ActivityDM) -> ActivityDM | None:
        """Сохранить активность в базе данных."""
        ...


class ActivityReader(Protocol):
    @abstractmethod
    async def read_by_id(self, _id: str) -> ActivityDM | None:
        """Получить активность по _id."""
        ...


class ActivityUpdater(Protocol):
    @abstractmethod
    async def update(self, _id: str, update_data: dict) -> ActivityDM | None:
        """Обновить активность по _id."""
        ...

        