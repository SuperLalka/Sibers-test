from django import forms
from django.contrib import admin
from django.db import models
from django.forms import TextInput

from newsline.models import News, Image


class NewsImagesForm(forms.ModelForm):
    image_1 = forms.ImageField(required=False)
    image_2 = forms.ImageField(required=False)
    image_3 = forms.ImageField(required=False)
    image_4 = forms.ImageField(required=False)
    image_5 = forms.ImageField(required=False)

    def save(self, *args, **kwargs):

        if not self.instance.id:
            news = News.objects.create(
                header=self.cleaned_data['header'],
                text=self.cleaned_data['text'],
                type=self.cleaned_data['type'])
            news.save()
            self.instance = news

        for image in self.files:
            image_obj, _ = Image.objects.get_or_create(
                name="photo_to_news_" + self.instance.header.replace(" ", "_"),
                filename=self.files[image].name,
                file=self.files[image],
                for_news=self.instance
            )

        return super(NewsImagesForm, self).save(*args, **kwargs)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'header', 'created_at', 'type')
    list_filter = ('type',)
    search_fields = ['header']
    form = NewsImagesForm
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})}
    }


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'filename')
