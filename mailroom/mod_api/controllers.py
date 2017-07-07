from flask import Blueprint, request, jsonify, abort

from mailroom.common.utils import recaptcha, mailer

from .models import Mailbox, Mailgroup

SECRETS = {}

mod_api = Blueprint('main', __name__, url_prefix='/api')

@mod_api.record_once
def record_keys(setup_state):
    global SECRETS
    app = setup_state.app
    SECRETS = app.config.get('SECRETS', {})

@mod_api.route('/mailboxes', methods=['GET'])
def list_mailboxes():
    groups = Mailgroup.query.all()
    return jsonify([group.serialize for group in groups])

@mod_api.route('/send', methods=['GET','POST'])
def send_message():
    mailbox = Mailbox.query.get_or_404(request.form.get('mailbox', -1))

    captcha_challenge = request.form.get('g-recaptcha-response', None)
    captcha_response = recaptcha.verify_captcha(SECRETS['recaptcha'], captcha_challenge)

    if not captcha_response[0]:
        return 'Invalid CAPTCHA', 404

    if not mailbox.is_visible:
        return 'Invalid mailbox', 404

    subject = 'New mail from {} mailbox'.format(mailbox.name)

    # Prepare the message to be sent
    content_dict = request.form.to_dict(flat=False)
    flat_dict = {k: ' '.join(v) for k, v in content_dict.items()}

    message = mailbox.template.format(**flat_dict)

    success = mailer.send_mail(SECRETS['mailer'], mailbox.email, subject, message)

    if success:
        return "Mail sent successfully!"
    else:
        return "Something went wrong while sending the message", 500
