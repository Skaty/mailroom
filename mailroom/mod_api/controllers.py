from flask import Blueprint, request, jsonify

from .models import Mailbox

keys = {}

mod_api = Blueprint('main', __name__, url_prefix='/api')

@mod_api.record_once
def record_keys(setup_state):
    global keys
    app = setup_state.app
    keys = app.config.get('KEYS', {})

@mod_api.route('/mailboxes', methods=['GET'])
def list_mailboxes():
    return_fields = ['id', 'name']
    response = [x.as_dict(return_fields) for x in Mailbox.query.all()]
    return jsonify(response)

@mod_api.route('/send', methods=['GET','POST'])
def send_message():
    pass
