from rest_framework import serializers
from home.models import *


class HomePostSerializer(serializers.ModelSerializer):

    # email = serializers.SerializerMethodField('get_username_from_author')

    class Meta:
        model = HomeArticleModel
        fields = ['title', 'body', 'image', 'date_updated']

    # def get_username_from_author(self, home_post):
    #     email = home_post.author.email
    #     return email


class ReviewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewsModel
        fields = '__all__'
