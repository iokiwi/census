import os


def parse_boolean(value):
    if type(value) == bool:
        return value
    if value.lower() in ['true', 't', '1', 1]:
        return True
    if value.lower() in ['false', 'f', '0', 0]:
        return False
    return value


SECRET_TOKEN = os.environ.get("SECRET_TOKEN")
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
