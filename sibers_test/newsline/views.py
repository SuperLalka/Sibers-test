from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views import generic

from .forms import NewNewsForm
from .models import News


class NewsListView(generic.ListView):
    model = News
    template_name = 'news_list.html'

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

    News.objects.get_or_create(header=form.cleaned_data.pop('header'),
                               text=form.cleaned_data.pop('text'))
    if form.cleaned_data:
        for image in form.cleaned_data:
            print(image)
    return HttpResponseRedirect(request.GET['next'])
