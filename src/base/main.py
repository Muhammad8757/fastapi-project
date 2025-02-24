from src.base.abstracts.app import app
from src.base.engine import engine
from src.base.abstracts.models import Base
from src.apps.accounts.views.users import register
Base.metadata.create_all(bind=engine)

