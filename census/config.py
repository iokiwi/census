import os


def parse_boolean(value):
    if type(value) == bool:
        return value
    if value.lower() in ['true', 't', '1', 1]:
        return True
    if value.lower() in ['false', 'f', '0', 0]:
        return False
    return value


# VERIFY_SSL_OR_TLS = parse_boolean(os.environ.get("VERIFY_SSL_OR_TLS", True))
SECRET_TOKEN = os.environ.get("SECRET_TOKEN")
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
print(SQLALCHEMY_DATABASE_URI)