from django.db import models

from tinymce.models import HTMLField

from sibers_test import constants


class News(models.Model):
    header = models.CharField(max_length=100, help_text='Enter news title')
    text = HTMLField(help_text='Enter news text')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    images = models.ManyToManyField('Image', null=True, blank=True)
    type = models.CharField(max_length=3, choices=constants.NEWS_STATUS,
                            help_text="Select news status", default="pre")

    def __str__(self):
        return '{0} / {1}'.format(self.created_at, self.header)

    class Meta:
        verbose_name_plural = 'News'


class Image(models.Model):
    name = models.CharField(max_length=120)
    filename = models.CharField(max_length=255, null=True, blank=True)
    images = models.ImageField(upload_to="images")
