from src.app.domain.base.value_objects import DomainValueObject
from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class NotificationId(DomainValueObject):
    value: UUID


@dataclass(frozen=True)
class UserId(DomainValueObject):
    value: UUID


@dataclass(frozen=True)
class Content(DomainValueObject):
    value: str


@dataclass(frozen=True)
class CreatedAt(DomainValueObject):
    value: datetime

        