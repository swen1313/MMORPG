from django.forms import ModelForm
from .models import Advert, Response


# Создаём модельную форму
class AdvertForm(ModelForm):
    # в класс мета, как обычно, надо написать модель, по которой будет строиться форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Advert
        fields = ['userWho', 'postType', 'header', 'text']


class ResponseForm(ModelForm):

    class Meta:
        model = Response
        fields = ['advertResponse', 'userTo', 'text']