__author__ = 'osw4l'

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

local = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


heroku = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd3v0ik2pnveagn',
        'USER': 'vlmhdhezimwxrk',
        'PASSWORD': 'uJwPWYl6AwWShvCZ7rrVIBr1Xv',
        'HOST': 'ec2-107-21-221-59.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
