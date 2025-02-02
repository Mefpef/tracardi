from pydantic import BaseModel

from tracardi.service.valiadator import validate_email


class Credentials(BaseModel):
    username: str
    password: str
    token: str
    needs_admin: bool

    def empty(self) -> bool:
        return self.password == "" or self.username == ""

    def username_as_email(self) -> bool:
        return validate_email(self.username)
