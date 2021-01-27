from django import forms

from tinymce.widgets import TinyMCE


REQUIRED = "Это поле является обязательным для заполнения"
OPTIONAL = "Необязательное поле"


class NewNewsForm(forms.Form):
    header = forms.CharField(label="Название новости", max_length=100, help_text=REQUIRED)
    text = forms.CharField(label="Текст новости", help_text=REQUIRED,
                           widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    image_1 = forms.ImageField(label="Иллюстрация к новости", required=False, help_text=OPTIONAL)
    image_2 = forms.ImageField(label="Иллюстрация к новости", required=False, help_text=OPTIONAL)
    image_3 = forms.ImageField(label="Иллюстрация к новости", required=False, help_text=OPTIONAL)
    image_4 = forms.ImageField(label="Иллюстрация к новости", required=False, help_text=OPTIONAL)
    image_5 = forms.ImageField(label="Иллюстрация к новости", required=False, help_text=OPTIONAL)
