import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME = 'Car Price API'
    API_KEY = os.getenv('API_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY','secret')
    JWT_ALGO = 'HS256'
    REDDIS_URL = os.getenv('REDDIS_URL','redis://localhost:6379')
    MODEL_PATH = 'app/model/model.pkl'



settings = Settings()
