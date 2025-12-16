from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class MessageModel(BaseModel):
    """Model for messages

    Args:
        BaseModel (pydantic model)
    """
    role: str
    content: str
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class ChatModel(BaseModel):
    """Chat Model that is returned by the API

    Args:
        BaseModel (pydantic model)
    """
    chat: list[MessageModel]
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
