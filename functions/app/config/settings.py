from dotenv import load_dotenv
import getpass
import os

load_dotenv()

if "GOOGLE_API_KEY" not in os.environ or not os.environ["GOOGLE_API_KEY"]:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Provide your Google API key here: ")

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    DB_NAME = os.getenv("DB_NAME")
    DB_COLLECTION_NAME = os.getenv("DB_COLLECTION_NAME")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    @staticmethod
    def validate():
        missing = []
        if not Config.MONGO_URI:
            missing.append("MONGO_URI")
        if not Config.DB_NAME:
            missing.append("DB_NAME")
        if not Config.DB_COLLECTION_NAME:
            missing.append("DB_COLLECTION_NAME")
        if not Config.GOOGLE_API_KEY:
            missing.append("GOOGLE_API_KEY")
        
        if missing:
            raise EnvironmentError(
                f"The following environment variables are missing: {', '.join(missing)}"
            )

try:
    Config.validate()
except EnvironmentError as e:
    print(f"Error: {e}")
    exit(1)
