import os


def get_db_credentials():
    return {
        'provider': os.getenv('DB_DRIVER'),
        'host': os.getenv('POSTGRES_HOST'),
        'user': os.getenv('POSTGRES_USER'),
        'password': os.getenv('POSTGRES_PASSWORD'),
        'port': os.getenv('POSTGRES_PORT'),
        'database': os.getenv('POSTGRES_DB'),
    }

