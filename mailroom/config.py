'''
Default configurations
'''
from mailroom.mailroom import app
import os

# Defines the URI of the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.instance_path, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRETS = {
    'recaptcha': '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe',
    'mailer': {
        'host': '',
        'username': '',
        'password': '',
        'sender': '',
    },
}
