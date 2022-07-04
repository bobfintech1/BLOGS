from django import forms
from home.models import  HomeArticleModel, ReviewsModel


class CreateHomeForm(forms.ModelForm):

    class Meta:
        model = HomeArticleModel
        fields = ['title', "body", 'image']


class ReviewsFrom(forms.ModelForm):

    class Meta:
        model = ReviewsModel
        fields = ['text']


class HomeDeleteForm(forms.ModelForm):
    class Meta:
        model = HomeArticleModel
        fields = ['title', "body", "image"]