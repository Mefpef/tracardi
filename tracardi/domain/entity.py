from typing import Optional
from uuid import uuid4
from pydantic import BaseModel
# import tracardi.service.storage.crud as crud
from tracardi.domain.value_object.storage_info import StorageInfo


class Entity(BaseModel):
    id: str

    # def storage(self, index) -> 'crud.EntityStorageCrud':
    #     return crud.EntityStorageCrud(index, entity=self)

    @staticmethod
    def new() -> 'Entity':
        return Entity(id=str(uuid4()))

    @staticmethod
    def storage_info() -> Optional[StorageInfo]:
        return None
