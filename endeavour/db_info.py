__author__ = 'osw4l'

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

local = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

import dj_database_url
heroku = {
    'default': dj_database_url.config(
        default=os.environ["DATABASE_URL"]
    )
}
