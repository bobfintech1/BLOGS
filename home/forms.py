from django import forms
from home.models import HomeCarouselModel, HomeArticleModel


class CreateHomeForm(forms.ModelForm):

    class Meta:
        model = HomeArticleModel
        fields = ['title', "body", 'image']


class CreateCarouselForm(forms.ModelForm):

    class Meta:
        model = HomeCarouselModel
        fields = ['title', "body", 'image']
