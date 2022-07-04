from django.contrib import admin
from django import forms
# Register your models here.
from django.utils.safestring import mark_safe
from home.models import HomeArticleModel, ReviewsModel
from modeltranslation.admin import TranslationAdmin


admin.site.register(ReviewsModel)
admin.site.register(HomeArticleModel)


