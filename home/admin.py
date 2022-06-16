from django.contrib import admin
from django import forms
# Register your models here.
from django.utils.safestring import mark_safe
from home.models import HomeCarouselModel, HomeArticleModel
from modeltranslation.admin import TranslationAdmin



admin.site.register(HomeCarouselModel)

admin.site.register(HomeArticleModel)


