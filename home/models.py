from uuid import uuid4

from django.db import models

# Create your models here.
from django.urls import reverse

from accounts.models import Account


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'home_archive/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path


class HomeCarouselModel(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('home:home_lis t')


    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url


class HomeArticleModel(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('home:home_list')


    @property
    def imageURL(self):
        try:
            url =str(self.image.url)
        except:
            url = ''
        return url
