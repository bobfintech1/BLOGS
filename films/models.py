from uuid import uuid4

from django.db import models

def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'film_archive/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path



# class FilmModle
