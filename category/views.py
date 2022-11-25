from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer, CharField, IntegerField
from .models import Category, News
from rest_framework.views import APIView
from .serializers import NewsCreateSerializer, NewsListSerializer

class NewsListAPIView(APIView):
    def get(self, request):
        news = [{"id": i.id, "title": i.title} for i in News.objects.all()
                ]
        # news = News.objects.all()
        return Response(news)



@api_view(['POST'])
def news_create(request):
    serializer = NewsCreateSerializer(data=request.POST)
    serializer.is_valid()

    category = Category.objects.get(id=serializer.validated_data['category_id'])

    news = News.objects.create(
        title=serializer.validated_data['title'],
        category=category,
    )
    return Response(serializer.data)

