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
        super(NewsImagesForm, self).save(*args, **kwargs)

        if not self.instance.id:
            news = News.objects.create(header=self.cleaned_data['header'],
                                       text=self.cleaned_data['text'],
                                       in_the_archive=self.cleaned_data['in_the_archive'])
            news.save()
            self.instance = news

        for image in self.files:
            if self.files[image].name not in self.instance.images.all():
                # print(self.instance.images.all(), self.files[image].name)
                image_obj, _ = Image.objects.get_or_create(
                    name="photo_to_news_" + self.instance.header.replace(" ", "_"),
                    filename=self.files[image].name,
                    images=self.files[image]
                )
                self.instance.images.add(image_obj)

        return self.instance


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
