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
        'NAME': 'dc54al2keh8qn7',
        'USER': 'xzboirdjtlychz',
        'PASSWORD': 'ODuvlajUXPFO99PH49xzknEQzy',
        'HOST': 'ec2-54-83-202-218.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
