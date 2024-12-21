from dataclasses import dataclass


@dataclass(slots=True)
class ActivityDM:
    email: str
    action_type: str
    details: str | None = None

