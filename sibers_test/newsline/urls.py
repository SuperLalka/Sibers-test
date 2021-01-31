from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import RedirectView

from . import views


app_name = 'newsline'
urlpatterns = [
    url(r'news/change_pagination/(?P<per_page>\d+)', views.change_pagination, name='change_pagination'),
    url(r'news/add-news', views.add_news, name='add-news'),
    url(r'news/(?P<page>\d+)?', views.NewsListView.as_view(), name='news'),
    url(r'', RedirectView.as_view(url='/news/', permanent=True)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
