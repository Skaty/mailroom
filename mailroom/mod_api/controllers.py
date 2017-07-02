from flask import Blueprint, request

from .models import Mailbox

mod_api = Blueprint('main', __name__, url_prefix='/api')

@mod_api.route('/send', methods=['GET','POST'])
def send_message():
    pass
