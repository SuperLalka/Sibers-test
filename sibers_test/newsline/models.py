from django.db import models

from tinymce.models import HTMLField

from sibers_test import constants


class News(models.Model):
    header = models.CharField(max_length=100, help_text='Enter news title')
    text = HTMLField(help_text='Enter news text')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    type = models.CharField(max_length=3, choices=constants.NEWS_STATUS,
                            help_text="Select news status", default="pre")

    def __str__(self):
        return '{0} / {1}'.format(self.created_at, self.header)

    def get_news_images(self):
        return Image.objects.filter(for_news=self)

    class Meta:
        verbose_name_plural = 'News'


class Image(models.Model):
    name = models.CharField(max_length=120)
    filename = models.CharField(max_length=255, null=True, blank=True)
    file = models.ImageField(upload_to="images")
    for_news = models.ForeignKey('News', on_delete=models.CASCADE,
                                 null=True, blank=True)
