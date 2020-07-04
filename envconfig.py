import os

def set_env_variables():
    # Media and static file Storage configurations
    os.environ['STORAGE_ACCOUNT_NAME'] = 'pydaystorageaccount'
    os.environ['STORAGE_ACCOUNT_KEY']  = 'cDCNj6Cjlf3IP2hamZ3RiipSHq+AmBJU8cFIlN72M5vE6cBlejdvSUpodvjgV/z03nM7fd+etQ8Liw/I6zqXKQ=='
    os.environ['STORAGE_ACCOUNT_DOMAIN'] = 'pydaystorageaccount.blob.core.windows.net'
    os.environ['STORAGE_MEDIA_CONTAINER'] = 'media'
    os.environ['STORAGE_STATIC_CONTAINER'] = 'static'

    # Postgre Database configuration
    os.environ['DATABASE_ENGINE'] = 'django.db.backends.postgresql'
    os.environ['DATABASE_NAME'] = 'contactdb'
    os.environ['DATABASE_USERNAME'] = 'labuser@azurepython'
    os.environ['DATABASE_PASSWORD'] = 'Password123'
    os.environ['DATABASE_HOST'] = 'azurepython.postgres.database.azure.com'
    os.environ['DATABASE_PORT'] = '5432'

    # Application insights configuration
    os.environ['APP_INSIGHTS_iNSTRUMENTATION_KEY'] = '0d5096cc-9547-4c61-a887-060b97cc90d7'

    print('Following environment variables set....')
    print(f"STORAGE_ACCOUNT_NAME = {os.environ.get('STORAGE_ACCOUNT_NAME')}")
    print(f"STORAGE_ACCOUNT_KEY = {os.environ.get('STORAGE_ACCOUNT_KEY')}")
    print(f"STORAGE_ACCOUNT_DOMAIN = {os.environ.get('STORAGE_ACCOUNT_DOMAIN')}")
    print(f"STORAGE_MEDIA_CONTAINER = {os.environ.get('STORAGE_MEDIA_CONTAINER')}")
    print(f"STORAGE_STATIC_CONTAINER = {os.environ.get('STORAGE_STATIC_CONTAINER')}")

    print(f"DATABASE_ENGINE = {os.environ.get('DATABASE_ENGINE')}")
    print(f"DATABASE_NAME = {os.environ.get('DATABASE_NAME')}")
    print(f"DATABASE_USERNAME = {os.environ.get('DATABASE_USERNAME')}")
    print(f"DATABASE_PASSWORD = {os.environ.get('DATABASE_PASSWORD')}")
    print(f"DATABASE_HOST = {os.environ.get('DATABASE_HOST')}")
    print(f"DATABASE_PORT = {os.environ.get('DATABASE_PORT')}")

    print(f"APP_INSIGHTS_iNSTRUMENTATION_KEY = {os.environ.get('APP_INSIGHTS_iNSTRUMENTATION_KEY')}")

