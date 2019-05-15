import os
from werkzeug import secure_filename

import sys

root = os.path.dirname((os.path.abspath(__file__)))
root += '/static/images'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def upload_file(file):
    if file.filename == '':
        raise Exception('Arquivo sem nome!')

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(root, filename))

    return file
