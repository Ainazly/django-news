from django.urls import path

from .import views

urlpatterns = [
    path('news-create/', views.news_create),
    path('new-list/', views.NewsListAPIView.as_view()),

]