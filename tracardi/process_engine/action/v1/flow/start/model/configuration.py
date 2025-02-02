from typing import List, Optional
from pydantic import validator
import json

from tracardi.domain.named_entity import NamedEntity
from tracardi.service.plugin.domain.config import PluginConfig


class Configuration(PluginConfig):
    debug: bool = False
    event_types: List[NamedEntity] = []
    event_id: Optional[str] = None
    event_type: Optional[NamedEntity] = None
    profile_id: Optional[str] = None
    session_id: Optional[str] = None
    properties: Optional[str] = "{}"

    @validator("properties")
    def convert_to_json_id_dict(cls, value):
        if isinstance(value, dict):
            value = json.dumps(value)
        return value

    def get_allowed_event_types(self) -> List[str]:
        return [event.id for event in self.event_types]

    @validator("event_id")
    def remove_whitespaces_from_event_id(cls, value):
        if isinstance(value, str):
            value = value.strip()
        return value

    @validator("profile_id")
    def remove_whitespaces_from_profile_id(cls, value):
        if isinstance(value, str):
            value = value.strip()
        return value

    @validator("session_id")
    def remove_whitespaces_from_session_id(cls, value):
        if isinstance(value, str):
            value = value.strip()
        return value

    @validator("event_type")
    def remove_whitespaces_from_event_type_id(cls, value):
        if isinstance(value, NamedEntity):
            value.id = value.id.strip()
        return value
