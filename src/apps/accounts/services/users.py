import bcrypt
from pydantic import ValidationError
from src.apps.accounts.dtos.dto import UserCreateDto
from src.apps.accounts.repositories.users import UserRepository, user_repository
from src.base.abstracts.services import AbstractCRUDService
from sqlalchemy import or_

class UserService(AbstractCRUDService[UserRepository]):
    def __init__(self, repository: UserRepository = user_repository):
        self.repository = repository
        super().__init__(repository)

    def create(self, dto: UserCreateDto):
        self._validate(dto)
        return super().create(dto)
    
    def _validate(self, dto: UserCreateDto):
        if self.repository.filter(email=dto.email, username=dto.username):
            raise ValidationError("User already exists")

    def get_hash(self, password: str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode("utf-8"), salt)
    
    def verify_password(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))

user_service = UserService()