from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.api.serializers import HomePostSerializer
from home.models import *
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def home_api_view(request):
    blogs = HomeArticleModel.objects.all()
    serializer = HomePostSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_home_api(request):
    serializer = HomePostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def home_detail_api_view(request, pk):
    blogs = get_object_or_404(HomeArticleModel, pk=pk)
    serializer = HomePostSerializer(blogs)

    return Response(serializer.data)


@api_view(['DELETE',])
def home_delete_api_view(request, pk):
    blogs = get_object_or_404(HomeArticleModel, pk=pk)
    serializer = HomePostSerializer(blogs)
    blogs.delete()
    return Response(serializer.data)

