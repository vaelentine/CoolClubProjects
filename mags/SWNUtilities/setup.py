from django.core.management import utils

"""
WARNING: Creating a new secret key will wipe out previous data.
Only run this file on first startup o

"""


def get_new_secret_key():
    return utils.get_random_secret_key()


def create_new_env(key):
    f = open(".env", "w+")
    f.write(f'SECRET_KEY = {key}')
    f.close()


if __name__ == '__main__':
    new_key = get_new_secret_key()
    create_new_env(new_key)

