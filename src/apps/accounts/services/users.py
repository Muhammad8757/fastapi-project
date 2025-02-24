
from src.apps.accounts.repositories.users import UserRepository, user_repository
from src.base.abstracts.services import AbstractCRUDService


class UserService(AbstractCRUDService[UserRepository]):
    def __init__(self, repository: UserRepository = user_repository):
        super().__init__(repository)

user_service = UserService()