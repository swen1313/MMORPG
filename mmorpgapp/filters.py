from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Response


# создаём фильтр

class ResponseFilter(FilterSet):

    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т.е. подбираться) информация о товарах
    class Meta:
        model = Response
        fields = {'advertResponse'}  # поля, которые мы будем фильтровать (т.е. отбирать по каким-то критериям, имена берутся из моделей)