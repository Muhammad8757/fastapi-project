from pydantic import BaseModel


class ModelDto(BaseModel):
    def to_dict(self):
        return self.model_dump()

