"""
Functions to verify reCAPTCHA challenge
"""
import requests

RECAPTCHA_API_URL = 'https://www.google.com/recaptcha/api/siteverify'

def verify_captcha(secret, response, remoteip = None):
    """Verifies the validity of the reCAPTCHA challenge"""
    params = {'secret': secret, 'response': response}

    if remoteip is not None:
        params['remoteip'] = remoteip

    r = requests.post(RECAPTCHA_API_URL, data=params)

    if r.status_code == requests.codes.ok:
        response = r.json()
        success = response.get('success', False)

        if success:
            return (True, 'Success')
        else:
            return (False, response.get('error-codes', []))
    else:
        return (False, 'API Error')
