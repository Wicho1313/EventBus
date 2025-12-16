from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class MessageModel(BaseModel):
    role: str
    content: str
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class ChatModel(BaseModel):
    chat: list[MessageModel]
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
