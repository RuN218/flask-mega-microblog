import json
import requests

from flask import current_app
from flask_babel import _


def translate(text, source_language, dest_language):
    if 'YA_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['YA_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')

    # auth = {'Ocp-Apim-Subscription-Key': app.config['YA_TRANSLATOR_KEY']}
    r = requests.get(
        f"""https://translate.yandex.net/api/v1.5/tr.json/translate
        ? [key={current_app.config['YA_TRANSLATOR_KEY']}]
        & [text={text}]
        & [lang={source_language}-{dest_language}]"""
    )
    if r.status_code != 200:
        return _('Error: the translation service failed.')

    return json.loads(r.content.decode('utf-8-sig'))
