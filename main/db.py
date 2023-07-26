from sqlalchemy import create_engine
from decouple import config

engine = create_engine(config('DB_CONNECTION'), echo=False)

