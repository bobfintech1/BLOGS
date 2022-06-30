from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from home.api.serializers import HomePostSerializer, ReviewsSerializer
from home.models import *
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def home_api_view(request):
    paginator = PageNumberPagination()
    paginator.page_size = 1
    blogs = HomeArticleModel.objects.all()
    blogs = paginator.paginate_queryset(blogs, request)
    serializer = HomePostSerializer(blogs, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def create_home_api(request):
    serializer = HomePostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def home_detail_api_view(request, pk):
    home = get_object_or_404(HomeArticleModel, pk=pk)
    serializer = HomePostSerializer(home)

    return Response(serializer.data)


@api_view(['DELETE',])
def home_delete_api_view(request, pk):
    blogs = get_object_or_404(HomeArticleModel, pk=pk)
    serializer = HomePostSerializer(blogs)
    blogs.delete()
    return Response(serializer.data)


# @api_view(['POST'])
# def comment_create_view(request):
#     user = request.user
#     article = get_object_or_404(ReviewsSerializer)
#
#     comment = ReviewsSerializer(data=request.data)
#     if comment.is_valid():
#         comment.author = user
#         comment.article = article
#         comment.save()
#         return Response(status=201)
#     return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)


# class CommentCreate(APIView):
#     def post(self, request):
#         comment = ReviewsSerializer(data=request.data)
#         if comment.is_valid():
#             comment.save()
#         return Response(status=201)



@api_view(['GET'])
def comments_home_view(request, pk):
    comments = ReviewsModel.objects.filter(article_id=pk)
    serializer = ReviewsSerializer(comments, many=True)
    return Response(serializer.data)




@api_view(['GET', 'POST'])
def comment_create_view(request):
    user = request.user

    if request.method == 'GET':
        snippets = HomeArticleModel.objects.all()
        serializer = HomePostSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewsSerializer(data=request.data)
        serializer.author = user
        serializer.article = serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)