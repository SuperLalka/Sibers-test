from django.urls import path

from . import views


app_name = 'newsline'
urlpatterns = [
    path('news/', views.NewsListView.as_view(), name='news'),
    path('news/add-news', views.add_news, name='add-news'),
]
