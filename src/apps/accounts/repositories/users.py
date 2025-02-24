from src.apps.accounts.models.user import User
from src.base.abstracts.repositories import AbstractRepository


class UserRepository(AbstractRepository[User]):
    def __init__(self):
        super().__init__(User)

user_repository = UserRepository()