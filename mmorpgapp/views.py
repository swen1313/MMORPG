import random
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import AdvertForm, ResponseForm
from .models import Advert, Response, Category
from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from .filters import ResponseFilter
from django.core.mail import send_mail


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'mmorpgapp/registerpage.html'

class AdvertList(ListView):
    model = Advert # указываем модель, объекты которой мы будем выводить
    template_name = 'mmorpgapp/advertlist.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'adverts'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    form_class = AdvertForm
    queryset = Advert.objects.order_by('-id')

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон.
    # В возвращаемом словаре context будут храниться все переменные.
    # Ключи этого словари и есть переменные, к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['categories'] = Category.objects.all()
        context['form'] = AdvertForm()
        return context


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не накосячил, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)


class AdvertDetail(DetailView):
    model = Advert # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'mmorpgapp/advertedit.html' # название шаблона будет product.html
    context_object_name = 'advert' # название объекта
    queryset = Advert.objects.all()

class ResponseList(ListView):
    model = Response  # указываем модель, объекты которой мы будем выводить
    template_name = 'mmorpgapp/responselist.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'responses'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    form_class = ResponseForm
    queryset = Response.objects.order_by('-id')

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон.
    # В возвращаемом словаре context будут храниться все переменные.
    # Ключи этого словари и есть переменные, к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['form'] = ResponseForm()
        context['filter'] = ResponseFilter(self.request.GET, queryset=self.get_queryset())

        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не накосячил, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)

class ResponseDetail(DetailView):
    model = Response  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'mmorpgapp/responseedit.html'  # название шаблона будет product.html
    context_object_name = 'response'  # название объекта
    queryset = Response.objects.all()


class AdvertUpdateView(UpdateView):
    template_name = 'mmorpgapp/advertupdate.html'
    form_class = AdvertForm
    success_url = '/advertlist'

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Advert.objects.get(pk=id)


# дженерик для удаления товара
class ResponseDeleteView(DeleteView):
    template_name = 'mmorpgapp/responsedelete.html'
    queryset = Response.objects.all()
    success_url = '/responselist'


class RListView(ListView):
    model = Response  # указываем модель, объекты которой мы будем выводить
    template_name = 'mmorpgapp/responselist.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'responses'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон




    def get_queryset(self):
        user = self.request.user
        responses_by_advert_by_user = Response.objects.filter(userTo__id=user.id).order_by('-datetime')
        return responses_by_advert_by_user
