import os
from dotenv import load_dotenv

load_dotenv()


#==========DATABASE==========
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")


