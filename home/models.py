from uuid import uuid4

from django.db import models

# Create your models here.
from django.urls import reverse
from Blogs import settings
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
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

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


class ReviewsModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comment', on_delete=models.SET_NULL, null=True)
    text = models.TextField('Comment', max_length=5000)
    article = models.ForeignKey(HomeArticleModel, verbose_name='Film', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author)

