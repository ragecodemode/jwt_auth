from pydantic import BaseModel


class TokenInfo(BaseModel):
    access_toke: str
    token_type: str
