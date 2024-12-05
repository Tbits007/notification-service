from dataclasses import dataclass
from datetime import datetime
from typing import Self
from uuid import UUID

from app.domain.base.entity import DomainEntity

from app.domain.notification.value_objects import NotificationId, UserId, Content, CreatedAt


@dataclass(kw_only=True)
class Notification(DomainEntity[UserId]):
    user_id: UserId
    content: Content
    created_at: CreatedAt

    @classmethod
    def create(cls, *, notification_id: UUID, user_id: UUID, content: str, created_at: datetime) -> Self:
        return cls(
            id_=NotificationId(notification_id),
            user_id=UserId(user_id),
            content=Content(content),
            created_at=CreatedAt(created_at),
        )
