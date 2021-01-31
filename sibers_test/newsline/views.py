from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views import generic

from .forms import NewNewsForm
from .models import Image, News


class NewsListView(generic.ListView):
    model = News
    paginate_by = 10
    template_name = 'news_list.html'
    queryset = News.objects.filter(type='act')

    def get_paginator(self, queryset, per_page, orphans=0,
                      allow_empty_first_page=True, **kwargs):
        return self.paginator_class(
            queryset, per_page=self.request.session.get('pagination', 10), orphans=orphans,
            allow_empty_first_page=allow_empty_first_page, **kwargs)

    def get_context_data(self, **kwargs):
        context = {
            'time_now': datetime.now().strftime("%A, %d. %B %Y"),
            'new_news_form': NewNewsForm(),
            **kwargs
        }
        return super().get_context_data(**context)


def add_news(request):
    form = NewNewsForm(request.POST)
    if not form.is_valid():
        return redirect(request.GET['next'])

    news, _ = News.objects.get_or_create(
        header=form.cleaned_data.pop('header'),
        text=form.cleaned_data.pop('text')
    )
    if request.FILES:
        for image in request.FILES:
            Image.objects.create(
                name="photo_to_news_" + news.header.replace(" ", "_"),
                filename=request.FILES[image].name,
                file=image,
                for_news=news
            )
    return HttpResponseRedirect(request.GET['next'])


def change_pagination(request, per_page):
    request.session['pagination'] = int(per_page)
    return HttpResponseRedirect('news')
